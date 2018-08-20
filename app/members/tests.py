from django.test import TestCase


# Create your tests here.
class Errorexec(TestCase):

    def check_number(self):
        self.assertEqual(2, 2)
