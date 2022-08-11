from custom_service.exceptions import ExamNotFound, StudentNotFound, GradeNotFound
from custom_service.models.ModelTechwiz import Grade, Student, Exam


class GradeHandle:
    def add_grade(self, data):
        '''
        arg:
            data: {student: 123, exam: 123, mark: 10, *description: 'text'}
        return:
        '''
        try:
            stu = Student.objects.get(pk=data.get('student'))
            exam = Exam.objects.get(pk=data.get('exam'))
            Grade.objects.create(student=stu, exam=exam, mark=data.get('mark'),
                                 description=data.get('description', None))
        except Exam.DoesNotExist:
            raise ExamNotFound('Exam not found')
        except Student.DoesNotExist:
            raise StudentNotFound('Student not found')

    def update_grade(self, data):
        '''
        arg:
            data: {student: 123, exam: 123, mark: 10, *description: 'text'}
        return:
        '''
        try:
            stu = Student.objects.get(pk=data.get('student'))
            exam = Exam.objects.get(pk=data.get('exam'))

            grade = Grade.objects.filter(student=stu, exam=exam).first()
            grade.mark = data.get('mark')
            grade.description = data.get('description')

            grade.save()
        except Exam.DoesNotExist:
            raise ExamNotFound('Exam not found')
        except Grade.DoesNotExist:
            raise GradeNotFound('Grade not found')
        except Student.DoesNotExist:
            raise StudentNotFound('Student not found')
