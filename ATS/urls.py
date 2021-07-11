from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name="ATS"),
    path('signin.html/', views.logIn, name='signin'),
    path('signup.html/', views.signUp, name='signup'),
    path('signout.html/', views.signOut, name='signout'),
    path('contactus.html/', views.index2, name='Contactus'),
    path('technews.html/',views.technews,name='technews'),
    path('uploadpage.html/',views.upload_form,name='Upload'),
    path('JobNotification.html/',views.job,name='Job'),
    path('jobUpload.html/',views.job_notify,name="jup"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)