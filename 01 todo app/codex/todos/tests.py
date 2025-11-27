from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoViewsTests(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title="Write tests",
            description="Add coverage for CRUD",
            due_date=date.today() + timedelta(days=1),
        )

    def test_home_creates_todo(self):
        response = self.client.post(
            reverse("home"),
            {
                "title": "New task",
                "description": "A description",
                "due_date": date.today(),
                "resolved": False,
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Todo.objects.filter(title="New task").exists())

    def test_edit_updates_fields(self):
        response = self.client.post(
            reverse("edit", args=[self.todo.id]),
            {
                "title": "Updated title",
                "description": "Updated description",
                "due_date": self.todo.due_date,
                "resolved": True,
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, "Updated title")
        self.assertTrue(self.todo.resolved)

    def test_toggle_resolved(self):
        response = self.client.get(reverse("toggle", args=[self.todo.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.resolved)

    def test_delete_removes_record(self):
        response = self.client.post(reverse("delete", args=[self.todo.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())

    def test_home_lists_todos(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Write tests")
