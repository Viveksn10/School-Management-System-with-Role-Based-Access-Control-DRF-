from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegistrationView, LoginView, UserManagementViewSet,
    StudentViewSet, LibraryHistoryViewSet, FeesHistoryViewSet
)

router = DefaultRouter()
router.register(r'users', UserManagementViewSet)#for all users
router.register(r'students', StudentViewSet)#for student management
router.register(r'library-history', LibraryHistoryViewSet)#for library management
router.register(r'fees-history', FeesHistoryViewSet)#fees history management

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),#registering a user(admin,office staff or librarian)
    path('login/', LoginView.as_view(), name='user-login'),#logging into user
]
