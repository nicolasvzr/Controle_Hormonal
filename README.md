# 💉 Controle de Aplicação de Hormônios

Este é um sistema web simples, desenvolvido com **Python e Flask**, para registrar e calcular a **próxima aplicação de hormônios**, com base em uma data inicial e um período em dias ou semanas. As informações são salvas em um arquivo `.json`.

## 🚀 Funcionalidades

- Registro do nome do hormônio aplicado.
- Data da aplicação atual.
- Período e tipo de período (dias ou semanas).
- Cálculo automático da próxima aplicação.
- Armazenamento local em JSON.
- Exibição em tabela das aplicações registradas.

## 🤖 IA 

- O front-end foi gerado com o apoio da IA (ChatGPT) para facilitar o desenvolvimento.

## 🛠 Tecnologias Utilizadas

- Python 3.13.2
- Flask
- HTML + CSS
- JSON para armazenamento local

## 📦 Estrutura do Projeto

projeto/
│
├── app.py # Arquivo principal do Flask
├── dados.json # Base de dados local (armazenamento dos dados das aplicações)
├── templates/
│ └── index.html # Interface do sistema (frontend)
├── static/
│ └── style.css # Estilização da aplicação
└── README.md # Documentação do projeto


## 🖥️ Como Rodar o Projeto

1. Clone este repositório:
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    python -m venv venv
    venv\Scripts\activate     # Windows

3. Instale as dependências:
   pip install Flask

4. Execute o aplicativo:
   O codigo ja possui o comando para rodar o app, então só executar o arquivo > app.py
   Caso não tenha o comando, execute o seguinte comando no terminal:
   python app.py

5. Acesse no navegador:
    http://127.0.0.1:5000/

📌 Observações
- Certifique-se de que o arquivo dados.json exista. Caso contrário, o app cria automaticamente.

- Datas devem ser inseridas no formato dd/mm/aaaa.

👤 Autor
Desenvolvido por Nicolas Vaz — sinta-se à vontade para contribuir ou fazer sugestões!
