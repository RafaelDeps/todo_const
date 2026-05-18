---

description: "Lista de tarefas para a implementação das Funcionalidades Core do TODO List"
---

# Tarefas: Funcionalidades Core do TODO List

**Entrada**: Documentos de design de `/specs/001-todo-list-core/`
**Pré-requisitos**: plan.md (obrigatório), spec.md (obrigatório), research.md, data-model.md, contracts/

**Testes**: Abordagem TDD solicitada. Testes são obrigatórios para cada área funcional.

**Organização**: As tarefas são agrupadas por história de usuário para permitir a implementação e os testes independentes de cada história.

## Formato: `[ID] [P?] [Story] Descrição`

- **[P]**: Pode rodar em paralelo (arquivos diferentes, sem dependências)
- **[Story]**: A qual história de usuário esta tarefa pertence (ex: US1, US2, US3)

---

## Fase 1: Configuração (Infraestrutura Compartilhada)

**Propósito**: Inicialização do projeto e estrutura básica

- [x] T001 Criar estrutura do projeto (src/, tests/, templates/, static/, utils/) conforme o plano de implementação
- [x] T002 Inicializar projeto Python (venv, requirements.txt com Flask, pytest, mypy, flake8)
- [x] T003 [P] Configurar Flake8/Black e Mypy para aplicação de PEP 8 e Type Hints
- [x] T004 [P] Configurar pytest em tests/conftest.py com fixture da app Flask

---

## Fase 2: Fundamental (Pré-requisitos Bloqueadores)

**Propósito**: Infraestrutura core que DEVE estar completa antes que QUALQUER história de usuário possa ser implementada

**⚠️ CRÍTICO**: Nenhum trabalho de história de usuário pode começar até que esta fase esteja concluída

- [x] T005 [P] Criar layout CSS base em src/static/style.css
- [x] T006 [P] Criar template Jinja2 base em src/templates/base.html
- [x] T007 [P] Implementar utilitários auxiliares em src/utils/helpers.py (geração de UUID, formatação ISO)
- [x] T008 [P] Escrever testes unitários para resiliência de I/O JSON em tests/unit/test_task_model.py
- [x] T009 Implementar Model de Tarefa com I/O JSON atômico e Resiliência em src/models/task.py (depende de T008)
- [x] T010 [P] Configurar tratamento de erros centralizado (mensagens flashed) em src/app.py

**Ponto de Verificação**: Fundação pronta - a implementação das histórias de usuário pode agora começar em paralelo

---

## Fase 3: História de Usuário 1 - Gerenciamento de Tarefas (Prioridade: P1) 🎯 MVP

**Objetivo**: Operações CRUD para tarefas (Título/Descrição/Status)

**Teste Independente**: Criar, Visualizar, Atualizar, Excluir uma tarefa através da interface Web e verificar o armazenamento JSON.

### Testes para a História de Usuário 1 (TDD)

- [x] T011 [P] [US1] Escrever testes unitários para validação da entidade Task em tests/unit/test_task_model.py
- [x] T012 [P] [US1] Escrever testes de integração para rotas CRUD (/, /tasks/add, /update, /toggle, /delete) em tests/integration/test_crud.py

### Implementação para a História de Usuário 1

- [x] T013 [P] [US1] Aprimorar o model Task com campos de validação e status em src/models/task.py
- [x] T014 [US1] Implementar rota do Painel Principal (GET /) em src/app.py
- [x] T015 [US1] Criar template Index com lista de tarefas e formulário de adição em src/templates/index.html
- [x] T016 [US1] Implementar rota de Criar tarefa (POST /tasks/add) em src/app.py
- [x] T017 [US1] Implementar rota de Alternar status (POST /tasks/<id>/toggle) em src/app.py
- [x] T018 [US1] Implementar rota de Atualizar tarefa (POST /tasks/<id>/update) em src/app.py
- [x] T019 [US1] Implementar rota de Excluir tarefa (POST /tasks/<id>/delete) em src/app.py

**Ponto de Verificação**: Neste ponto, a História de Usuário 1 está totalmente funcional e testável de forma independente

---

## Fase 4: História de Usuário 2 - Lembretes de Tarefa (Prioridade: P2)

**Objetivo**: Sistema de lembretes por data/hora

**Teste Independente**: Definir um lembrete para uma tarefa e verificar se ele é exibido e aciona uma notificação visual na interface Web.

### Testes para a História de Usuário 2 (TDD)

- [x] T020 [P] [US2] Escrever testes unitários para validação de data de lembrete em tests/unit/test_task_model.py
- [x] T021 [P] [US2] Escrever testes de integração para exibição de lembretes em tests/integration/test_reminders.py

### Implementação para a História de Usuário 2

- [x] T022 [P] [US2] Atualizar model Task para lidar com o campo reminder_at em src/models/task.py
- [x] T023 [US2] Atualizar template Index para mostrar campos de lembrete e exibição em src/templates/index.html
- [x] T024 [US2] Atualizar rotas de Criar/Atualizar em src/app.py para lidar com reminder_at
- [x] T025 [US2] Implementar lógica de notificação visual In-App (JavaScript) em src/templates/base.html

