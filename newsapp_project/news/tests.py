from django.test import TestCase
from django.urls import reverse
from .models import *


# Create your tests here.

class HomePageViewTest(TestCase): 
    def setUp(self):
        self.post1 = Post.objects.create(text='Test Post 1') 
        self.post2 = Post.objects.create(text='Test Post 2') 
        self.url = reverse('home')   
         
    def test_home_page_status_code(self): 
        response = self.client.get(self.url) 
        self.assertEqual(response.status_code, 200) 
 
    def test_home_page_uses_correct_template(self): 
        response = self.client.get(self.url) 
        self.assertTemplateUsed(response, 'index.html') 
 
    def test_home_page_displays_posts(self): 
        response = self.client.get(self.url) 
        self.assertContains(response, self.post1.text) 
        self.assertContains(response, self.post2.text) 
 
    def test_home_page_uses_correct_context_object_name(self): 
        response = self.client.get(self.url) 
        self.assertTrue(response.context['all_posts_list']) 
 
class PostModelTest(TestCase): 
    def setUp(self): 
        self.post = Post.objects.create(text='Test Post Content') 
 
    def test_text_content(self): 
        post = Post.objects.get(id=1) 
        expected_object_name = f'{post.text[:50]}' 
        self.assertEqual(expected_object_name, str(post))