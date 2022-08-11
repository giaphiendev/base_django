import datetime

from custom_service.exceptions import StudentNotFound
from custom_service.models.ModelTechwiz import Student, ClassTeacherSubject, Grade, TermStatus


class ReportHandle:
    def get_report_grade(self, student_id):
        try:
            stu = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            raise StudentNotFound("Student not found")
        class_teacher_sub = ClassTeacherSubject.objects.filter(my_class=stu.my_class).select_related(
            "subject").all()
        list_completed_exam = Grade.objects.filter(student=stu,
                                                   start_year__gte=datetime.datetime.now().year).select_related(
            "subject").all()
        list_sub = [item.get('subject__name') for item in class_teacher_sub.values("subject__name")]

        term1 = []
        term2 = []
        for sub in list_sub:
            for completed_exam in list_completed_exam:
                data = {
                    "subject_name": sub
                }
                if sub == completed_exam.subject.name:
                    data["exams"] = {
                        "type_exam": completed_exam.type_exam,
                        "grade": completed_exam.mark
                    }
                    if completed_exam.term == TermStatus.TERM1:
                        term1.append(data)
                    if completed_exam.term == TermStatus.TERM2:
                        term2.append(data)

        all_exams_count = len(class_teacher_sub) * 2 * 3  # subject * len(term) * 3 (final, assignment, middle)
        completed_exams_count = len(list_completed_exam)

        return {
            "academic_progress": {
                "all_exams_count": all_exams_count,
                "completed_exams_count": completed_exams_count
            },
            "report_card": {"term1": term1, "term2": term2}
        }
