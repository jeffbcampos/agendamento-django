from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bcrypt import hashpw, gensalt, checkpw
from naty_agendamento.models import User, Schedule
from naty_agendamento.serializers import UserSerializer, ScheduleSerializer

class CreateAccountView(APIView):
    
    def get(self, request):
        users = User.objects.all()
        users_data = UserSerializer(users, many=True).data
        return Response(users_data)
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        phone = request.data.get('phone')
        password_hash = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')       

        user = User.objects.create(
            name=name,
            email=email,
            password=password_hash,
            phone=phone
        )

        return Response({'msg': 'successufuly', 'password': password_hash})


class LoginView(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password').encode('utf-8')
            user = User.objects.get(email=email)                  
            if checkpw(password, user.password.encode('utf-8')):
                return Response({'msg': 'successufuly'})
            else:
                return Response({'msg': 'wrong password'})            
        except User.DoesNotExist:
            return Response({'msg': 'user not found'}, status=404)
        
class CreateScheduleView(APIView):
    def get(self, request):
        schedules = Schedule.objects.all()
        schedules_data = ScheduleSerializer(schedules, many=True).data
        return Response(schedules_data)
    
    
    def post(self, request):
        id_user = request.data.get('id_user')
        date = request.data.get('date')
        hour = request.data.get('hour')
        description = request.data.get('description')
        
        try:
            user_instance = User.objects.get(id=id_user)
        except User.DoesNotExist:
            return Response({'msg': 'User not found'}, status=404)
        
        schedule = Schedule.objects.create(
            id_user=user_instance,
            date=date,
            hour=hour,
            description=description
        )
        schedule_data = ScheduleSerializer(schedule).data
        return Response({'msg': 'successufuly', 'schedule': schedule_data})