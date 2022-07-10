from django.urls import path, include
from .views import ArticleViewSet, UserViewSet
from rest_framework import routers

app_name = 'api'


router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename="articles")          #these are doing same as urls do
router.register('users', UserViewSet, basename="users")

#urlpatterns = router.urls                # good but better to use bellow codes insteed

urlpatterns = [
    path('', include(router.urls)),     #this is better because we can add more routs
#    path('authors/<int:pk>/', AuthorRetreive.as_view(), name='authors-detail'),         # was about hyperlink
]
