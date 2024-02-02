from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Post, Tag, Category


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise ValidationError(
                'Заголовок не должен повторяться'
            )
        return title


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'author']

 
