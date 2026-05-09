# 🏭 Gestão e Monitoramento de Ativos - Sprint 1

Este repositório contém a entrega da Sprint 1 do desafio de desenvolvimento de uma interface funcional para cadastro e visualização de telemetria de motores industriais.

O projeto foi desenvolvido utilizando **Streamlit** e foca em uma arquitetura desacoplada (separando Front-end e manipulação de dados) para facilitar a futura integração com os modelos de Inteligência Artificial e bancos de dados em nuvem.

## 📁 Estrutura do Projeto

```text
desafio_sprint1/
├── backend/
│   └── data_manager.py      # Gerenciamento de dados (simulando banco de dados/API)
├── frontend/
│   ├── main.py              # Tela Inicial (Consulta e Datatable)
│   └── pages/               
│       ├── 1_📋_Cadastro_Tecnico.py  # Formulário de entrada
│       └── 2_📈_Dados_Brutos.py      # Visualização gráfica de sinais
├── data/
│   └── equipamentos.json    # Armazenamento local (mock)
├── requirements.txt         # Dependências do projeto
└── README.md