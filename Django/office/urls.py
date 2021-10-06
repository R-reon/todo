from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('five.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/password_change_form/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change_form'),    # 追加
    path('accounts/password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_finish.html'), name='password_change_done'), # 追加
    path('accounts/password_reset_form/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', from_email=' office54@office54.net '), name='password_reset'),
    path('accounts/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_mail_done.html'), name='password_reset_done'),
    path('accounts/password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmation.html'), name='password_reset_confirm'),    # 追加
    path('accounts/password_reset_finish/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_finish.html'), name='password_reset_complete'),
]