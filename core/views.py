from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from .models import CustomUser, Student, LibraryHistory, FeesHistory
from .serializers import (
    UserSerializer, UserRegistrationSerializer, LoginSerializer,
    StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer
)
from .permissions import IsAdminUser, IsOfficeStaff, IsLibrarian

# User Registration only done by admin user
class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'message': 'Registered successfully',
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)


# Login View for users
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        })


# Admin:views to manage all CRUD operations of office staff and librarians
class UserManagementViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


#Student Management: (CRUD for Admin, Create/Edit/Delete for Office Staff)
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser, IsOfficeStaff]
        return [permission() for permission in permission_classes]


#library history management views
class LibraryHistoryViewSet(viewsets.ModelViewSet):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsLibrarian]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser, IsOfficeStaff]
        return [permission() for permission in permission_classes]


# Fees History Management views
class FeesHistoryViewSet(viewsets.ModelViewSet):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsOfficeStaff]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser, IsOfficeStaff]
        return [permission() for permission in permission_classes]

