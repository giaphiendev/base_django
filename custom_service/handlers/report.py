from custom_service.models.ModelTechwiz import Student, ClassTeacherSubject, Grade, TermStatus


class ReportHandle:
    def get_report_grade(self, stu):
        pass
        # class_teacher_sub = ClassTeacherSubject.objects.filter(my_class=stu.my_class).all()
        # list_exams = []
        # report_card = []
        #
        # for class_tea_sub in class_teacher_sub:
        #     exams = Exam.objects.filter(subject=class_tea_sub.subject).all()
        #     term1 = []
        #     term2 = []
        #     for exam in exams:
        #         list_exams.append(exam)
        #         if exam.term == TermStatus.TERM1:
        #             grade = Grade.objects.filter(exam=exam, student=stu).first()
        #             term1.append({'name': exam.name, "grade": grade.mark if grade is not None else None})
        #         elif exam.term == TermStatus.TERM2:
        #             grade = Grade.objects.filter(exam=exam, student=stu).first()
        #             term2.append({'name': exam.name, "grade": grade.mark if grade is not None else None})
        #
        #     report_card.append({
        #         "name": class_tea_sub.subject.name,
        #         'term1': term1,
        #         'term2': term2
        #     })
        #
        # all_exams_count = len(list_exams)
        # completed_exams_count = len(Grade.objects.filter(student=stu))
        #
        # return {
        #     "academic_progress": {
        #         "all_exams_count": all_exams_count,
        #         "completed_exams_count": completed_exams_count
        #     },
        #     "report_card": report_card
        # }
