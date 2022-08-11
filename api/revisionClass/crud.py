from custom_service.models.ModelTechwiz import Subject, User, RevisionClass, ClassTeacherSubject, TimeTable

class RevisionHandler:
    def get_revision(self, stu):
        list_revision = []
        class_teacher_sub = ClassTeacherSubject.objects.filter(my_class=stu.my_class).all()
        for class_tea_sub in class_teacher_sub:
            subject = Subject.objects.filter(subject=class_tea_sub.subject).all()
            for sub in subject:
                revision = RevisionClass.objects.filter(subject=sub.subject).first()
                time_table = []
                time = TimeTable.objects.filter(revision_class=revision.pk).all()
                for temp in time:
                    time_table.append({
                        "day_of_week": temp.day_of_week,
                        "start_time": temp.start_time,
                        "end_time": temp.end_time,
                        "teacher": User.objects.filter(pk=revision.teacher).first()
                    })
                list_revision.append({
                    "name": sub.name,
                    "time_table": time
                })
        return list_revision


