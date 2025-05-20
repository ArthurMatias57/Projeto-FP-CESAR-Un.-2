# Projeto-FP-CESAR-Un.-2

Projeto de simulação de um "sistema de um Pet Shop" com algumas funcionalidades diferenciadas !!

🐾 PetCare - Sistema de Gerenciamento de Pets
PetCare é uma aplicação simples e intuitiva para gerenciamento de informações de pets em um petshop ou ambiente doméstico. Desenvolvida com Python e Tkinter Designer, a aplicação simula funcionalidades essenciais como cadastro de pets, gerenciamento de eventos importantes (vacinação, consultas), definição de metas de saúde, e sugestões personalizadas baseadas na espécie e idade.

🚀 Funcionalidades
📋 CRUD de Pets

Cadastro, visualização, edição e exclusão de pets.

Armazenamento em arquivos .txt.

📅 Registro de Eventos

Marcação de datas para vacinações, consultas veterinárias e outros eventos.

Atualização dinâmica nos dados do pet.

🎯 Metas de Saúde

Defina objetivos como perda de peso, frequência de passeios e alimentação.

Visualize o progresso diretamente no menu.

✨ Sugestões Personalizadas

Geração automática de recomendações com base na idade, espécie e características do pet.

Estrutura hierárquica baseada em árvore para maior precisão.

🧭 Menu Principal (GUI)

Interface gráfica amigável desenvolvida com Tkinter Designer.

Acesso centralizado a todas as funcionalidades.

- Criação de ambiente usando conceitos de árvores:

  - Implementei minha funcionalidade: um algoritmo baseado em estrutura de árvore que gera ambientes ideais para pets a partir dos filtros de características físicas, e raça. Ainda não o terminei, mas já tenho código e BD, vou fazer o debug amn sem falta.


🛠 Estrutura do Projeto
bash
Copiar
Editar
📁 projeto_petshop/
│
├── 📄 MenuPrincipal.py            # Interface principal (Tkinter Designer)
├── 📄 CRUD.py                     # Funções de cadastro, edição e remoção de pets
├── 📄 cadastro_eventos.py        # Registro e atualização de eventos
├── 📄 metas_saude.py             # Sistema de definição e leitura de metas
├── 📄 SugestoesPersonalizadas.py # Algoritmo de recomendações baseado em hierarquia
├── 📁 BD/
│   ├── pets.txt                  # Dados dos pets
│   ├── eventos.txt               # Eventos registrados
│   ├── metas.txt                 # Metas definidas
│   └── recomendacoes.txt         # Estrutura de árvore de recomendações
📌 Todos os dados são armazenados localmente em arquivos .txt.

▶️ Como Executar
Pré-requisitos:

Python 3.8+

Tkinter (já incluso no Python padrão)

Tkinter Designer (para editar o layout, opcional)

Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seuusuario/petcare.git
cd petcare
Execute a aplicação:

bash
Copiar
Editar
python MenuPrincipal.py
📚 Exemplos de Uso
Cadastrar novo pet: Use a opção “Adicionar Pet” no menu e preencha os dados básicos.

Definir meta: Clique em “Metas de Saúde” e insira uma nova meta por pet.

Ver recomendações: Acesse a aba “Sugestões” para dicas de cuidados personalizadas.

🧩 Tecnologias Utilizadas
Python 3

Estrutura de arquivos .txt como banco de dados

Estrutura de árvore para lógica de recomendações

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

📄 Licença
Este projeto está licenciado sob a MIT License.
![Projeto FP - Turma A docx_001](https://github.com/user-attachments/assets/3fb4372b-93ab-4a15-8b0c-6215c3bdc40a)

![Projeto FP - Turma A docx_002](https://github.com/user-attachments/assets/ac8a1f22-77b9-43d8-b7df-fb71f8471dc7)
