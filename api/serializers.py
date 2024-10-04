from teacher.models import Teacher
from rest_framework import serializers
from markingscheme.models import MarkingScheme
from assessment.models import Assessment
from module.models import Module
from trainer.models import Trainer
from kicd.models import Kicd


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class MarkingSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkingScheme
        fields = "__all__"


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"


class KicdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kicd
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"



class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"
