from django.urls import path
from . import views
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
#from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [


    path("books/",views.BookList.as_view()),
    path("books/<int:pk>",views.BookDetail.as_view()),
    path("schema/",SpectacularAPIView.as_view(), name='schema'),
    path('docs/',SpectacularSwaggerView.as_view(url_name='schema'),name = 'docs'),
    path('',views.home)

]