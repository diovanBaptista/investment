from django.test import TestCase

class InvestimentTestCase(TestCase):

    def test_create_inventiment(self):
        from ..models import Investiment,Investor
        from django.contrib.auth.models import User

        # Crie um usuário
        user = User.objects.create(
            username='diovan',
            email='diovan@gmail.com',
            password='diovan1539',  # Corrigido para 'password'
        )

        investidor = Investor.objects.create(
            name="Diovan",
            cpf="123.456.789-10",
            user=user,
        )      

        # Crie uma instância de Inventimento
        investimnet = Investiment.objects.create(
            owner=investidor,
            creation_date="2024-01-20",
            value='200',
            investment_withdrawal=False
        )        

        # Verifique se o usuário e o investidor foram criados corretamente
        self.assertIsNotNone(user)
        self.assertIsNotNone(investidor)
        self.assertIsNotNone(investimnet)
        
        # Verifique se o investidor foi salvo no banco de dados
        self.assertTrue(Investiment.objects.filter(id=investimnet.id).exists())
        print('test_create_investment')
