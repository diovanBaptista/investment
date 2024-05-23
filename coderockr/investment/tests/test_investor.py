from django.test import TestCase

class InvestorTestCase(TestCase):

    def test_create_investor(self):
        from ..models import Investor
        from django.contrib.auth.models import User
        # Crie um usuário
        user = User.objects.create(
            username='diovan',
            email='diovan@gmail.com',
            password='diovan1539',  # Corrigido para 'password'
        )

        # Crie uma instância de Investidor associada ao usuário
        investidor = Investor.objects.create(
            name="Diovan",
            cpf="123.456.789-10",
            user=user,
        )        

        # Verifique se o usuário e o investidor foram criados corretamente
        self.assertIsNotNone(user)
        self.assertIsNotNone(investidor)
        
        # Verifique se o investidor foi salvo no banco de dados
        self.assertTrue(Investor.objects.filter(name=investidor.name).exists())
        print('test_create_investor')
