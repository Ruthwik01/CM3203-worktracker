from django.test import TestCase
from django.urls import reverse


class UrlTest(TestCase):
    def test_dashboard_url(self):
        url = reverse('dashboard')
        self.assertEqual(url, '/dashboard/')

    def test_assessments_url(self):
        url = reverse('show_assessments')
        self.assertEqual(url, '/assessments/')
    
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')
    
    def test_tasks_url(self):
        url = reverse('tasks')
        self.assertEqual(url, '/todo/')

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(url, '/register/')


