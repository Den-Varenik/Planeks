from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):

    def test_get_home_index(self):
        response = self.client.get(reverse("home:index"))
        self.assertEquals(response.status_code, 200)
