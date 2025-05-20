🐾 PetCare - Sistema de Gerenciamento de Pets

PetCare é uma aplicação simples e intuitiva desenvolvida em Python com interface gráfica em Tkinter Designer, ideal para gerenciamento de informações de pets em pet shops ou residências. O sistema oferece funcionalidades como cadastro de pets, registro de eventos (vacinas, consultas), definição de metas de saúde e sugestões personalizadas baseadas na espécie e idade do animal.

🚀 Funcionalidades
📋 CRUD de Pets
Cadastro, visualização, edição e exclusão de pets.

Armazenamento local em arquivos .txt.

📅 Registro de Eventos
Marcação de datas para vacinação, consultas veterinárias e outros eventos relevantes.

Atualização dinâmica dos dados vinculados ao pet.

🎯 Metas de Saúde
Definição de metas individuais (ex.: perda de peso, frequência de passeios, alimentação).

Visualização e acompanhamento do progresso.

✨ Sugestões Personalizadas
Recomendações automáticas com base na idade, espécie e características do pet.

Utiliza uma estrutura hierárquica em árvore para aumentar a precisão das sugestões.

🧠 Ambiente Personalizado com Estrutura em Árvore
Algoritmo em desenvolvimento baseado em árvore de decisão.

Geração de ambientes ideais para o pet a partir de filtros como raça e características físicas.

🛠 Estrutura do Projeto
├── MenuPrincipal.py               # Interface principal 
├── CRUD.py                        # Funções de cadastro, edição e exclusão
├── cadastro_eventos.py           # Registro de eventos (vacinas, consultas)
├── metas_saude.py                # Definição e visualização de metas
├── SugestoesPersonalizadas.py    # Algoritmo de recomendações
│
└── BD/
    ├── pets.txt                  # Dados dos pets
    ├── eventos.txt              # Eventos registrados
    ├── metas.txt                # Metas definidas
    └── recomendacoes.txt        # Estrutura em árvore com as recomendações

📚 Exemplos de Uso
Cadastrar um novo pet: Acesse a opção “Adicionar Pet” e preencha os dados.

Registrar evento: Vá para a aba de eventos e adicione vacinações ou consultas.

Definir metas de saúde: Insira objetivos personalizados para cada pet.

Ver sugestões: Consulte dicas de cuidados personalizadas com base nas informações cadastradas.

🧩 Tecnologias Utilizadas
Python 3

Tkinter (interface gráfica)

Estrutura de arquivos .txt como banco de dados local

Algoritmo com estrutura de árvore para lógica de recomendações

Navegação centralizada entre as funcionalidades.
![Projeto FP - Turma A docx_001](https://github.com/user-attachments/assets/3fb4372b-93ab-4a15-8b0c-6215c3bdc40a)

![Projeto FP - Turma A docx_002](https://github.com/user-attachments/assets/ac8a1f22-77b9-43d8-b7df-fb71f8471dc7)
