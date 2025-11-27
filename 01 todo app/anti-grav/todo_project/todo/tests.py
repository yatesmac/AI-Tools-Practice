from django.test import TestCase, Client
from django.urls import reverse
from .models import TodoItem
from django.utils import timezone

class TodoModelTest(TestCase):
    def test_todo_string_representation(self):
        todo = TodoItem(title="Test Task")
        self.assertEqual(str(todo), "Test Task")

class TodoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.todo = TodoItem.objects.create(
            title="Existing Task",
            description="Test Description",
            due_date=timezone.now()
        )

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Existing Task")

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': '2023-12-31',
            'is_completed': False
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertTrue(TodoItem.objects.filter(title='New Task').exists())

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo_update', args=[self.todo.pk]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'due_date': '2023-12-31',
            'is_completed': True
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Task')
        self.assertTrue(self.todo.is_completed)

    def test_todo_delete_view(self):
        response = self.client.post(reverse('todo_delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TodoItem.objects.filter(pk=self.todo.pk).exists())

    def test_todo_toggle_view(self):
        # Initially False (default)
        self.assertFalse(self.todo.is_completed)
        
        # Toggle to True
        response = self.client.get(reverse('todo_toggle', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_completed)
        
        # Toggle back to False
        response = self.client.get(reverse('todo_toggle', args=[self.todo.pk]))
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.is_completed)
