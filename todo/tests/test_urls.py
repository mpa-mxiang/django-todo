from django.test import TestCase
from django.urls import reverse, resolve
from todo import views

class URLResolutionTest(TestCase):
    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, views.signup)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.user_login)

    def test_todo_url_resolves(self):
        url = reverse('todo')
        self.assertEqual(resolve(url).func, views.todo)

    def test_edit_todo_url_resolves(self):
        url = reverse('edit_todo', args=[1])
        self.assertEqual(resolve(url).func, views.edit_todo)

    def test_delete_todo_url_resolves(self):
        url = reverse('delete_todo', args=[1])
        self.assertEqual(resolve(url).func, views.delete_todo)

    def test_signout_url_resolves(self):
        url = reverse('signout')
        self.assertEqual(resolve(url).func, views.signout)
