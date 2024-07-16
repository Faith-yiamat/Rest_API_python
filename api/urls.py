from django.urls import path
from .views import StudentListView
from .views import CourseListView
from .views import TeacherListView
from .views import ClassPeriodListView
from .views import ClassroomListView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("teacher/", TeacherListView.as_view(), name= "teacher_list_view"),
    path("course/", CourseListView.as_view(), name= "course_list_view"),
    path("classPeriod/", ClassPeriodListView.as_view(), name = "classPeriod_list_view"),
    path("classroom/", ClassroomListView.as_view(), name= "classroom_list_view")
]