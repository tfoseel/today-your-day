from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserAuthActionsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name="승우",
            nickname="테스트승우",
            birthday="2000-08-06",
            phone_number="01022223333",
            password="pass1234"
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)
        self.auth_header = {
            "HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

    def test_get_user_profile(self):
        url = reverse("me")  # /users/me/
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "승우")
        self.assertEqual(response.data["phone_number"], "01022223333")

    def test_delete_user_account(self):
        url = reverse("me")  # /users/me/
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(User.objects.filter(
            phone_number="01022223333").exists())

    def test_logout(self):
        url = reverse("logout")  # /users/logout/
        data = {"refresh": str(self.refresh)}
        response = self.client.post(url, data, **self.auth_header)
        self.assertEqual(response.status_code, 200)
