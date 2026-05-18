# Constituição do todo-const

## Princípios Fundamentais

### I. Stack Estritamente Python
O projeto deve ser implementado exclusivamente em Python. Nenhuma outra linguagem de programação é permitida para a lógica principal ou implementação.

### II. Persistência JSON Local
A persistência de dados deve depender exclusivamente de arquivos JSON locais. O uso de bancos de dados SQL ou NoSQL é estritamente proibido.

### III. Qualidade de Código e Padrões
Todo o código Python deve aderir aos padrões PEP 8. O uso de Type Hints é obrigatório. As convenções de nomenclatura devem seguir estritamente snake_case.

### IV. Resiliência e Integridade de I/O
Tratamento de erros robusto deve ser implementado para todas as operações de I/O. A aplicação deve lidar com cenários onde arquivos estão ausentes ou corrompidos sem travar.

### V. UX Centrada no Usuário e Tratamento de Erros
As mensagens voltadas para o usuário devem ser amigáveis e úteis. Detalhes técnicos de erros e stack traces nunca devem ser exibidos ao usuário final.
