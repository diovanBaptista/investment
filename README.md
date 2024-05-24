# # Investments API Coderockr  <img src="https://coderockr.com/assets/images/coderockr.svg" align="right" height="50px" />

Bem-vindo à API de Investimento! Esta API foi desenvolvida para proporcionar uma experiência simplificada e completa para gestão de investimentos. Utilizando Python com o framework Django, oferecemos uma solução abrangente que permite aos usuários criar contas de investimento e efetuar saques de forma eficiente e segura.

## Configuração do Ambiente de Desenvolvimento

1. Instalação do Python
   <p>Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python em python.org.</p>
   
2. Clonar o Repositório
    Clone o repositório da API de Investimento para uma pasta de sua escolha. Abra o terminal e execute o seguinte comando:
   ```
    git clone https://github.com/diovanBaptista/investment.git
   ```
   
4. Criando um Ambiente Virtual
    <p>É recomendável criar um ambiente virtual para isolar as dependências do projeto. Abra o terminal e execute os seguintes comandos: </p>
    
        ```
       Instale o pacote 'virtualenv' se ainda não estiver instalado
   
            pip install virtualenv
        
        Crie um ambiente virtual na pasta do seu projeto
        
            virtualenv venv
        
        Ative o ambiente virtual
         No Windows:
   
        venv\Scripts\activate
        
         No MacOS/Linux:
         
        source venv/bin/activate
        ```


3. Instalando as dependenciado projeto

Com o ambiente virtual ativado,acesse a pasta ate diretorio principal do projeto.
```
    cd investment
 ```
```
    cd coderockr
 ```

mude para a branch de desenvolvimento 
```
    git checkout development 
 ```
instale as dependenciado  executando o seguinte comando:
 ```
    pip install -r requirements-dev.txt
 ```

Após instalar as dependências, execute python3 manage.py migrate para configurar o banco de dados:

```
    python3 manage.py migrate
 ```
Com banco criado, rodamos um comando para criar super usuario:
```
    python3 manage.py createsuperuser
```

