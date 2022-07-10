from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin


#class AuthorSerializer(serializers.ModelSerializer):     #its about nested serializers( todarto )
#    class Meta:
#        model = get_user_model()
#        fields = ["id","username","last_name","first_name"]

class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
#    author = AuthorSerializer()                            #related to above(nested serializers)
#    author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')   # wrotten for hyperlinks
    def get_author(self, obj):
        return {
             "usename": obj.author.username,
             "first_name": obj.author.first_name,
             "last_name": obj.author.last_name,
        }
    author = serializers.SerializerMethodField("get_author")
    class Meta:
        model = Article
        #fields = ("title", "slug", "author", "content", "publish", "status")
        #exclude = ('created', 'updated')    #means everything except...
        fields = "__all__"
    def validate_title(self, value):
        filter_list = ["javascript","laravel","php"]

        for i in filter_list:
            if i in value:
                raise serializers.ValidationError('plz do not use these words! : {}'.format(i))

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
