import pytest
from rest_framework.reverse import reverse
from rest_framework import status


@pytest.mark.django_db
def test_first(api_client, course_factory):
    """ проверка получения 1го курса """
    course = course_factory()
    url = reverse("courses-detail", args=[course.id, ])
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert resp_json["id"] == course.id


@pytest.mark.django_db
def test_second(api_client, course_factory):
    """ проверка получения списка курсов  """
    course = course_factory()
    url = reverse("courses-list")
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1


@pytest.mark.django_db
def test_third(api_client, course_factory):
    """ проверка фильтрации списка курсов по id """
    course3 = course_factory(id=3)
    course5 = course_factory(id=5)
    url = reverse("courses-list")
    resp = api_client.get(url, {'id': 3})
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]["id"] == 3
    resp = api_client.get(url, {'id': 5})
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]["id"] == 5


@pytest.mark.django_db
def test_fourth(api_client, course_factory):
    """ проверка фильтрации списка курсов по name """
    course1 = course_factory(name='physics')
    course2 = course_factory(name='chemistry')
    url = reverse("courses-list")
    resp = api_client.get(url, {'name': 'physics'})
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]["name"] == 'physics'


@pytest.mark.django_db
def test_fifth(api_client):
    """ тест успешного создания курса """
    course = {'name': 'chemistry'}
    url = reverse("courses-list")
    resp = api_client.post(url, course)
    assert resp.status_code == status.HTTP_201_CREATED
    resp = api_client.get(url)
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]["name"] == 'chemistry'


@pytest.mark.django_db
def test_sixth(api_client, course_factory):
    """ тест успешного обновления курса """
    course = course_factory()
    url = reverse("courses-detail", args=[course.id, ])
    new_course = {'name': 'chemistry'}
    resp = api_client.put(url, new_course)
    assert resp.status_code == status.HTTP_200_OK
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp_json["name"] == 'chemistry'


@pytest.mark.django_db
def test_seventh(api_client, course_factory):
    """ тест успешного удаления курса """
    course = course_factory()
    url = reverse("courses-detail", args=[course.id, ])
    resp = api_client.delete(url)
    assert resp.status_code == status.HTTP_204_NO_CONTENT
