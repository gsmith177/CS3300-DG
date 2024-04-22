from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import User, Post
from .forms import CustomUserCreationForm, PostForm
from .views import index, posts_page, post_detail, user_page

class ModelTestCase(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create(email='test1@example.com', name='Test User 1', skill_level='Professional')
        self.user2 = User.objects.create(email='test2@example.com', name='Test User 2', skill_level='Intermediate')

        # Create test posts
        self.post1 = Post.objects.create(user=self.user1, location='Test Location 1', num_joined=0)
        self.post2 = Post.objects.create(user=self.user2, location='Test Location 2', num_joined=0)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(self.user1.name, 'Test User 1')
        self.assertEqual(self.user2.skill_level, 'Intermediate')

    def test_post_creation(self):
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(self.post1.location, 'Test Location 1')
        self.assertEqual(self.post2.num_joined, 0)

class FormTestCase(TestCase):
    # Form Tests
    def test_custom_user_creation_form_valid(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'skill_level': 'Beginner',
            'password1': 'testpassword123',
            'password2': 'testpassword123', 
        }
        form = CustomUserCreationForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())


    def test_post_form(self):
        form_data = {
            'location': 'Test Location',
            'num_joined': 0,
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

class ViewTestCase(TestCase):
    # View Tests
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_app/index.html')

    def test_posts_page_view(self):
        response = self.client.get(reverse('posts_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_app/posts_page.html')

    def test_post_detail_view(self):
        # Create a test post
        test_user = User.objects.create(email='test@example.com', name='Test User', skill_level='Professional')
        test_post = Post.objects.create(user=test_user, location='Test Location', num_joined=0)

        # Get the URL for the test post detail page
        url = reverse('post_detail', args=[test_post.pk])

        # Send GET request to the post detail page
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'portfolio_app/post_details.html')

        # Check if the post object is passed to the template context
        self.assertEqual(response.context['post'], test_post)

    # URL Tests
    def test_index_url(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_app/index.html')

    def test_posts_page_url(self):
        url = reverse('posts_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_app/posts_page.html')

    def test_post_detail_url(self):
        test_user = User.objects.create(email='test@example.com', name='Test User', skill_level='Professional')
        test_post = Post.objects.create(user=test_user, location='Test Location', num_joined=0)
        url = reverse('post_detail', args=[test_post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_app/post_details.html')

    def test_user_page_url(self):
        url = reverse('user_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_app/user_page.html')

    # Add more view tests as needed