preencha o username, email e password:
   ![image](https://github.com/diovanBaptista/investment/assets/84948264/162e285b-216f-460d-bbe6-68b85547bbd8)
> Observação ao digitar a senha ele nao exibira visualmente!


Para rodar os teste unitario feito na api, antes de rodar o servidor execute o segundo comando:
```
   python3 manage.py test investment.tests
```

 executa oo projeto com o seguinte comando:

```
    python3 manage.py runserver
 ```


após rodar porjeto entre no navegador e digite a seguinte url para ser redirecionado ao Swagger

```
    http://localhost:8000/swagger/
 ```


![image](https://github.com/diovanBaptista/investment/assets/84948264/606abd3f-2fb0-4f4d-aa96-acaa1ab8fa35)
> A fim de garantir a segurança e a integridade dos dados em nossa API, é necessário autenticar-se antes de efetuar alterações. Por favor, não utilize o botão 'Authorize' para inserir suas credenciais de usuário e senha.

![image](https://github.com/diovanBaptista/investment/assets/84948264/2bc84e7f-fbd5-4307-a447-b74f0c318372)
> Exemplo username: diovan;  passwoerd: papa1539

![image](https://github.com/diovanBaptista/investment/assets/84948264/82569c82-697f-40a4-99d9-109962bf441c)


## Extra Envio de E-mails

A API possui funcionalidades de envio de e-mails em três situações diferentes:

### 1. Cadastro de Novo Investidor

Após o cadastro de um novo investidor na API, um e-mail de boas-vindas é enviado para informar sobre o sucesso do cadastro e fornecer informações úteis sobre como começar a investir.

![image](https://github.com/diovanBaptista/investment/assets/84948264/6297f9fd-d7f4-489e-a9a7-654a54f74311)


### 2. Realização de Novo Investimento

Após a realização de um novo investimento, um e-mail de confirmação é enviado para fornecer detalhes sobre o investimento realizado, como valor investido e data.

![image](https://github.com/diovanBaptista/investment/assets/84948264/c5838ece-b6d5-4df1-8d69-08589570b245)

### 3. Realização de Saque

Após a realização de um saque, um e-mail de confirmação é enviado para fornecer detalhes sobre o saque realizado, como valor sacado e data.


![image](https://github.com/diovanBaptista/investment/assets/84948264/661bba51-3a64-4607-80dc-596d3f75afc5)




## Rotas do Investidor (Investor)

![image](https://github.com/diovanBaptista/investment/assets/84948264/a4a8c9ee-d6b7-4ba2-9bc1-9961a38897db)
> Ao criar um investidor, um usuário correspondente será automaticamente gerado com base nos dados fornecidos, permitindo uma experiência de usuário mais integrada e simplificada. Isso significa que, ao registrar um novo investidor, um usuário será criado simultaneamente, usando as informações fornecidas, como nome de usuário, e-mail e senha. Essa abordagem facilita o processo de registro e elimina a necessidade de criar separadamente uma conta de usuário para cada investidor.

Listar Investidores

![image](https://github.com/diovanBaptista/investment/assets/84948264/6580c423-c41e-471d-8fd0-6cff0cb4ca16)


![image](https://github.com/diovanBaptista/investment/assets/84948264/b6cc7978-0b2a-49b7-9cc6-9c8cd89ddca5)


Endpoint: /investor/investor/

    GET: Retorna uma lista de todos os investidores cadastrados.
        Nome da View: investor_investor_list

Criar Novo Investidor

![image](https://github.com/diovanBaptista/investment/assets/84948264/47ddda61-bb2f-4341-a70f-2ea2be08ac1a)


![image](https://github.com/diovanBaptista/investment/assets/84948264/2736d194-4c14-4ad8-bf24-e886b04c5689)

Endpoint: /investor/investor/

    POST: Cria um novo investidor com os dados fornecidos.
        Nome da View: investor_investor_create
        Corpo da Requisição:

        json

        {
          "user": {
            "username": "3HbfNtx3lF1ym95t@oH9PdHuJ4QRIaSfqKe97GZZiXBcvL2jwQ8_GWrZC.S+_xvn.ZAJ1KXAkEg8.OniFLJQgK",
            "email": "user@example.com",
            "password": "string"
          },
          "name": "string",
          "cpf": "string"
        }
> É importante observar que, após a criação, a data de criação do usuário estará disponível apenas para leitura nas APIs de consulta (GET)
Detalhes do Investidor

Endpoint: /investor/investor/{id}/

![image](https://github.com/diovanBaptista/investment/assets/84948264/cefd8eab-eeb7-4c6f-bc9e-72f2c46d683b)

![image](https://github.com/diovanBaptista/investment/assets/84948264/f1da7649-c0e8-4a69-a44a-f5cf9326a558)

    GET: Retorna os detalhes de um investidor específico com base no ID.
        Parâmetro: {id} - ID único do investidor.
        Nome da View: investor_investor_read

Atualizar Investidor

![image](https://github.com/diovanBaptista/investment/assets/84948264/4a8f93cc-1b8a-461b-8c06-cc793fcc3b8a)

![image](https://github.com/diovanBaptista/investment/assets/84948264/3a1eb1fa-9e07-40ea-8a1f-9c788d18dccc)


Endpoint: /investor/investor/{id}/


    PUT: Atualiza todos os campos de um investidor específico com base no ID.
        Parâmetro: {id} - ID único do investidor.
        Nome da View: investor_investor_update

Atualização Parcial do Investidor

![image](https://github.com/diovanBaptista/investment/assets/84948264/0b8f7019-355d-4e92-9a4c-f5a7658b203c)

![image](https://github.com/diovanBaptista/investment/assets/84948264/6ca4c2ab-94ff-49fa-8b32-fbd0588e8587)

Endpoint: /investor/investor/{id}/

    PATCH: Atualiza parcialmente os campos de um investidor específico com base no ID.
        Parâmetro: {id} - ID único do investidor.
        Nome da View: investor_investor_partial_update

Remover Investidor

![image](https://github.com/diovanBaptista/investment/assets/84948264/d8b19070-66ac-49cd-b500-58feadb45e06)


Endpoint: /investor/investor/{id}/

    DELETE: Remove um investidor específico com base no ID.
        Parâmetro: {id} - ID único do investidor.
        Nome da View: investor_investor_delete


## Autenticação lib Djoser
   Endpoint de Login de Token (v1)
   POST /v1/auth/token/login/
   
   Use este endpoint para obter um token de autenticação de usuário.
   Parâmetros
   
       data: Objeto contendo os dados de autenticação do usuário.
           username: Nome de usuário do usuário.
           password: Senha do usuário.
   
      Exemplo de Corpo da Requisição
      
      json
      
      {
        "username": "string",
        "password": "string"
      }
      
      Respostas
      
          Código 201: Token de autenticação foi gerado com sucesso.
              Exemplo de Corpo da Resposta:
      
              json
      
              {
                "token": "string"
              }
   
   Endpoint de Logout de Token (v1)
   POST /v1/auth/token/logout/
   
   Use este endpoint para fazer logout do usuário (remover o token de autenticação do usuário).
   Parâmetros
   
      Este endpoint não aceita parâmetros.
      Respostas
   
       Código 201: Logout realizado com sucesso.

## Rotas do Investimento (Investment)

![image](https://github.com/diovanBaptista/investment/assets/84948264/7f28f140-f9ba-4a1e-80d3-4f6c92978676)
> Optei por criar uma modelagem adicional para representar os investimentos na nossa API. Esta modelagem recebe uma chave estrangeira (foreign key - fk) de investidor, estabelecendo uma conexão direta entre os investimentos e os investidores correspondentes.

> Além disso, implementamos validações para garantir a integridade dos dados. Na nossa API, não é permitido criar um investimento com valor negativo ou investir em uma data posterior à data atual. Da mesma forma, não é possível alterar o valor do investimento para um valor negativo ou para uma data posterior à data atual.

> Entretanto, é possível criar um investimento com uma data anterior à data atual, proporcionando flexibilidade ao usuário nesse aspecto.
Listar Investimentos

> Optei por adicionar um campo booleano para cada investimento, denominado "sacado", que serve para verificar se o investimento foi sacado ou não. Quando um investimento é sacado, esse campo é alterado para "true", indicando que o investimento foi resgatado.

> Além disso, introduzi o conceito de "balance" (saldo) na nossa API. O saldo do investimento representa o valor total do investimento antes do resgate, ou seja, inclui o valor inicial investido e os rendimentos acumulados até o momento em que o investimento é sacado.

> Essas adições proporcionam uma visão mais completa e detalhada sobre o estado dos investimentos na nossa plataforma, permitindo ao usuário acompanhar o saldo atual e verificar se um investimento já foi resgatado ou não.


![image](https://github.com/diovanBaptista/investment/assets/84948264/7711ff5a-a6bc-485f-9f68-a6784f598663)
> Segue um exemplo com dois investimentos: um investimento já sacado e outro ainda não sacado. No caso do investimento que foi sacado, o campo "balance" representa o lucro líquido obtido com o investimento, após a dedução do imposto sobre o lucro. Esse imposto é aplicado apenas sobre os ganhos do investimento e é deduzido no momento do saque.

    Investimento Sacado:
        ID: 1
        Balance: $101.56 
        Data de Criação: 23 de Março de 2024
        Valor Investido: $100.00
        Investimento Sacado: Sim
        Proprietário: Usuário de ID 4

    Investimento Não Sacado:
        ID: 2
        Balance: $346.56
        Data de Criação: 23 de Março de 2024
        Valor Investido: $150.00
        Investimento Sacado: Não
        Proprietário: Usuário de ID 4

Listar Investimento

![image](https://github.com/diovanBaptista/investment/assets/84948264/fef6b26e-6f68-42b9-af2f-e9d41cdf9b3d)

![image](https://github.com/diovanBaptista/investment/assets/84948264/4cd4238f-64fb-4f3f-a8af-1f60f7dac103)

> Vale apena obsrvar que também essa apis estão paginadas, no exemplo abaixo coloquei limit 1 sera exibida apenas 1 por pagina na api

![image](https://github.com/diovanBaptista/investment/assets/84948264/1e5ee0ef-5b1c-4f1a-8707-3f041433aaa4)

![image](https://github.com/diovanBaptista/investment/assets/84948264/b53de8b5-88c2-4e8a-85d6-625fa151a2ac)



Endpoint: /investment/investment/

    GET: Retorna uma lista de todos os investimentos cadastrados.
        Nome da View: investment_investment_list

Criar Novo Investimento

![image](https://github.com/diovanBaptista/investment/assets/84948264/2ab7b2a4-d78d-4e38-bd4d-016603abaaec)

![image](https://github.com/diovanBaptista/investment/assets/84948264/4fa67726-6576-439e-bf52-ae6046eeee05)


Endpoint: /investment/investment/

    POST: Cria um novo investimento com os dados fornecidos.
        Nome da View: investment_investment_create
        Corpo da Requisição:

        json

        {
          "creation_date": "string (formato: YYYY-MM-DD)",
          "value": "string",
          "investment_withdrawal": "boolean",
          "owner": "integer"
        }

Detalhes do Investimento

![image](https://github.com/diovanBaptista/investment/assets/84948264/57b84454-9c41-4365-a7e7-9ab7f76c20c9)


![image](https://github.com/diovanBaptista/investment/assets/84948264/2f66a786-2f21-4db5-9710-55fdc58281ca)


Endpoint: /investment/investment/{id}/

    GET: Retorna os detalhes de um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_read

Atualizar Investimento

![image](https://github.com/diovanBaptista/investment/assets/84948264/7ab953a4-e5b9-4a51-acc4-2faa6324a94b)


![image](https://github.com/diovanBaptista/investment/assets/84948264/259c5642-d507-47cd-a129-f82c606ffb14)


Endpoint: /investment/investment/{id}/

    PUT: Atualiza todos os campos de um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_update

Atualização Parcial do Investimento

![image](https://github.com/diovanBaptista/investment/assets/84948264/f56dd682-7c5a-44c1-87f8-e65e5030a4cc)

![image](https://github.com/diovanBaptista/investment/assets/84948264/81128f4b-62ca-4a71-9b79-9244bcf5ac64)


Endpoint: /investment/investment/{id}/

    PATCH: Atualiza parcialmente os campos de um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_partial_update

Remover Investimento

![image](https://github.com/diovanBaptista/investment/assets/84948264/a0305f07-6272-4fdb-9e60-cb87780bc63d)


Endpoint: /investment/investment/{id}/

    DELETE: Remove um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_delete


## Rotas de Saque (Withdraw)

![image](https://github.com/diovanBaptista/investment/assets/84948264/07ff9385-bcbc-471b-b95b-df023f54fff0)
> O modelo de saque foi desenvolvido para permitir que os investidores realizem retiradas dos seus investimentos. Esse modelo possui um campo para o valor do saque e uma opção para sacar o valor total do saldo de investimento sem a necessidade de digitar manualmente. Abaixo estão os detalhes e validações implementadas:

> Chave Estrangeira investment: Este campo estabelece uma relação com o modelo de investimento, indicando de qual investimento o saque está sendo realizado. Um investimento só pode ter um saque associado a ele.

> Campo withdraw_full_amount: Este é um campo booleano que, quando marcado como true, automaticamente define o valor do saque para o saldo total do investimento, sem que o investidor precise inserir manualmente.

    Campo withdraw_date: A data do saque. Existem validações importantes para este campo:
        A data do saque não pode ser anterior à data de criação do investimento.
        A data do saque não pode ser posterior à data atual.

> Além disso, a API calcula o imposto sobre o rendimento do investimento, conforme descrito a seguir:
Cálculo de Imposto

    O imposto é calculado com base na duração do investimento:

    Menos de 1 ano: 22,5%
    De 1 a 2 anos: 18,5%
    Mais de 2 anos: 15%

    O imposto é aplicado apenas sobre o ganho do investimento (diferença entre o saldo atual e o valor inicial investido).
    
> Campo de Valor Final
   O campo valor_final representa o saldo do investimento após a dedução do imposto. Esse valor é calculado automaticamente durante o processo de saque.
   Validações Adicionais

> Restrição de Saques Múltiplos: Um investimento não pode ter mais de um saque associado a ele. Se já existir um saque registrado para um determinado investimento, não será permitido criar um novo saque para o mesmo investimento.


![image](https://github.com/diovanBaptista/investment/assets/84948264/fc95e5e6-c2c7-45a9-8ce1-e5c8e0cd2a1a)
> Exemplo de um Saque



Listar Saques

![image](https://github.com/diovanBaptista/investment/assets/84948264/2d0a5ee0-a56e-450c-b24d-9beb70b3d4eb)

![image](https://github.com/diovanBaptista/investment/assets/84948264/7cdcd440-bea1-4304-94ea-9ad780020003)
> Api tembém é paginada!

Endpoint: /withdraw/withdraw/

    GET: Retorna uma lista de todos os saques realizados.
        Nome da View: withdraw_withdraw_list

Criar Novo Saque

![image](https://github.com/diovanBaptista/investment/assets/84948264/86f4472a-af1f-4163-9091-5144daeaa6f3)


![image](https://github.com/diovanBaptista/investment/assets/84948264/b5cfeae7-a5bf-4bd8-9f26-50b7cfbcf74a)


Endpoint: /withdraw/withdraw/

    POST: Realiza um novo saque com os dados fornecidos.
        Nome da View: withdraw_withdraw_create
        Corpo da Requisição:

        json

        {
          "withdrawal_date": "string (formato: YYYY-MM-DD)",
          "withdraw_full_amount": "boolean",
          "investment": "integer"
        }

Detalhes do Saque

![image](https://github.com/diovanBaptista/investment/assets/84948264/4ab5a5cd-00b6-44d7-a6f0-c3b497bf7ca3)

![image](https://github.com/diovanBaptista/investment/assets/84948264/2013956c-fe8f-49e1-8e26-3c0b95731cf5)


Endpoint: /withdraw/withdraw/{id}/


    GET: Retorna os detalhes de um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_read

Atualizar Saque

![image](https://github.com/diovanBaptista/investment/assets/84948264/6fb16c1e-c223-4971-868c-37e2962e9f2c)



Endpoint: /withdraw/withdraw/{id}/

    PUT: Atualiza todos os campos de um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_update

Atualização Parcial do Saque

![image](https://github.com/diovanBaptista/investment/assets/84948264/ea902657-dcad-462f-9b72-864ecb9dfbd8)

![image](https://github.com/diovanBaptista/investment/assets/84948264/14e3ae3a-6691-4945-acd3-58a758f96376)


Endpoint: /withdraw/withdraw/{id}/

    PATCH: Atualiza parcialmente os campos de um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_partial_update

Remover Saque

![image](https://github.com/diovanBaptista/investment/assets/84948264/0066c71e-483f-4afc-b659-3a6c85475879)


Endpoint: /withdraw/withdraw/{id}/

    DELETE: Remove um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_delete


