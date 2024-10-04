from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from teacher.models import Teacher
from .serializers import TeacherSerializer
from markingscheme.models import MarkingScheme
from .serializers import MarkingSchemeSerializer
from assessment.models import Assessment
from .serializers import AssessmentSerializer
from module.models import Module
from .serializers import ModuleSerializer
from trainer.models import Trainer
from .serializers import TrainerSerializer
from django.shortcuts import get_object_or_404
from kicd.models import Kicd
from .serializers import KicdSerializer
# Create your views here.


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id) 
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    

class MarkingSchemeListView(APIView):
    def get(self, request):
        markingschemes = MarkingScheme.objects.all()
        serializer = MarkingSchemeSerializer(markingschemes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MarkingSchemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkingSchemeDetailView(APIView):
    def get(self, request, id):
        markingschemes = MarkingScheme.objects.get(id=id) 
        serializer = MarkingSchemeSerializer(markingschemes)
        return Response(serializer.data)
    
    def put(self, request, id):
        markingschemes = MarkingScheme.objects.get(id=id)
        serializer = MarkingSchemeSerializer(markingschemes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        markingscheme = MarkingScheme.objects.get(id=id)
        markingscheme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AssessmentListView(APIView):
    def get(self, request):
        assessments = Assessment.objects.all()
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AssessmentDetailView(APIView):
    def get(self, request, pk):
        try:
            assessment = Assessment.objects.get(pk=pk)
        except Assessment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)
    def put(self, request, pk):
        try:
            assessment = Assessment.objects.get(pk=pk)
        except Assessment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AssessmentSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            assessment = Assessment.objects.get(pk=pk)
        except Assessment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    


class TrainerListView(APIView):
    def get(self, request):
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TrainerDetailView(APIView):
    def get(self, request, id):
        trainers = Trainer.objects.get(id=id)
        serializer = TrainerSerializer(trainers)
        return Response(serializer.data)
    def put(self, request, id):
        trainers = Trainer.objects.get(id=id)
        serializer = TrainerSerializer(trainers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        trainer = Trainer.objects.get(id=id)
        trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ModuleListView(APIView):
    def get(self, request):
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModuleDetailView(APIView):
    def get(self, request, id):
        module = get_object_or_404(Module, id=id)
        serializer = ModuleSerializer(module)
        return Response(serializer.data)

    def put(self, request, id):
        module = get_object_or_404(Module, id=id)
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        module = get_object_or_404(Module, id=id)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class KicdListView(APIView):
    def get(self, request):
        kicds = Kicd.objects.all()
        serializer = KicdSerializer(kicds, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = KicdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class KicdDetailView(APIView):
    def get(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)
        serializer = KicdSerializer(kicd)
        return Response(serializer.data)
    def put(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)
        serializer = KicdSerializer(kicd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)
        kicd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
