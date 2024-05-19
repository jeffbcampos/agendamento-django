from django.test import TestCase
from naty_agendamento.models import User


class TestNatyAgendamento(TestCase):
    def test_something(self):
        self.assertEqual(True, True)


    def test_user_model(self):
        user = User.objects.create(name='Teste', email='teste@teste.com', password='teste123', phone='1234567890')
        self.assertEqual(user.name, 'Teste')
        self.assertEqual(user.email, 'teste@teste.com')
        self.assertEqual(user.password, 'teste123')
        self.assertEqual(user.phone, '1234567890')
