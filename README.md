# API REST - Resumo
Este repositório possui a atividade de uma Simples API REST, alterando um banco de dados local.
Alterando o modelo previsto, adicionei mais informações ao produto para que pudesse ser um carro 
e adicionei informações para o usuário, apesar de ambas as informações não serem relacionadas, podem vir
estarem relacionadas para um simples projeto de mercado online.

Abaixo estão algumas informações importantes e resumidas da documentação que está no arquivo: docAPIProd.html

## Endpoints

### Carros
- **GET /carros**: Retorna todos os carros cadastrados.
- **GET /carros/{carro_id}**: Retorna os dados de um carro específico pelo ID.
- **POST /carros**: Cria um novo carro com os dados fornecidos.
- **PUT /carros/{carro_id}**: Atualiza os dados de um carro específico.
- **DELETE /carros/{carro_id}**: Deleta um carro específico.

### Usuários
- **GET /usuarios**: Retorna todos os usuários cadastrados.
- **GET /usuarios/{usuario_id}**: Retorna os dados de um usuário específico pelo ID.
- **POST /usuarios**: Cria um novo usuário com os dados fornecidos.
- **PUT /usuarios/{usuario_id}**: Atualiza os dados de um usuário específico.
- **DELETE /usuarios/{usuario_id}**: Deleta um usuário específico.

### Autenticação
- **POST /login**: Realiza o login de um usuário com e-mail e senha.

## Exemplos de Respostas

### Carros

- **GET /carros**: Retorna todos os carros cadastrados.
  - **Exemplo de resposta**:
    ```json
    [
      {
        "id": 1,
        "nome": "Fusca",
        "modelo": "Clássico",
        "ano": 1978,
        "preco": 15000.00
      },
      {
        "id": 2,
        "nome": "Civic",
        "modelo": "Ex-L",
        "ano": 2020,
        "preco": 95000.00
      }
    ]
    ```

- **GET /carros/{carro_id}**: Retorna os dados de um carro específico pelo ID.
  - **Exemplo de resposta**:
    ```json
    {
      "id": 1,
      "nome": "Fusca",
      "modelo": "Clássico",
      "ano": 1978,
      "preco": 15000.00
    }
    ```

- **POST /carros**: Cria um novo carro com os dados fornecidos.
  - **Exemplo de corpo da requisição (JSON)**:
    ```json
    {
      "nome": "Gol",
      "modelo": "G6",
      "ano": 2018,
      "preco": 35000.00
    }
    ```
  - **Exemplo de resposta**:
    ```json
    {
      "id": 3,
      "nome": "Gol",
      "modelo": "G6",
      "ano": 2018,
      "preco": 35000.00
    }
    ```

- **PUT /carros/{carro_id}**: Atualiza os dados de um carro específico.
  - **Exemplo de corpo da requisição (JSON)**:
    ```json
    {
      "nome": "Civic",
      "modelo": "Ex-L",
      "ano": 2020,
      "preco": 105000.00
    }
    ```
  - **Exemplo de resposta**:
    ```json
    {
      "id": 2,
      "nome": "Civic",
      "modelo": "Ex-L",
      "ano": 2020,
      "preco": 105000.00
    }
    ```

- **DELETE /carros/{carro_id}**: Deleta um carro específico.
  - **Exemplo de resposta**:
    ```json
    {
      "mensagem": "Carro excluído com sucesso"
    }
    ```

### Usuários

- **GET /usuarios**: Retorna todos os usuários cadastrados.
  - **Exemplo de resposta**:
    ```json
    [
      {
        "id": 1,
        "nome": "Maria Silva",
        "email": "maria@email.com"
      },
      {
        "id": 2,
        "nome": "João Souza",
        "email": "joao@email.com"
      }
    ]
    ```

- **GET /usuarios/{usuario_id}**: Retorna os dados de um usuário específico pelo ID.
  - **Exemplo de resposta**:
    ```json
    {
      "id": 1,
      "nome": "Maria Silva",
      "email": "maria@email.com"
    }
    ```

- **POST /usuarios**: Cria um novo usuário com os dados fornecidos.
  - **Exemplo de corpo da requisição (JSON)**:
    ```json
    {
      "nome": "Pedro Oliveira",
      "email": "pedro@email.com",
      "senha": "senhaSegura123"
    }
    ```
  - **Exemplo de resposta**:
    ```json
    {
      "id": 3,
      "nome": "Pedro Oliveira",
      "email": "pedro@email.com"
    }
    ```

- **PUT /usuarios/{usuario_id}**: Atualiza os dados de um usuário específico.
  - **Exemplo de corpo da requisição (JSON)**:
    ```json
    {
      "nome": "Pedro Oliveira Atualizado",
      "email": "pedroatualizado@email.com",
      "senha": "novaSenha123"
    }
    ```
  - **Exemplo de resposta**:
    ```json
    {
      "id": 3,
      "nome": "Pedro Oliveira Atualizado",
      "email": "pedroatualizado@email.com"
    }
    ```

- **DELETE /usuarios/{usuario_id}**: Deleta um usuário específico.
  - **Exemplo de resposta**:
    ```json
    {
      "mensagem": "Usuário excluído com sucesso"
    }
    ```

### Autenticação

- **POST /login**: Realiza o login de um usuário com e-mail e senha.
  - **Exemplo de corpo da requisição (JSON)**:
    ```json
    {
      "email": "maria@email.com",
      "senha": "senhaSuperSecreta"
    }
    ```
  - **Exemplo de resposta (sucesso)**:
    ```json
    {
      "mensagem": "Login realizado com sucesso"
    }
    ```
  - **Exemplo de resposta (falha)**:
    ```json
    {
      "mensagem": "Email ou senha inválidos"
    }
    ```

## Como Rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/repo.git
