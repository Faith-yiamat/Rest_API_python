from django.urls import path
from .views import StudentListView, CourseListViews,TeacherListViews, ClassPeriodListViews, ClassroomListView

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student_list_view"),
    path("Teachers/", TeacherListViews.as_view(), name= "teacher_list_views"),
    path("Course/", CourseListViews.as_view(), name= "course_list_views"),
    path("ClassPeriod/", ClassPeriodListViews.as_view(), name = "classPeriod_list_views"),
    path("classroom/", ClassroomListView.as_view(), name= "classroom_list_views")
]