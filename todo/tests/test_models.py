from django.test import TestCase
from django.contrib.auth.models import User
from todo.models import Todo

class TodoModelTest(TestCase):
    def test_todo_creation(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        todo = Todo.objects.create(title='Test Todo', user=user)
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.user, user)
