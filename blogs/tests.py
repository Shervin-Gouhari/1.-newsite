from django.test import TestCase
from .models import Blog
from django.urls import reverse
from django.contrib.auth import get_user_model

class BlogsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "shervin",
            password = "1234",
        )
        self.blog = Blog.objects.create(
            title = "testing title",
            body = "testing body",
            author = self.user,
        )
        
    def test__str__(self):
        blog = Blog(title="testing title")
        self.assertEqual(str(blog), blog.title)
        
    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), '/blogs/1/')    

    def test_blog_model(self):
        excepted_title_content = Blog.objects.get(id=1).title
        excepted_body_content = Blog.objects.get(id=1).body
        excepted_author_content = f'{Blog.objects.get(id=1).author}'
        self.assertEqual(f'{self.blog.title}', "testing title")
        self.assertEqual(f'{self.blog.body}', "testing body")
        self.assertEqual(f'{self.blog.author}', "shervin")
        self.assertEqual(excepted_title_content, "testing title")
        self.assertEqual(excepted_body_content, "testing body")
        self.assertEqual(excepted_author_content, "shervin")
        
    def test_create_url_template(self):
        response1 = self.client.post(reverse("create"), {
            "title": "creating title",
            "body": "creating body",
            "author": self.user.id,
        })
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(Blog.objects.last().title, "creating title")
        self.assertEqual(Blog.objects.last().body, "creating body")
        self.assertEqual(Blog.objects.last().author.username, "shervin")
        response2 = self.client.get(reverse("create"))
        self.assertTemplateUsed(response2, "blogs/create.html")
     
    def test_list_url_template(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/list.html")
           
    def test_detail_url_template(self):
        response = self.client.get("/blogs/1/")
        no_response = self.client.get("/blogs/1000000000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "blogs/detail.html")
        
    def test_update_url_template(self):
        response1 = self.client.post(reverse("update", args="1"), {
            "title": "updating title",
            "body": "updating body",
        })
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(Blog.objects.first().title, "updating title")
        self.assertEqual(Blog.objects.first().body, "updating body")
        response2 = self.client.get(reverse("update", args="1"))
        self.assertTemplateUsed(response2, "blogs/edit.html")
        
    def test_delete_url_template(self):
        response2 = self.client.get(reverse("delete", args="1"))
        self.assertTemplateUsed(response2, "blogs/delete.html")
        response1 = self.client.post(reverse("delete", args="1"))
        self.assertEqual(response1.status_code, 302)
        
        