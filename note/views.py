from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from note.models import Note
from rest_framework.response import Response
from note.serializers import NoteModelSerializer
# Create your views here.

class NoteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        qs=Note.objects.all()
        serializer=NoteModelSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=NoteModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class NoteDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Note.objects.get(id=id)
        serializer=NoteModelSerializer(qs)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Note.objects.get(id=id)
        serializer=NoteModelSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Note.objects.get(id=id)
        qs.delete()
        return Response({"msg":'deleted'})




