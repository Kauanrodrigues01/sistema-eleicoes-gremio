# Sistema de Votação para Eleições do Grêmio Estudantil - EEEP Adolfo Ferreira de Sousa

![Dashboard do Sistema de Votação](https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/projetos/sistema-eleicoes-gremio/foto-dashboard-eleicoes-gremio.png)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

Sistema desenvolvido para gerenciar o processo eleitoral do Grêmio Estudantil da Escola EEEP Adolfo Ferreira de Sousa, proporcionando uma solução digital para cadastro de chapas, votação e apuração de resultados.

## Funcionalidades Principais

### 🗳️ Sistema de Votação
- Registro seguro de votos dos alunos
- Controle de turmas participantes
- Impedimento de votos duplicados

### 📊 Dashboard de Resultados
- Visualização dos resultados
- Gráficos interativos com Chart.js
- Dados detalhados por turma e geral

### 👥 CRUD de Chapas
- Cadastro de chapas candidatas
- Edição de informações
- Remoção de chapas

## Tecnologias Utilizadas

- **Backend**: Django (Python)
- **Frontend**: Bootstrap 5 + HTML/CSS/JS
- **Banco de Dados**: PostgreSQL
- **Visualização de Dados**: Chart.js
- **Containerização**: Docker

## Dados do Dashboard

📈 **Visão Geral:**
- Total de votos apurados
- Número de salas participantes
- Quantidade de chapas inscritas
- Ranking das chapas com porcentagem de votos

🏫 **Por Turma:**
- Distribuição de votos por chapa
- Taxa de participação da turma
- Total de votos da turma
- Gráfico de barras comparativo

## Pré-requisitos

- Docker e Docker Compose instalados

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-votacao-gremio.git
cd sistema-votacao-gremio
```

2. Configure as variáveis de ambiente no arquivo .env:
```text
DEBUG=True
SECRET_KEY='django-insecure-$9x8$8!yw9(*ml_r@-39_5d*ft=#w8x$j_=@zf%5e8db4ghp#r'
ALLOWED_HOSTS=*
LANGUAGE_CODE='pt-br'
TIME_ZONE='America/Sao_Paulo'

# DATABASE_URL=postgresql://admin:secret@localhost:5432/meudb2

ADMIN_USERNAME=dev
ADMIN_PASSWORD=1234
```

3. Inicie os containers com Docker:
```bash
docker-compose up -d
```

3. Acesse a aplicação:
```
http://localhost:8000
```

---

#### Desenvolvido para a EEEP Adolfo Ferreira de Sousa - © 2025

<br>
<br>
