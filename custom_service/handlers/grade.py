from datetime import datetime
from django.db.models import Q, Avg
from dateutil.relativedelta import relativedelta

from core.exceptions import UserNotFound
from core.models import User
from custom_service.exceptions import StudentNotFound, SubjectNotFound
from custom_service.models.ModelTechwiz import Grade, Student, Subject, NameExam, MyClass, ClassTeacherSubject


class GradeHandle:

    def list_of_grade_by_class(self, data):
        '''
        arg:
            data: {class_id: 123, subject_id: 123, term: 1 # 2}
        return:
        '''
        term = 'TERM1' if int(data.get('term')) == 1 else 'TERM2'
        # get list student_id
        list_students = Student.objects.filter(my_class_id=data.get("class_id")).values_list("id", flat=True)
        # get list grade by student id
        list_grades = Grade.objects.filter(subject_id=data.get('subject_id'), term=term,
                                           student_id__in=list_students).select_related('student').select_related(
            "student__user").all()
        final = []
        middle = []
        assignment = []
        for grade in list_grades:
            data = {
                "student_name": grade.student.user.first_name + ' ' + grade.student.user.last_name,
                "grade": grade.mark,
                "exam_date": grade.exam_date,
                "id": grade.student.id,
                "grade_id": grade.id,
                "subject_id": grade.subject_id,
            }
            if grade.type_exam == NameExam.MIDDLE:
                middle.append(data)
            if grade.type_exam == NameExam.FINAL:
                final.append(data)
            if grade.type_exam == NameExam.ASSIGNMENT:
                assignment.append(data)
        return [
            {
                "exam_name": NameExam.ASSIGNMENT,
                "term": term,
                "grades": assignment,
            },
            {
                "exam_name": NameExam.MIDDLE,
                "term": term,
                "grades": middle,
            },
            {
                "exam_name": NameExam.FINAL,
                "term": term,
                "grades": final,
            },
        ]

    def get_grade_family(self, student_id, term):
        '''
        arg:
            student_id:
            term: 1 # 2
        return:
        {
            term1: [{subject_id: "", subject_name:"", mark: '', exam_date:"", }],
            term2: [{subject_id: "", subject_name:"", mark: '', exam_date:"", }]
        }

        validate by start_year, end_year
        1/9 => 30/8
        '''
        date_start_year = datetime(datetime.now().year, 9, 1).date()
        # get list subject
        if datetime.now().date() > date_start_year:
            all_grade = Grade.objects.filter(student_id=student_id, start_year=datetime.now().year).select_related(
                'subject').all()
        else:
            all_grade = Grade.objects.filter(student_id=student_id, end_year=datetime.now().year).select_related(
                'subject').all()

        term = 'TERM1' if int(term) == 1 else 'TERM2'

        all_grade = all_grade.filter(term=term).all()
        list_subject_id = []
        for sub in all_grade:
            list_subject_id.append((sub.subject.id, sub.subject.name))

        list_subject_id = list(set(list_subject_id))
        res = []
        for each_sub in list_subject_id:
            data = {
                'subject_id': each_sub[0],
                'subject_name': each_sub[1],
            }
            for grade in all_grade:
                if grade.subject_id != each_sub[0]:
                    continue
                else:
                    data['exam_date'] = grade.exam_date
                    data['grade_id'] = grade.id
                    if grade.type_exam == NameExam.ASSIGNMENT:
                        data['ASSIGNMENT'] = grade.mark
                    elif grade.type_exam == NameExam.MIDDLE:
                        data['MIDDLE'] = grade.mark
                    elif grade.type_exam == NameExam.FINAL:
                        data['FINAL'] = grade.mark
            res.append(data)

        return res

    def add_grade(self, data):
        '''
        arg:
            data: {student_id: 123, subject_id: 123, exam: 123, mark: 10, *description: 'text'}
        return:
        '''
        try:
            created_by = User.objects.get(pk=data.get('teacher_id'))
            student = Student.objects.get(pk=data.get('student_id'))
            subject = Subject.objects.get(pk=data.get('subject_id'))
            del data["teacher_id"]
            del data["student_id"]
            del data["subject_id"]
            grade = Grade(created_by=created_by, subject=subject, student=student, **data)
            grade.save()
            return grade
        except User.DoesNotExist:
            raise UserNotFound('User not found')
        except Subject.DoesNotExist:
            raise SubjectNotFound('Subject not found')
        except Student.DoesNotExist:
            raise StudentNotFound('Student not found')

    def update_grade(self, data):
        '''
        arg:
            data: { grade_id: 123, mark: 10, *description: 'text'}
        return:
        '''
        grade = Grade.objects.filter(id=data.get('grade_id')).first()
        grade.mark = data.get('mark')
        grade.exam_date = data.get('exam_date')
        grade.description = data.get('description')
        grade.save()
        return grade

    def get_input_grade(self, teacher_id):
        '''
        arg
            teacher_id: 1
        return:
            {
                class: {
                        name: '',
                        id: '',
                    },
                subject: {
                        name: '',
                        id: '',
                },
                total_student: 10,
                has_grade_student: 7,
                exam: 'final',
                last_update: ''
            }
        '''

        grade1 = Grade.objects.filter(created_by_id=teacher_id).order_by('-created_by').first()

        grade2 = Grade.objects.filter(created_by_id=teacher_id).filter(
            ~Q(term=grade1.term) | ~Q(type_exam=grade1.type_exam) | ~Q(
                student__my_class_id=grade1.student.my_class.id)).order_by(
            '-created_by').first()

        grade3 = Grade.objects.filter(created_by_id=teacher_id).filter(
            ~Q(term__in=[grade1.term, grade2.term]) | ~Q(type_exam__in=[grade1.type_exam, grade2.type_exam]) | ~Q(
                student__my_class_id__in=[grade1.student.my_class.id, grade2.student.my_class.id])).order_by(
            '-created_by').first()

        top_student = self.top_3_grade(teacher_id)
        average_grades = self.average_grades_subject(teacher_id)

        return {
            "recentExams": [self.filter_exam(grade1), self.filter_exam(grade2), self.filter_exam(grade3)],
            "top_student": top_student,
            "average_grades": average_grades
        }

    def filter_exam(self, grade):
        if grade is None:
            return {}

        exam = grade.type_exam
        subject = grade.subject
        last_update = grade.created_at
        student = Student.objects.filter(id=grade.student_id).first()
        my_class = MyClass.objects.filter(id=student.my_class.id).first()
        list_student_id = Student.objects.filter(my_class_id=my_class.id).values_list('id', flat=True)

        list_student_has_grade = Grade.objects.filter(
            created_by_id=grade.created_by.id,
            type_exam=exam,
            start_year=grade.start_year,
            student_id__in=list_student_id
        ).count()
        data = {
            "class": {
                "name": my_class.name,
                "id": my_class.id,
            },
            "subject": {
                "name": subject.name,
                "id": subject.id,
            },
            "total_student": len(list_student_id),
            "has_grade_student": list_student_has_grade,
            "exam": exam,
            "last_update": last_update
        }
        return data

    def top_3_grade(self, teacher_id):
        if teacher_id is None:
            return {}
        last_month = datetime.now() - relativedelta(months=1)

        top_grade = Grade.objects.filter(
            created_by_id=teacher_id,
            created_at__gte=last_month,
        ).order_by('-mark') \
            .select_related('student') \
            .select_related('student__my_class') \
            .select_related("student__user").values(
            'id',
            'student_id',
            'student__user__first_name',
            'student__user__last_name',
            'mark',
            'student__my_class__name',
            'student__my_class__id',
            'type_exam',
            'term',
        )[:3]

        res = []
        for student in top_grade:
            res.append({
                "grade_id": student.get('id'),
                "student_id": student.get('student_id'),
                "student_name": student.get('student__user__first_name') + " " + student.get(
                    'student__user__first_name'),
                "mark": student.get('mark'),
                "class_id": student.get('student__my_class__id'),
                "class_name": student.get('student__my_class__name'),
                "type_exam": student.get('type_exam'),
                "term": student.get('term'),
            })

        return res

    def average_grades_subject(self, teacher_id):
        """
        get list subject
        tinh average of each subject
        return
        """
        list_subjects = Subject.objects.filter(
            class_teacher_subject_subject__teacher_id=teacher_id
        ).values_list('id', 'name').all()

        res = []
        for sub_id in set(list_subjects):
            grade = Grade.objects.filter(subject_id=sub_id, created_by_id=teacher_id).values_list('mark', flat=True)
            if len(grade) > 0:
                res.append({
                    "subject_id": sub_id[0],
                    "subject_name": sub_id[1],
                    "average_mark": round(sum(grade) / len(grade), 2)
                })

        return res
