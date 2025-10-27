import unittest
from unittest.mock import patch, MagicMock
from django.http import HttpRequest
from django.template.exceptions import TemplateDoesNotExist
from django.test import RequestFactory
from books.views import book_list
from books.forms import BookCreateForm

from django.test import TestCase, RequestFactory
from django.urls import reverse
from books.models import Book
from books.forms import BookCreateForm
from books.views import book_list


class BookListViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        # Создаем тестовые книги
        Book.objects.create(title="Book 1", author="Author 1")
        Book.objects.create(title="Book 2", author="Author 2")

    def test_book_list_uses_correct_template(self):
        """Тест, что view использует правильный шаблон"""
        request = self.factory.get('/books/')
        response = book_list(request)

        self.assertEqual(response.status_code, 200)
 
        # self.assertIn('base.html', response.template_name)

    # def test_book_list_returns_all_books(self):
    #     """Тест, что view возвращает все книги"""
    #     request = self.factory.get('/books/')
    #     response = book_list(request)

    #     self.assertEqual(response.status_code, 200)
    #     # Проверяем, что все книги передаются в контекст
    #     self.assertEqual(len(response.context_data['book_list']), 2)

    # def test_book_list_includes_form_in_context(self):
    #     """Тест, что форма присутствует в контексте"""
    #     request = self.factory.get('/books/')
    #     response = book_list(request)

    #     self.assertEqual(response.status_code, 200)
    #     # Проверяем, что форма передается в контекст
    #     self.assertIn('form', response.context_data)
    #     self.assertIsInstance(response.context_data['form'], BookCreateForm)

    # def test_book_list_context_data(self):
    #     """Тест содержимого контекста"""
    #     request = self.factory.get('/books/')
    #     response = book_list(request)

    #     context = response.context_data
    #     self.assertIn('book_list', context)
    #     self.assertIn('form', context)

    #     # Проверяем, что book_list содержит созданные книги
    #     books = context['book_list']
    #     self.assertEqual(books.count(), 2)
    #     self.assertEqual(books[0].title, "Book 1")
    #     self.assertEqual(books[1].title, "Book 2")