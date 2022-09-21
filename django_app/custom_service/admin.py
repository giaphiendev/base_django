from django.contrib import admin
from .models.ModelTechwiz import (
    MyClass,
    Student,
    Subject,
    Grade,
    ClassTeacherSubject,
    StudyResource,
    HelpLine,
    RevisionClass,
    TimeTable
)

admin.site.register(MyClass)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(ClassTeacherSubject)
admin.site.register(StudyResource)
admin.site.register(HelpLine)
admin.site.register(RevisionClass)
admin.site.register(TimeTable)
