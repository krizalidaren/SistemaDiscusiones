from django.test import TestCase
from apps.discuss.models import Question
from apps.users.models import User


class SimpleTest(TestCase):
    def test_save_slug(self):
        user = User.objects.create_user(username='Renato Velasquez Luis', email='rvelasquez@binariaconsultores.com')
        question = Question.objects.create(user=user, title='pregunta 1', description='estas es la descripcion')
        self.assertEqual(question.slug, 'pregunta-1')
