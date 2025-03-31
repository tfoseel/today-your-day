from PIL import Image
import tempfile
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from recipients.models import Recipient, RollingPaper


def generate_test_image():
    image = Image.new("RGB", (100, 100), color=(255, 0, 0))
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
    image.save(tmp_file, format="JPEG")
    tmp_file.seek(0)
    return tmp_file


class RollingPaperTests(APITestCase):

    def setUp(self):
        self.recipient = Recipient.objects.create(
            name="홍길동",
            birthday="2001-05-03",
            address="서울시 강남구 테헤란로 123"
        )

    def test_create_rollingpaper_success(self):
        url = reverse('rollingpaper-create')  # urls.py에 이름 설정 필요
        data = {
            "recipient": self.recipient.id,
            "message": "생일 축하해요 :)"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RollingPaper.objects.count(), 1)
        self.assertEqual(RollingPaper.objects.first().message, "생일 축하해요 :)")

    def test_create_rollingpaper_with_image(self):
        url = reverse('rollingpaper-create')
        image = generate_test_image()
        data = {
            "recipient": self.recipient.id,
            "message": "생일 축하해!",
            "image": image
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_rollingpaper_over_100_chars(self):
        url = reverse('rollingpaper-create')
        data = {
            "recipient": self.recipient.id,
            "message": "a" * 101  # 101자
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RecipientTests(APITestCase):

    def test_create_recipient_success(self):
        url = reverse('recipient-create')
        data = {
            "name": "홍길동",
            "birthday": "2001-05-03",
            "address": "서울시 강남구 테헤란로 123",
            "phone_number": "01012345678"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipient.objects.count(), 1)
        self.assertEqual(Recipient.objects.first().name, "홍길동")

    def test_create_recipient_missing_required_fields(self):
        url = reverse('recipient-create')
        data = {
            "name": "홍길동"
            # birthday, address 빠짐
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
