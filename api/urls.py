from django.urls import path

from .views import TeacherDetailView
from .views import TeacherListView
from .views import MarkingSchemeDetailView
from .views import MarkingSchemeListView
from .views import AssessmentDetailView
from .views import AssessmentListView
from .views import TrainerDetailView
from .views import TrainerListView
from .views import ModuleDetailView
from .views import ModuleListView
from .views import KicdDetailView
from .views import KicdListView


urlpatterns =[
path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
path("teacher/<int:id>/",TeacherDetailView.as_view(),name="teacher_detail_view"),
path("markingscheme/",MarkingSchemeListView.as_view(),name="markingscheme_list_view"),
path("markingscheme/<int:id>/",MarkingSchemeDetailView.as_view(),name="markingscheme_detail_view"),
path("assessment/",AssessmentListView.as_view(),name="Assessment_list_view"),
path("Assessment/<int:id>/",AssessmentDetailView.as_view(),name="Assessment_detail_view"),
path("trainer/",TrainerListView.as_view(),name="Trainer_list_view"),
path("Trainer/<int:id>/",TrainerDetailView.as_view(),name="Trainer_detail_view"),
path("module/",ModuleListView.as_view(),name="Module_list_view"),
path("Module/<int:id>/",ModuleDetailView.as_view(),name="Module_detail_view"),
path("kicd/",KicdListView.as_view(),name="Kicd_list_view"),
path("Kicd/<int:id>/",KicdDetailView.as_view(),name="Kicd_detail_view"),
]