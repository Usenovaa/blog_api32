from rest_framework.test import APIRequestFactory, APITestCase
from .views import PostViewSet
from django.contrib.auth import get_user_model
from .models import Post, Tag, Category
from rest_framework.authtoken.models import Token
from django.urls import reverse


User = get_user_model()


class PostTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(title='cat1')
        self.tag = Tag.objects.create(title='tag1')
        self.tags = [self.tag]

        self.user = User.objects.create_user(email='test@gmail.com', password='12345678', name='test', is_active=True)

        posts = [
            Post(
                author=self.user,
                title='post1',
                body='bla bla bla',
                category=self.category
                ),
            Post(
                author=self.user,
                title='post2', 
                body='hello',
                category=self.category
            ),
                        Post(
                author=self.user,
                title='post3', 
                body='hello dfbgher',
                category=self.category
            )
        ]
        Post.objects.bulk_create(posts)
        self.token = Token.objects.create(user=self.user)
    #     self.authenticate()

    # def authenticate(self):
    #     self.client.credetentials(HTTP_AUTHORIZATION=f'Token: {self.token}')

    # # def test_create(self):
    # #     data = {
    # #         'title': 'post666',
    # #         'body': 'post4',
    # #         'category': self.category,
    # #         'author': self.user
    # #     }

    # #     self.client.force_authenticate(user=self.user)

    # #     # self.authenticate()
    # #     url = reverse('post-list')
    # #     response = self.client.post(url, data)
    # #     print(response)
    # #     print('===============')
    # #     assert Post.objects.get(title=data['title']).body == data['body']




