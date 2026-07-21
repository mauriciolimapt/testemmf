==========================================================
ATLIN TASK
BACKEND API SPECIFICATION
==========================================================

## Objetivo

Este documento descreve o contrato da API que será consumida
pelo frontend React.

A ideia é permitir que frontend e backend sejam desenvolvidos
independentemente.

==========================================================
TECNOLOGIAS
==========================================================

Frontend

- React
- Vite
- Axios
- Tailwind CSS

Backend

- Python
- FastAPI

Banco de Dados

- Livre escolha da equipe de backend.

==========================================================
PORTAS DURANTE O DESENVOLVIMENTO
==========================================================

Frontend
http://localhost:5173

Backend
http://localhost:8000

Caso outra porta seja utilizada,
avisar para que o frontend seja atualizado.

==========================================================
CORS
==========================================================

O backend deverá permitir requisições vindas de:

http://localhost:5173

==========================================================
SCHEMA DA TASK
==========================================================

Task

id: number
title: string
completed: boolean

Exemplo

{
"id": 1,
"title": "Estudar React",
"completed": false
}

==========================================================
ENDPOINTS
==========================================================

---

## GET /tasks

Descrição

Retorna todas as tarefas.

Resposta

[
{
"id": 1,
"title": "Estudar React",
"completed": false
}
]

---

## POST /tasks

Descrição

Cria uma nova tarefa.

Body

{
"title": "Nova tarefa"
}

Resposta

{
"id": 2,
"title": "Nova tarefa",
"completed": false
}

---

## PUT /tasks/{id}

Descrição

Atualiza uma tarefa existente.

Body

{
"title": "Novo título",
"completed": true
}

Resposta

{
"id": 2,
"title": "Novo título",
"completed": true
}

---

## DELETE /tasks/{id}

Descrição

Remove uma tarefa.

Resposta

{
"message": "Task deleted."
}

==========================================================
STATUS HTTP
==========================================================

200 OK

201 Created

400 Bad Request

404 Not Found

500 Internal Server Error

==========================================================
OBSERVAÇÕES
==========================================================

- O backend deverá seguir exatamente os endpoints
  descritos acima.

- O frontend espera receber JSON em todas as respostas.

- O backend é responsável por gerar o campo "id".

- Toda nova tarefa deverá ser criada com:

  completed = false

- Caso a estrutura da API precise mudar,
  avisar antes para evitar incompatibilidades.
