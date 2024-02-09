from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from .views import PostViewSet
from django.contrib.auth import get_user_model
from .models import Post, Tag, Category
from rest_framework.authtoken.models import Token
from django.urls import reverse
from collections import OrderedDict
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict
from collections import OrderedDict
User = get_user_model()


class PostTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(title="cat1")
        self.tag = Tag.objects.create(title="tag1", slug="tag1")
        self.tags = [self.tag.slug]

        self.user = User.objects.create_user(
            email="test@gmail.com", password="12345678", name="test", is_active=True
        )

        posts = [
            Post(
                author=self.user,
                title="post1",
                body="bla bla bla",
                category=self.category,
                slug="1",
            ),
            Post(
                author=self.user,
                title="post2",
                body="hello",
                category=self.category,
                slug="2",
            ),
            Post(
                author=self.user,
                title="post3",
                body="hello dfbgher",
                category=self.category,
                slug="3",
            ),
        ]
        Post.objects.bulk_create(posts)
        self.token = Token.objects.create(user=self.user)

    def test_create(self):
        data = {
            "body": "new post",
            "title": "post4",
            "category": self.category,
            # 'tags': self.tags
        }
        self.client.force_authenticate(user=self.user, token=self.token)
        url = reverse("post-list")
        # print(url)
        response = self.client.post(url, data)
        # print(response.status_code)
        # assert response.status_code == 201
        assert Post.objects.filter(author=self.user, body=data["body"]).exists()

    # def test_create(self):
    #     data = {
    #         'body': 'new post',
    #         'title': 'post4',
    #         'category': 'cat1'
    #     }
    #     request = self.factory.post('/posts/', data, format='json')
    #     force_authenticate(request, self.user=user, token=self.token)
    #     view = PostViewSet.as_view({'post': 'create'})
    #     response = view(request)

    #     assert Post.objects.filter(author=user, body=data['body']).exists()

    def test_list(self):
        url = reverse("post-list")
        response = self.client.get(url)
        # print(response.status_code)
        # print(type(response.data))
        # assert response.status_code == 200
        assert type(response.data) == OrderedDict


    def test_retrieve(self):
        slug = Post.objects.all()[0].slug
        url = reverse('post-detail', kwargs={'pk': slug})
        print(url)
        response = self.client.get(url)
        print(response.data)
        assert response.status_code == 200

    
    def test_update(self):
        post = Post.objects.get(title='post1')
        url = reverse('post-detail', kwargs={'pk': post.slug})
        data = {
            'title': 'post update',
            'body': 'update',
            'category': self.category
        }
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.put(url, data)
        print(response.data)
        assert Post.objects.get(slug=post.slug).title == data['title']

    
    def test_delete(self):
        post = Post.objects.get(title='post2')
        url = reverse('post-detail', kwargs={'pk': post.slug})
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.delete(url)
        print(response.status_code)
        # assert response.status_code == 204 
        assert not Post.objects.filter(slug=post.slug).exists()


