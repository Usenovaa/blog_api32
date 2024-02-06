from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
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
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise ValidationError(
                'Заголовок не должен повторяться'
            )
        return title
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     # representation['test'] = 'test' 
    #     # representation['tags'] = instance.tags.all().count()  
    #     return representation 
        # return {'test': 'hello'}
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        # print('================')
        # print(user)
        # print('================')
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(author=user, **validated_data)
        post.tags.add(tags)
        return post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'author']


