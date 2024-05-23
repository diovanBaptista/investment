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
 executa oo projeto com o seguinte comando:

```
    python3 manage.py runserver
 ```

## Rotas do Investidor (Investor)

![image](https://github.com/diovanBaptista/investment/assets/84948264/a4a8c9ee-d6b7-4ba2-9bc1-9961a38897db)
> Ao criar um investidor, um usuário correspondente será automaticamente gerado com base nos dados fornecidos, permitindo uma experiência de usuário mais integrada e simplificada. Isso significa que, ao registrar um novo investidor, um usuário será criado simultaneamente, usando as informações fornecidas, como nome de usuário, e-mail e senha. Essa abordagem facilita o processo de registro e elimina a necessidade de criar separadamente uma conta de usuário para cada investidor.

Listar Investidores

Endpoint: /investor/investor/

    GET: Retorna uma lista de todos os investidores cadastrados.
        Nome da View: investor_investor_list

Criar Novo Investidor

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

    GET: Retorna os detalhes de um investidor específico com base no ID.
        Parâmetro: {id} - ID único do investidor.
        Nome da View: investor_investor_read

Atualizar Investidor

Endpoint: /investor/investor/{id}/

    PUT: Atualiza todos os campos de um investidor específico com base no ID.
        Parâmetro: {id} - ID único do investidor.
        Nome da View: investor_investor_update

Atualização Parcial do Investidor

Endpoint: /investor/investor/{id}/

    PATCH: Atualiza parcialmente os campos de um investidor específico com base no ID.
        Parâmetro: {id} - ID único do investidor.
        Nome da View: investor_investor_partial_update

Remover Investidor

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

Endpoint: /investment/investment/

    GET: Retorna uma lista de todos os investimentos cadastrados.
        Nome da View: investment_investment_list

Criar Novo Investimento

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

Endpoint: /investment/investment/{id}/

    GET: Retorna os detalhes de um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_read

Atualizar Investimento

Endpoint: /investment/investment/{id}/

    PUT: Atualiza todos os campos de um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_update

Atualização Parcial do Investimento

Endpoint: /investment/investment/{id}/

    PATCH: Atualiza parcialmente os campos de um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_partial_update

Remover Investimento

Endpoint: /investment/investment/{id}/

    DELETE: Remove um investimento específico com base no ID.
        Parâmetro: {id} - ID único do investimento.
        Nome da View: investment_investment_delete


## Rotas de Saque (Withdraw)

![image](https://github.com/diovanBaptista/investment/assets/84948264/07ff9385-bcbc-471b-b95b-df023f54fff0)
> O modelo de saque foi desenvolvido para permitir que os investidores realizem retiradas dos seus investimentos. Esse modelo possui um campo para o valor do saque e uma opção para sacar o valor total do saldo de investimento sem a necessidade de digitar manualmente. Abaixo estão os detalhes e validações implementadas:

> Chave Estrangeira investment: Este campo estabelece uma relação com o modelo de investimento, indicando de qual investimento o saque está sendo realizado. Um investimento só pode ter um saque associado a ele.

> Campo value: Este campo permite ao investidor digitar o valor que deseja sacar. No entanto, a aplicação não permite saques parciais. Se um valor for inserido, ele deve ser igual ao saldo total do investimento.

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

Endpoint: /withdraw/withdraw/

    GET: Retorna uma lista de todos os saques realizados.
        Nome da View: withdraw_withdraw_list

Criar Novo Saque

Endpoint: /withdraw/withdraw/

    POST: Realiza um novo saque com os dados fornecidos.
        Nome da View: withdraw_withdraw_create
        Corpo da Requisição:

        json

        {
          "value": "string",
          "withdrawal_date": "string (formato: YYYY-MM-DD)",
          "withdraw_full_amount": "boolean",
          "investment": "integer"
        }

Detalhes do Saque

Endpoint: /withdraw/withdraw/{id}/

    GET: Retorna os detalhes de um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_read

Atualizar Saque

Endpoint: /withdraw/withdraw/{id}/

    PUT: Atualiza todos os campos de um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_update

Atualização Parcial do Saque

Endpoint: /withdraw/withdraw/{id}/

    PATCH: Atualiza parcialmente os campos de um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_partial_update

Remover Saque

Endpoint: /withdraw/withdraw/{id}/

    DELETE: Remove um saque específico com base no ID.
        Parâmetro: {id} - ID único do saque.
        Nome da View: withdraw_withdraw_delete


