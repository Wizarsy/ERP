# AIC II - ERP

- [AIC II - ERP](#aic-ii---erp)
  - [Config](#config)
    - [.env](#env)
  - [TODO](#todo)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Insights](#insights)

## Config

### .env

| Variable         | Description |
| ---------------- | ----------- |
| DB_HOST          | -           |
| DB_USER          | -           |
| DB_NAME          | -           |
| DB_PASS          | -           |
| FLASK_DEBUG      | -           |
| FLASK_SECRET_KEY | -           |
| TOKEN_SECRET_KEY | -           |
| SMTP_HOST        | -           |
| SMTP_PORT        | -           |
| EMAIL_ACCOUNT    | -           |
| EMAIL_PASSWORD   | -           |

## TODO

### Backend

- [x] Banco de dados de usuário;
- [x] Cadastro de usuário;
- [x] Login de usuário;
- [x] Confirmação de email;
- [x] Recuperação de senha;
- [x] Autenticação requerida pras rotas;
- [x] Cookies de usuário;
- [ ] Cadastro de item;
- [ ] Cadastro de lista de clientes.

### Frontend

- [ ] Design figma;

## Insights

Mudar pagina de confirmação de email:
pagina para pesquisar email de resetar senha -> volta pra pagina de login com a msg de erro ou envio
ao cadastrar direcionar pra pagina que diz que email de confirmação foi enviado, com a opção de mandar novamente o email.
Se o token falhar apenas retorne pra pagina de login com o erro.
