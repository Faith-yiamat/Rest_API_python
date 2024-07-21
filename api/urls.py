from django.urls import path
from .views import StudentListView
from .views import CourseListView
from .views import TeacherListView
from .views import ClassPeriodListView
from .views import ClassroomListView
from .views import StudentDetailsView
from .views import TeacherDetailsView
from .views import ClassPeriodDetailsView
from .views import ClassroomDetailsView
from .views import CourseDetailsView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("teacher/", TeacherListView.as_view(), name= "teacher_list_view"),
    path("course/", CourseListView.as_view(), name= "course_list_view"),
    path("classPeriod/", ClassPeriodListView.as_view(), name = "classPeriod_list_view"),
    path("classroom/", ClassroomListView.as_view(), name= "classroom_list_view"),
    path("students/<int:id>/", StudentDetailsView.as_view(), name= "student_detail_view"),
    path("teacher/<int:id>/", TeacherDetailsView.as_view(), name= "teacher_detail_view"),
    path("classroom/<int:id>/", ClassroomDetailsView.as_view(), name= "classroom_detail_view"),
    path("class_period/<int:id>/", ClassPeriodDetailsView.as_view(), name= "class_period_detail_view"),
    path("course/<int:id>/", CourseDetailsView.as_view(), name= "course_detail_view"),


    




]