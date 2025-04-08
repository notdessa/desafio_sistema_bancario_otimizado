 # desafio_sistema_bancario_otimizado
Código do sistema bancário otimizado feito conforme instruções do desafio.

## Melhorias implementadas

1. **Separação em funções** 
Criado funções para todas as operações do sistema.

2. **Saque**
A função saque com os argumentos apenas por nome (keyword only). 

3. **Depósito**

A função depósito recebe os argumentos apenas por posição (positional only). 
4. **Novas Funções**
Criadas duas novas funções: criar usuário e criar conta corrente. 

5. **Criar Usuário (cliente)** 

O programa armazena os usuários em uma lista. 
O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. 
Impossibilitado cadastro de 2 usuários com o mesmo CPF.

6. **Criar conta corrente**
O programa armazena contas em uma lista. 
O número da conta sequencial, iniciando em 1. 
O número da agência é fixo: "0001". 
O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

## Melhorias adicionais

1. Interface visual com .center(40)
2. Melhora a legibilidade no terminal.
3. Validação da data de nascimento com datetime.strptime().
4. Busca eficiente de usuário com next() e expressão geradora.
5. Exibição formatada de contas com print("="*40) e f-strings.
6. Variáveis globais com nomes claros e significativos.
7. Mensagens de erro e feedback informativos ao usuário.
