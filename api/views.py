from rest_framework.viewsets import ModelViewSet
#from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth import get_user_model
#from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

#class ArticleList(ListCreateAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerialiser

#class ArticleDetail(RetrieveUpdateDestroyAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerialiser
#    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author__username']
    ordering_fields = ['publish','status']
    ordering = ['-publish']
    search_fields = ['title','content','author__username','author__last_name','author__first_name']

    def get_permissions(self):
        if self.action in ['list', 'create']:
              permission_classes = [IsStaffOrReadOnly]
        else:
              permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

#class AuthorRetreive(RetrieveAPIView):                        #made for hyperlink serialzers
#    queryset = get_user_model().objects.filter(is_staff=True)
#    serializer_class = AuthorSerializer





#class UserList(ListCreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerialiser
#    permission_classes = (IsSuperUserOrStaffReadOnly,)

#class UserDetail(RetrieveUpdateDestroyAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerialiser
#    permission_classes = (IsSuperUserOrStaffReadOnly,)
