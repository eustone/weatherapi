from django.test import TestCase
from .models import Temperature


# Create your tests here.

class TestTemperature(TestCase):
    def setUp(self) -> None:
        temp=Temperature.objects.create(max_temp=30, min_temp=26)
        temp.save()

    def tearDown(self) -> None:
        pass

    def test_average_result(self):
        # Test must pass
        self.assertEqual(self.temp.max_temp, )

    def test_average_result_fail(self):
        # Test should fail
        pass
