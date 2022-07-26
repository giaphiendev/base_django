from custom_service.models.ModelTechwiz import Subject, User, RevisionClass, ClassTeacherSubject, TimeTable, Student
from custom_service.exceptions import PostNotFound
from django.db import transaction


class RevisionHandler:
    def get_revision_by_teacher(self, teacher_id):
        #  list_revision
        list_time_table = RevisionClass.objects.filter(
            status=1,
            teacher_id=teacher_id
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
            list_time_table_res.append({
                "id_subject": time_table[0],
                "name_subject": time_table[1],
                "name_teacher": time_table[2] + " " + time_table[3],
                "time_table": {
                    "day_of_week": time_table[4],
                    "time_start": time_table[5],
                    "time_end": time_table[6],
                    "id": time_table[7],
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
        ).prefetch_related(
            'time_table_revision_class'
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
                "id_subject": time_table[0],
                "name_subject": time_table[1],
                "name_teacher": time_table[2] + " " + time_table[3],
                "time_table": {
                    "day_of_week": time_table[4],
                    "time_start": time_table[5],
                    "time_end": time_table[6],
                    "id": time_table[7],
                }
            }
            if data['id_subject'] is None or data['time_table']['id'] is None:
                continue
            list_time_table_res.append(data)

        return list_time_table_res

    def update_revision(self, time_table_id, data):
        """
        arg:
            data: {time_table_id: 1, day_of_week: 'monday', end_time: '', start_time: ''}
        """
        TimeTable.objects.filter(id=time_table_id).update(**data)

    def get_revision(self, pk):
        """
        Get revision by id
        """
        try:
            return RevisionClass.objects.get(
                pk=pk,
            )
        except RevisionClass.DoesNotExist:
            raise PostNotFound(f"The Class not found")

    def create_revision(self, data):
        """
        Create revision
        """
        revision = RevisionClass(**data)
        revision.save()

        return revision

    def update_revision_by_admin(self, pk, data):
        """
        Update revision by admin
        """
        with transaction.atomic():
            RevisionClass.objects.filter(pk=pk).update(**data)
            # Update cart
            return self.get_revision(pk)

    def delete_revision(self, pk):
        """
        Delete a revision
        """
        post = self.get_revision(pk)
        post.delete()
