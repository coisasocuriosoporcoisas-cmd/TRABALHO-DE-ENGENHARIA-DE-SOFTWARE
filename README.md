# TRABALHO-DE-ENGENHARIA-DE-SOFTWARE
UM APP DE CADASTRAMENTO USANDO A LINGUAGEM PYTHON.

## Escopo do Projeto

O app se tratar de uma aplicação voltada para o cadastramento de usuários em um sistema genérico de empressa, para o nosso projeto, um sistema de pedido.

## Estrutura 
- Admin será o responsável por cadatra as pessoas , os atributos de cada pessoa será divido conforme a tabela a seguir:

|Atributos|Descrição|
|---|---|
|_id| identificador de cada pessoa, ele será aramazenado de forma crescente, a medida que sendo cadatrado as pessoa vai se somando +1, eo "_id" será visivel internamente, neste projeto ele ficará visível apenas no arquivo Json|
|cpf| O Cpf, será o idetificador visível da pessoa na interface, ELE É UNICO!|
|Nome| A nomeclatura da pessoa, ambas as pessoas podem possuí o mesmo nome, ele servirá como uma alternativa para a barra de pesquisa|
|telefone|uma forma de contata a pessoa cadastrada|
|email|uma forma secudária de contata a pessoa cadastrada|
|pedido|Não solicitado no documento, uma implementação, que possui o valor Bool (True or False)|

## Ferramentas usadas 
A aplicação será desenvolvida em Python,o cadastro será de maneira simples juntamente com sua interface que támebem será realizada em Python, pela Biblioteca **customtkinter**, a opção atual em python mais moderna para o desenvolvimento de interfaces python, para o salvamento dos cadastro será usado **NSQL**, sendo que as informações adiquerida serão salvas em arquivos  Json.
