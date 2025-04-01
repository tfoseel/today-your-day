from django.test import TestCase
from django.urls import reverse
from recipients.models import Recipient, RollingPaper


class RecipientTemplateViewsTests(TestCase):

    def setUp(self):
        self.recipient = Recipient.objects.create(
            last_name="홍",
            first_name="길동",
            birthday="1999-09-09",
            address="서울시 중구 명동 100"
        )

    def test_invite_view_renders(self):
        url = reverse('recipient-invite', args=[self.recipient.uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipient.name)

    def test_write_rollingpaper_view_get(self):
        url = reverse('write-rollingpaper', args=[self.recipient.uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipient.name)

    def test_write_rollingpaper_view_post_success(self):
        url = reverse('write-rollingpaper', args=[self.recipient.uuid])
        data = {
            "message": "길동 생일 축하해!"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # 리디렉트 확인
        self.assertEqual(RollingPaper.objects.count(), 1)

    def test_write_rollingpaper_over_limit(self):
        url = reverse('write-rollingpaper', args=[self.recipient.uuid])
        data = {
            "message": "x" * 101
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  # 다시 폼 렌더링
        self.assertContains(response, "100자 이하로 작성해주세요.")
        self.assertEqual(RollingPaper.objects.count(), 0)

    def test_recipient_papers_display(self):
        RollingPaper.objects.create(
            recipient=self.recipient, message="테스트 롤링페이퍼")
        url = reverse('recipient-rollingpapers', args=[self.recipient.uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "테스트 롤링페이퍼")

    def test_recipient_detail_api(self):
        url = reverse('recipient-detail-by-uuid', args=[self.recipient.uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("first_name", response.data)
        self.assertEqual(response.data["first_name"], "길동")
