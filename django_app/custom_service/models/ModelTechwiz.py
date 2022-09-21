from core.models import TimeStampMixin, User
from django.db import models

from utils.validators import validate_phone_number


class TermStatus(models.TextChoices):
    TERM1 = 'TERM1'
    TERM2 = 'TERM2'


class NameExam(models.TextChoices):
    MIDDLE = 'MIDDLE'
    FINAL = 'FINAL'
    ASSIGNMENT = 'ASSIGNMENT'


class MyClass(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "class"

    def __str__(self):
        return self.name


class Student(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="user_student")
    parent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name="user_student_parent")
    my_class = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="my_class_user")

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.user.username


class Subject(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "subject"

    def __str__(self):
        return self.name


#
# class Exam(TimeStampMixin):
#     name = models.CharField(choices=NameExam.choices, max_length=255, blank=True, null=True)
#     term = models.CharField(choices=TermStatus.choices, max_length=20, null=True, blank=True)
#     weight = models.FloatField(null=True, blank=True)
#     subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name="exam_subject")
#
#     class Meta:
#         db_table = "exam"
#
#     def __str__(self):
#         return self.name
#

class Grade(TimeStampMixin):
    mark = models.FloatField(blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    type_exam = models.CharField(choices=NameExam.choices, max_length=50, blank=True, null=True)
    term = models.CharField(choices=TermStatus.choices, max_length=20, null=True, blank=True)
    exam_date = models.DateField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="grade_teacher")
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name="grade_subject")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name="grade_student")

    class Meta:
        db_table = "grade"

    def __str__(self):
        return f'{self.term}-{self.type_exam}-{self.mark}'


class ClassTeacherSubject(TimeStampMixin):
    my_class = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True,
                                 related_name="class_teacher_subject_my_class")
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True,
                                related_name="class_teacher_subject_subject")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name="class_teacher_subject_teacher")

    class Meta:
        db_table = "class_teacher_subject"

    def __str__(self):
        return f'{self.subject.name}-{self.my_class.name}'


class StudyResource(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True,
                                related_name="study_resource_subject")

    class Meta:
        db_table = "study_resource"

    def __str__(self):
        return self.name


class HelpLine(TimeStampMixin):
    title = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True, validators=[validate_phone_number])
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "help_line"

    def __str__(self):
        return self.title


class RevisionClass(TimeStampMixin):
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=1)

    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True, related_name="revision_class_subject")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="revision_class_teacher")

    class Meta:
        db_table = "revision_class"

    def __str__(self):
        return f"RevisionClass - {self.subject.name}"


class TimeTable(TimeStampMixin):
    day_of_week = models.CharField(max_length=50, null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)

    revision_class = models.ForeignKey(RevisionClass, on_delete=models.SET_NULL, null=True,
                                       related_name="time_table_revision_class")

    class Meta:
        db_table = "time_table"

    def __str__(self):
        return f"TimeTable - {self.revision_class.status}"


class DeviceTokenPushNotification(TimeStampMixin):
    token = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name="device_token_push_notification_user")

    class Meta:
        db_table = "device_token_push_notification"

    def __str__(self):
        return f"id - {self.id} - user: {self.user.username}"
