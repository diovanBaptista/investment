from django.test import TestCase

class WithdrawTestCase(TestCase):

    def test_create_withdraw(self):
        from ..models import Investiment,Investor, Withdraw
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

        withdraw = Withdraw.objects.create(
            investment=investimnet,
            withdrawal_date="2024-05-20",
            value='0',
            withdraw_full_amount=True
        )  

        # Verifique se o usuário e o investidor foram criados corretamente
        self.assertIsNotNone(user)
        self.assertIsNotNone(investidor)
        self.assertIsNotNone(investimnet)
        self.assertIsNotNone(withdraw)
        
        # Verifique se o investidor foi salvo no banco de dados
        self.assertTrue(Withdraw.objects.filter(id=withdraw.id).exists())
        print('test_create_withdraw')
