# Refatoração com Clean Code - Projeto Acadêmico

## 📌 Descrição

Este projeto tem como objetivo refatorar um código legado em Python, aplicando os princípios do Clean Code para torná-lo mais legível, manutenível e eficiente. Trata-se de um trabalho acadêmico desenvolvido na disciplina de Gestão e Qualidade de Software.

## 🎯 Objetivo

* Melhorar a legibilidade e organização do código
* Eliminar repetições e más práticas
* Aplicar princípios SOLID, DRY, KISS e YAGNI
* Modularizar funções e aplicar o padrão de projeto Strategy
* Criar testes unitários para validar a refatoração
* Utilizar Git e GitHub com controle de versão via branches profissionais

## 📁 Estrutura do Projeto

```
clean-code-projeto-a3/
├── legacy/                    # Código legado original (não modificado)
│   └── legacy_order_system.py
├── refactored/               # Código refatorado
│   ├── models/
│   │   ├── user.py          # Gerenciamento de usuários
│   │   ├── product.py       # Gerenciamento de produtos
│   │   ├── order.py         # Gerenciamento de pedidos
│   │   └── customer.py      # Gerenciamento de clientes
│   └── services/
│       └── auth_service.py  # Serviço de autenticação
├── tests/                    # Testes unitários
├── docs/                     # Documentação
│   ├── relatorio/           # Relatório do trabalho
│   └── apresentacao/        # Slides da apresentação
└── README.md
```

## ⚙️ Tecnologias Utilizadas

* Python 3.x
* unittest (para testes)
* Git / GitHub
* Padrão de projeto Strategy
* Princípios SOLID e Clean Code

## 💻 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/victuribdev/clean-code-projeto-a3.git
cd clean-code-projeto-a3
```

2. Execute o código legado:
```bash
python legacy/legacy_order_system.py
```

3. Execute o código refatorado:
```bash
python refactored/models/user.py
```

## 🧪 Testes

Para executar os testes unitários:
```bash
python -m unittest discover tests
```

## 👥 Integrantes do Grupo

* Allan Carreiro Fonseca Prado
* Daniely Teixeira Oliveira Melo
* Gabriel Henrique de Oliveira Ramos
* Graziele dos Santos Rodrigues
* Paulo Victor Ribeiro dos Santos

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. 