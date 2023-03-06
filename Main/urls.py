from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from students import views

schema_view = get_schema_view(
    openapi.Info(
        title="Custom Tinder",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@jva.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_v1 = [
    path('flows/', views.FlowListAPIView.as_view()),
    path('flow/', views.FlowCreateAPIView.as_view()),
    path('directions/', views.DirectionListAPIView.as_view()),
    path('direction/', views.DirectionCreateApiView.as_view()),
    path('students/', views.StudentListAPIView.as_view()),
    path('student/', views.StudentCreateAPIView.as_view()),
    path('student/<int:pk>/', views.StudentDestroyAPIView.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