**Ponto de Verificação**: Neste ponto, as Histórias de Usuário 1 E 2 estão funcionais de forma independente

---

## Fase 5: História de Usuário 3 - Importação/Exportação de Dados (Prioridade: P3)

**Objetivo**: Importar/Exportar tarefas de/para arquivos JSON

**Teste Independente**: Exportar tarefas para um arquivo, limpar os dados e importar o arquivo de volta escolhendo "Substituir" ou "Mesclagem Inteligente".

### Testes para a História de Usuário 3 (TDD)

- [x] T026 [P] [US3] Escrever testes unitários para a lógica de Mesclagem Inteligente em tests/unit/test_task_model.py
- [x] T027 [P] [US3] Escrever testes de integração para rotas de Exportação/Importação em tests/integration/test_portability.py

### Implementação para a História de Usuário 3

- [x] T028 [P] [US3] Implementar lógica de Mesclagem Inteligente e Exportação no src/models/task.py
- [x] T029 [US3] Implementar rota de Exportação (GET /export) em src/app.py
- [x] T030 [US3] Criar template de Importação com upload de arquivo e seleção de modo em src/templates/import.html
- [x] T031 [US3] Implementar rota de Importação (POST /import) em src/app.py

**Ponto de Verificação**: Todas as histórias de usuário estão agora funcionalmente independentes

---

## Fase N: Polimento e Preocupações Transversais

**Propósito**: Refinamentos finais e verificações de qualidade

- [x] T032 [P] Linting PEP 8 final e validação de Type Hints em todos os arquivos
- [x] T033 [P] Atualizar quickstart.md com exemplos de uso finais
- [x] T034 Rodar suíte completa de testes (pytest) para garantir que não haja regressões
- [x] T035 Verificar tratamento de erros amigável para todos os cenários de falha de I/O

---

## Dependências e Ordem de Execução

### Dependências de Fase

- **Configuração (Fase 1)**: Sem dependências - pode começar imediatamente
- **Fundamental (Fase 2)**: Depende da conclusão da Configuração - BLOQUEIA todas as histórias de usuário
- **Histórias de Usuário (Fase 3+)**: Todas dependem da conclusão da fase Fundamental
  - US1 (CRUD) é a base para US2 e US3
  - US2 (Lembretes) e US3 (Portabilidade) podem rodar em paralelo uma vez que a US1 esteja estável

### Dependências de História de Usuário

- **História de Usuário 1 (P1)**: Fundação para as outras histórias.
- **História de Usuário 2 (P2)**: Estende os models e views da US1.
- **História de Usuário 3 (P3)**: Opera nos models estabelecidos na US1.

### Dentro de cada História de Usuário (Estilo TDD)

1. Escrever testes PRIMEIRO e garantir que falhem.
2. Implementar a lógica de model/serviço.
3. Implementar a lógica de controller/rota.
4. Implementar a lógica de UI/template.
5. Verificar se os testes passam.

---

## Exemplos de Execução Paralela

### Configuração e Fundação Paralelas

```bash
# Desenvolvedor A: Configuração e Linting
Tarefa: "T002 Inicializar projeto Python"
Tarefa: "T003 Configurar Flake8/Black e Mypy"

# Desenvolvedor B: Infraestrutura
Tarefa: "T005 Criar layout CSS base"
Tarefa: "T006 Criar template Jinja2 base"
```

### Model e View Paralelos (Fundamental)

```bash
# Execução paralela dentro da Fase 2:
Tarefa: "T008 Escrever testes unitários para resiliência de I/O JSON" -> "T009 Implementar Model de Tarefa"
Tarefa: "T007 Implementar utilitários auxiliares"
Tarefa: "T010 Configurar tratamento de erros centralizado"
```

---

## Estratégia de Implementação

### MVP Primeiro (Apenas História de Usuário 1)

1. Concluir Fase 1: Configuração
2. Concluir Fase 2: Fundamental (CRÍTICO)
3. Concluir Fase 3: História de Usuário 1 (CRUD)
4. **PARAR e VALIDAR**: Testar o CRUD independentemente via interface Web.

### Entrega Incremental

1. Fundação pronta.
2. Adicionar CRUD (MVP).
3. Adicionar Lembretes.
4. Adicionar Importação/Exportação.
5. Cada história é entregue com seus próprios testes.

---

## Notas

- TDD é rigorosamente aplicado: Testes (T008, T011, T012, T020, T021, T026, T027) DEVEM ser feitos antes da implementação.
- Marcadores [P] indicam tarefas sem dependências bloqueadoras dentro de sua fase.
- Os caminhos de arquivos são específicos para a estrutura de projeto solicitada.
- Os princípios de resiliência e UX (da Constituição) estão incorporados nas tarefas fundamentais e de histórias.
