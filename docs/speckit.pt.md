# Desenvolvimento Orientado a Especificações (SpecKit)

Este projeto utiliza o **SpecKit**, uma metodologia de desenvolvimento orientada a especificações (*Specification-Driven Development* - SDD) que exige planejamento detalhado, conformidade com uma "constituição" de regras de design do projeto e acompanhamento de tarefas (incluindo TDD) antes do início da escrita de código.

## Configuração e Estrutura do SpecKit

A automação e os metadados do SpecKit estão organizados nos seguintes componentes no repositório:

*   **Configurações do SpecKit:**
    *   `.specify/init-options.json`: Configura opções globais, incluindo a integração com a IA (`gemini`), numeração sequencial de branches e o arquivo de contexto principal (`GEMINI.md`).
    *   `.specify/feature.json`: Registra o diretório da feature ativa (`specs/001-todo-list-core`).
*   **Constituição do Projeto:**
    *   `.specify/memory/constitution.md` (publicado em [Constituição do Projeto](constitution.pt.md)): Estabelece os **5 princípios inegociáveis** que servem como portões de qualidade para qualquer alteração no código:
        1. **Strictly Python Stack**: Uso exclusivo de Python/Flask para a lógica principal.
        2. **Local JSON Persistence**: Persistência estritamente em arquivos JSON locais, proibindo bancos SQL/NoSQL.
        3. **Code Quality & Standards**: Adesão estrita ao PEP 8, Type Hints obrigatórios e nomenclatura snake_case.
        4. **Resilience & I/O Integrity**: Tratamento robusto de erros de I/O para evitar falhas críticas.
        5. **User-Centric UX & Error Handling**: Esconder stack traces/erros técnicos e exibir mensagens amigáveis.
*   **Workflow e Automação de Git:**
    *   `.specify/extensions.yml`: Configura ganchos (hooks) de Git para automação de branches de features (`speckit.git.feature`) e auto-commits (`speckit.git.commit`) antes/depois de cada etapa.
    *   `.specify/workflows/speckit/workflow.yml`: Define a esteira completa do ciclo de desenvolvimento (Full SDD Cycle).
    *   `.gemini/commands/`: Contém comandos TOML customizados que definem as instruções passo a passo para a IA em cada fase do ciclo (por exemplo, `speckit.specify.toml`, `speckit.plan.toml`, `speckit.tasks.toml` e `speckit.implement.toml`).

---

## Ciclo de Desenvolvimento e Prompts Registrados

O ciclo de desenvolvimento da feature principal `001-todo-list-core` seguiu rigorosamente os passos e prompts abaixo:

### 1. Especificação (`speckit.specify`)
*   **Prompt de Entrada:** 
    > "Crie a especificação para um TODO List com: 1. CRUD de tarefas (Título/Descrição). 2. Sistema de lembretes por data/hora. 3. Função de Importar/Exportar dados."
*   **Resultado:** Gerou a especificação em [Especificação da Feature](project/001-todo-list-core/spec.pt.md), detalhando histórias de usuário (US1, US2, US3) com critérios de aceitação estruturados no formato **Given / When / Then**, casos de borda e requisitos funcionais.
*   **Qualidade:** O checklist em `specs/001-todo-list-core/checklists/requirements.md` foi utilizado para validar a qualidade e completude dos requisitos antes de prosseguir.

### 2. Planejamento (`speckit.plan`)
*   **Entrada:** A especificação gerada anteriormente.
*   **Resultado:** Gerou o plano em [Plano de Implementação](project/001-todo-list-core/plan.pt.md), estruturando a arquitetura técnica (MVC), a árvore de arquivos do projeto (`src/` e `tests/`) e os portões de conformidade constitucional.
*   **Detalhes adicionais:**
    *   `specs/001-todo-list-core/research.md`: Registrou as decisões técnicas do projeto (como escrita atômica para integridade de dados).
    *   `specs/001-todo-list-core/contracts/api.md`: Documentou os contratos formais das rotas web/SSR e o esquema JSON de persistência/exportação.

### 3. Tarefas (`speckit.tasks`)
*   **Entrada:** Os documentos de design de `specs/001-todo-list-core/`.
*   **Resultado:** Gerou a lista em [Tarefas de Implementação](project/001-todo-list-core/tasks.pt.md), rastreando as etapas de setup, infraestrutura básica, CRUD, lembretes e importação/exportação no formato `[ID] [P?] [Story] Descrição`.

### 4. Implementação (`speckit.implement`)
*   **Entrada:** A especificação, o plano e as tarefas geradas anteriormente.
*   **Aplicação de TDD:** Conforme exigido no arquivo de tarefas, testes de unidade e integração (ex: em `tests/unit/test_task_model.py` e `tests/integration/test_crud.py`) foram obrigatoriamente escritos e validados (falhando) antes do desenvolvimento da lógica correspondente nos controllers/models.
