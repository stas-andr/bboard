from django.urls import path
from django.contrib.auth.views import PasswordResetDoneView
from .views import index, other_page
from .views import BBLoginView, BBLogoutView, profile
from .views import ChangeUserInfoView, BBPasswordChangeView, BBPasswordResetView, BBPassrordResetConfirmView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate, DeleteUserView
from .views import by_rubric, detail

app_name = 'main'
urlpatterns = [
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('acсounts/password_reset/done/', PasswordResetDoneView.as_view(
        template_name='main/password_reset_email_sent.html'),
         name='password_reset_done'),
    path('accounts/password_confirm/<uidb64>/<token>/', BBPassrordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password_reset/', BBPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/activate/<str:sign>/', user_activate,
         name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(),
         name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(),
         name='register'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]