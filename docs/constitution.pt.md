# Constituição do todo-const

## Princípios Fundamentais

### I. Stack Estritamente Python
O projeto deve ser implementado exclusivamente usando Python. Nenhuma outra linguagem de programação é permitida para a lógica principal ou implementação.
**Justificativa**: Garante um ambiente de desenvolvimento consistente, simplifica o gerenciamento de dependências e alinha-se com a expertise da equipe.

### II. Persistência JSON Local
A persistência de dados deve depender exclusivamente de arquivos JSON locais. O uso de bancos de dados SQL (SQLite, PostgreSQL, etc.) ou NoSQL (MongoDB, Redis, etc.) é estritamente proibido.
**Justificativa**: Prioriza a portabilidade, simplicidade e facilidade de inspeção sem exigir servidores de banco de dados externos ou drivers complexos.

### III. Qualidade de Código e Padrões
Todo o código Python deve aderir aos padrões PEP 8. O uso de Type Hints é obrigatório para todas as assinaturas de funções e APIs públicas. As convenções de nomenclatura devem seguir estritamente snake_case.
**Justificativa**: Mantém alta legibilidade do código, garante a segurança de tipos durante o desenvolvimento e segue as práticas idiomáticas do Python.

### IV. Resiliência e Integridade de I/O
Tratamento de erros robusto deve ser implementado para todas as operações de I/O. A aplicação deve lidar com cenários onde arquivos estão ausentes, corrompidos ou inacessíveis sem travar.
**Justificativa**: Garante a confiabilidade do sistema e evita a perda de dados ou encerramento inesperado em ambientes instáveis.

### V. UX Centrada no Usuário e Tratamento de Erros
As mensagens voltadas para o usuário devem ser amigáveis e úteis. Detalhes técnicos de erros, stack traces e exceções internas nunca devem ser exibidos ao usuário final.
**Justificativa**: Proporciona uma experiência de usuário profissional e evita a exposição de detalhes internos do sistema por segurança e clareza.

## Restrições de Desenvolvimento

### Stack Tecnológico e Conformidade
- **Linguagem Principal**: Python (estritamente)
- **Formato de Dados**: JSON (estritamente)
- **Guia de Estilo**: PEP 8
- **Segurança de Tipos**: Type Hints obrigatórios
- **Nomenclatura**: snake_case para todos os identificadores

## Fluxo de Trabalho de Desenvolvimento

### Portões de Qualidade
1. **Verificação de Linting**: Deve passar na conformidade PEP 8.
2. **Verificação de Tipos**: Deve passar na análise estática de tipos (ex: mypy).
3. **Verificação de Resiliência**: Operações de I/O devem ser envolvidas em blocos try/except apropriados com mensagens de erro amigáveis ao usuário.

## Governança
Esta constituição define os padrões inegociáveis para o todo-const. Emendas exigem documentação e um salto de versão.

### Procedimento de Emenda
1. Propor alterações em uma nova versão da constituição.
2. Atualizar os modelos dependentes (`.specify/templates/*`).
3. Ratificar a nova versão e atualizar a data `LAST_AMENDED_DATE`.

**Versão**: 1.0.0 | **Ratificada**: 2026-05-17 | **Última Alteração**: 2026-05-17
