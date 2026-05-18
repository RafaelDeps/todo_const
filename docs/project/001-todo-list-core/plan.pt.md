# Plano de Implementação: Funcionalidades Core do TODO List

**Branch**: `001-todo-list-core-001` | **Data**: 2026-05-17 | **Spec**: [spec.md](spec.md)

## Resumo
Implementar uma aplicação de lista de tarefas local usando uma arquitetura MVC em Python/Flask. O sistema suporta operações CRUD, um sistema de lembretes baseado em navegador e portabilidade de dados JSON, aderindo estritamente à persistência de arquivos locais e ao tratamento de erros não técnicos.

## Contexto Técnico

**Linguagem/Versão**: Python 3.10+  
**Principais Dependências**: Flask (Controller), Jinja2 (View), Biblioteca padrão `json` (Model)  
**Armazenamento**: Arquivos JSON locais (`tasks.json`)  
**Testes**: pytest  
**Plataforma Alvo**: Linux/macOS/Windows (compatível com Python)
**Tipo de Projeto**: Aplicação Web (MVC / SSR)  
**Metas de Desempenho**: N/A
**Restrições**: PEP 8, Type Hints, resiliência de I/O, UX amigável, Sem JS complexo  
**Escala/Escopo**: Gerenciamento de tarefas local

## Verificação da Constituição

*PORTÃO: Deve passar antes da pesquisa da Fase 0. Re-verificar após o design da Fase 1.*

- [x] **Princípio I (Python)**: Implementação estritamente em Python/Flask.
- [x] **Princípio II (JSON)**: Persistência apenas via arquivos JSON locais.
- [x] **Principle III (Qualidade)**: PEP 8, Type Hints e snake_case obrigatórios.
- [x] **Princípio IV (Resiliência)**: Erros de I/O tratados graciosamente no Model.
- [x] **Princípio V (UX)**: Erros técnicos ocultos da interface Web; mensagens amigáveis utilizadas.

## Estrutura do Projeto

### Documentação (desta funcionalidade)

```text
specs/001-todo-list-core/
├── plan.md              # Este arquivo
├── research.md          # Decisões de implementação
├── data-model.md        # Esquema JSON e definições de entidades
├── quickstart.md        # Configuração de dev e uso
├── contracts/           # Definições de API e Rotas de UI
│   └── api.md
└── tasks.md             # Tarefas de implementação
```

### Código Fonte (raiz do repositório)

```text
src/
├── app.py               # Ponto de entrada da aplicação Flask (Controller)
├── models/
│   └── task.py          # Entidade Task e I/O JSON (Model)
├── templates/           # Arquivos HTML Jinja2 (View)
│   ├── base.html
│   ├── index.html
│   └── import.html
├── static/              # Arquivos CSS
│   └── style.css
└── utils/
    └── helpers.py       # Validação e formatação

tests/
├── unit/                # Testes de Model e validação
├── integration/         # Testes de rotas Flask
└── conftest.py          # Fixtures do Pytest
```

## Rastreamento de Complexidade

| Violação | Por que é necessária | Alternativa mais simples rejeitada porque |
|-----------|------------|-------------------------------------|
| Nenhuma | N/A | N/A |
