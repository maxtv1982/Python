import pytest
from rest_framework.test import APIClient
from students.models import Student, Course


@pytest.fixture
def api_client():
    """Фикстура для клиента API."""
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        params = {"name": 'Maxim'}
        params.update(kwargs)
        student = Student.objects.create(**params)
        return student

    return factory


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        params = {"name": 'Science'}
        params.update(kwargs)
        course = Course.objects.create(**params)
        return course

    return factory
