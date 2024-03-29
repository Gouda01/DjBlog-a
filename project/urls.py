"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts import views
# from posts.api import post_list_api, post_detail_api
from posts.api import PostListApi, PostDetailApi


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),

    #Posts Url
    path('posts/', views.post_list),
    path('posts/new/', views.create_post),
    path('posts/<int:pk>/', views.post_details),
    path('posts/<int:pk>/edit/', views.edit_post),
    path('posts/<int:pk>/delete/', views.delete_post),

    # Class Based View Urls :
    # path('posts/', views.PostList.as_view()),
    # path('posts/new', views.AddPost.as_view()),
    # path('posts/<int:pk>', views.PostDetail.as_view()),
    # path('posts/<int:pk>/edit', views.EditPost.as_view()),
    # path('posts/<int:pk>/delete', views.DeletePost.as_view()),

    path('summernote/', include('django_summernote.urls')),



    # Api Urls :
    # path('posts/api/', post_list_api),
    path('posts/api' , PostListApi.as_view()),
    # path('posts/api/<int:pk>', post_detail_api),
    path('posts/api/<int:pk>', PostDetailApi.as_view()),


    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
