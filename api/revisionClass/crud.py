from custom_service.models.ModelTechwiz import Subject, User, RevisionClass, ClassTeacherSubject, TimeTable, Student


class RevisionHandler:
    def get_revision(self, stu):
        stu = Student.objects.get(pk=stu)
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

    def get_revision_optimize(self, stu):
        stu = Student.objects.get(pk=stu)
        # list subject
        list_subject = ClassTeacherSubject.objects.filter(my_class_id=stu.my_class).select_related(
            'subject').values_list('subject_id')
        #  list_revision
        list_time_table = RevisionClass.objects.filter(
            status=1,
            subject__in=[item[0] for item in list_subject]
        ).prefetch_related('time_table_revision_class'
                           ).values_list(
            'subject__name',
            "teacher__last_name",
            "teacher__first_name",
            "time_table_revision_class__day_of_week",
            "time_table_revision_class__start_time",
            'time_table_revision_class__end_time',
            'time_table_revision_class__id',
        )
        list_time_table_res = []
        for time_table in list_time_table:
            list_time_table_res.append({
                "name_subject": time_table[0],
                "name_teacher": time_table[1] + " " + time_table[2],
                "time_table": {
                    "day_of_week": time_table[3],
                    "time_start": time_table[4],
                    "time_end": time_table[5],
                    "id": time_table[6],
                }
            })

        return list_time_table_res

    def update_revision(self, revision_id, data):
        """
        arg:
            data: {time_table_id: 1, day_of_week: 'monday', end_time: '', start_time: ''}
        """
        time_id = data.get('time_table_id')
        del data['time_table_id']
        TimeTable.objects.filter(id=time_id).update(**data)
