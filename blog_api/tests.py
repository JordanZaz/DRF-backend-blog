from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):

        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):

        self.test_category = Category.objects.create(name='django')

        self.test_user1 = User.objects.create_user(
            username='test_user1', password='123123')

        self.client.login(username=self.test_user1.username, password='123123')

        data = {'title': 'new', 'author': 1,
                'excerpt': 'new', 'content': 'new'}

        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')

        self.test_user1 = User.objects.create_user(
            username='test_user1', password='123123')

        self.test_user2 = User.objects.create_user(
            username='test_user2', password='123123')

        test_post = Post.objects.create(
            category_id=1, title='test_title', excerpt='post excerpt',
            content='post content', slug='test_title', author_id=1,
            status='published')

        client.login(username=self.test_user1.username, password='123123')

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "id": 1,
                "title": "new",
                "author": 1,
                "excerpt": "new",
                "content": "new",
                "status": "published"
            }, format='json')

        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
