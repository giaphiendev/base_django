from core.exceptions import UserNotFound
from core.models import User
from custom_service.exceptions import StudentNotFound, SubjectNotFound
from custom_service.models.ModelTechwiz import Grade, Student, Subject


class GradeHandle:
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
