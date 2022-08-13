from custom_service.models.ModelTechwiz import Subject, User, RevisionClass, ClassTeacherSubject, TimeTable, Student


class RevisionHandler:
    def get_revision_by_teacher(self, teacher_id):
        #  list_revision
        list_time_table = RevisionClass.objects.filter(
            status=1,
            teacher_id=teacher_id
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

    def get_revision_optimize(self, stu):
        stu = Student.objects.get(pk=stu)
        # list subject
        list_subject = ClassTeacherSubject.objects.filter(my_class_id=stu.my_class).select_related(
            'subject').values_list('subject_id', flat=True)
        #  list_revision
        list_subject = [item for item in list_subject]
        list_time_table = RevisionClass.objects.filter(
            status=1,
            subject__in=list_subject
        ).prefetch_related('time_table_revision_class'
                           ).values_list(
            "subject__id",
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
            data = {
                "name_subject": time_table[1],
                "name_teacher": time_table[2] + " " + time_table[3],
                "time_table": []
            }

            filtered = RevisionHandler.check_duplicated(list_time_table, time_table[0])
            if not filtered:
                list_time_table_res.append({
                    "name_subject": time_table[1],
                    "name_teacher": time_table[2] + " " + time_table[3],
                    "time_table": []
                })
            else:
                print(filtered)
                # currentClass.lessons.push(time_table)
            # for item in list_time_table:
            #     lesson = {
            #         "day_of_week": item[4],
            #         "time_start": item[5],
            #         "time_end": item[6],
            #         "id": item[7],
            #     }
            #
            # if item[0] == time_table[0]:
            #     list_time_table_res.append(data)
            # else:
            #     data["time_table"].append(lesson)

        """
        const
        res = []
        for (let lesson of data.revision_class) {
            const {name_teacher, name_subject, time_table} = lesson;
            const currentClass = res.find(
                (cls) = > cls.name_subject === lesson.name_subject
            );
            if (!currentClass) {
                res.push({name_teacher, name_subject, lessons: [time_table]})
            } else {
                currentClass.lessons.push(time_table)
            }
        }
        """

        return list_time_table_res

    def update_revision(self, revision_id, data):
        """
        arg:
            data: {time_table_id: 1, day_of_week: 'monday', end_time: '', start_time: ''}
        """
        time_id = data.get('time_table_id')
        del data['time_table_id']
        TimeTable.objects.filter(id=time_id).update(**data)

    @staticmethod
    def check_duplicated(list_item, item):
        for it in list_item:
            if item == it[0]:
                return it
        return None
