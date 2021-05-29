from .models import Schedule,Exercises,User
from rest_framework.fields import CurrentUserDefault
from rest_framework import authentication, permissions,status
from .serializers import ExerciseSerializer, UserCreateSerializer,ScheduleSerializer
from rest_framework.generics import ListCreateAPIView,CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
# Create your views here.
class UserSignupView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class ExercisesListView(ListAPIView):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (JWTAuthentication,)
    queryset = Exercises.objects.all()
    serializer_class = ExerciseSerializer


class ScheduleListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.filter(User = self.request.user)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(User=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
