from core.exceptions import UserNotFound
from core.models import User
from custom_service.exceptions import StudentNotFound, SubjectNotFound
from custom_service.models.ModelTechwiz import Grade, Student, Subject, NameExam, TermStatus, ClassTeacherSubject, \
    MyClass


class GradeHandle:

    def list_of_grade_by_class(self, data):
        '''
        arg:
            data: {class_id: 123, subject_id: 123, term: TERM1 # TERM2}
        return:
        '''
        # get list student_id
        list_students = Student.objects.filter(my_class_id=data.get("class_id")).values_list("id", flat=True)
        # get list grade by student id
        list_grades = Grade.objects.filter(subject_id=data.get('subject_id'), term=data.get('term'),
                                           student_id__in=list_students).select_related('student').select_related(
            "student__user").all()
        final = []
        middle = []
        assignment = []
        for grade in list_grades:
            data = {
                "student_name": grade.student.user.first_name + ' ' + grade.student.user.last_name,
                "grade": grade.mark,
                "exam_date": grade.exam_date
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
                "grades": assignment,
            },
            {
                "exam_name": NameExam.MIDDLE,
                "grades": middle,
            },
            {
                "exam_name": NameExam.FINAL,
                "grades": final,
            },
        ]

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
            print('data: ', data)
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
            data: {student: 123, exam: 123, mark: 10, *description: 'text'}
        return:
        '''
        pass
        # try:
        #     stu = Student.objects.get(pk=data.get('student'))
        #     exam = Exam.objects.get(pk=data.get('exam'))
        #
        #     grade = Grade.objects.filter(student=stu, exam=exam).first()
        #     grade.mark = data.get('mark')
        #     grade.description = data.get('description')
        #
        #     grade.save()
        # except Exam.DoesNotExist:
        #     raise ExamNotFound('Exam not found')
        # except Grade.DoesNotExist:
        #     raise GradeNotFound('Grade not found')
        # except Student.DoesNotExist:
        #     raise StudentNotFound('Student not found')

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
        grade = Grade.objects.filter(created_by_id=teacher_id).order_by('-created_by').first()

        if grade is None:
            return {}

        exam = grade.type_exam
        subject = grade.subject
        last_update = grade.created_at
        student = Student.objects.filter(id=grade.student_id).first()
        my_class = MyClass.objects.filter(id=student.my_class.id).first()
        list_student_id = Student.objects.filter(my_class_id=my_class.id).values_list('id', flat=True)

        list_student_has_grade = Grade.objects.filter(
            created_by_id=teacher_id,
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
