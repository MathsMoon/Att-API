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
- **Listagem de Carros/Usuários:**
  ```json
  [
    {
      "id": 1,
      "nome": "Nome do Item",
      "modelo": "Modelo",
      "preco": 123.45
    }
  ]