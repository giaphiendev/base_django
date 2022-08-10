from core.models import TimeStampMixin, User
from django.db import models

from utils.validators import validate_phone_number


class TermStatus(models.TextChoices):
    TERM1 = 'TERM1'
    TERM2 = 'TERM2'


class MyClass(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "class"


class Student(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="user_student")
    parent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user_student_parent")
    my_class = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="my_class_user")

    class Meta:
        db_table = "student"


class Subject(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "subject"


class Exam(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)
    term = models.CharField(choices=TermStatus.choices, max_length=20, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name="exam_subject")

    class Meta:
        db_table = "exam"


class Grade(TimeStampMixin):
    mark = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True, related_name="grade_exam")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name="grade_student")

    class Meta:
        db_table = "grade"


class ClassTeacherSubject(TimeStampMixin):
    my_class = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True,
                                 related_name="class_teacher_subject_my_class")
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True,
                                related_name="class_teacher_subject_subject")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name="class_teacher_subject_teacher")

    class Meta:
        db_table = "class_teacher_subject"


class StudyResource(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True,
                                related_name="study_resource_subject")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name="study_resource_student")

    class Meta:
        db_table = "study_resource"


class HelpLine(TimeStampMixin):
    title = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True, validators=[validate_phone_number])
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "help_line"


class RevisionClass(TimeStampMixin):
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=1)

    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name="revision_class_subject")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="revision_class_teacher")

    class Meta:
        db_table = "revision_class"


class TimeTable(TimeStampMixin):
    day_of_week = models.CharField(max_length=50, null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)

    revision_class = models.ForeignKey(RevisionClass, on_delete=models.SET_NULL, null=True,
                                       related_name="time_table_revision_class")

    class Meta:
        db_table = "time_table"
