# desafio_workshop_backend_2023_2

## Passo a Passo de como executar:

1 - Clonar o Repositorio:
```bash
git clone https://github.com/MiguellArcanjo/desafio_workshop_backend_2023_2.git
```

2 - Criar um ambiente virtual no repositorio clonado 
> No ambiente Windows
```ps1
python -m venv venv
.\venv\Scripts\activate.ps1
```

> No ambiente Linux
```bash
python -m venv venv
source venv/bin/activate
```

3 - Baixando os pacotes do projeto
```bash
pip install -r requirements.txt
```

4 - Rodar o servidor 
```bash
python manage.py runserver
```

## Acessando as rotas do produto

**(GET)** 

**rota_api/produto/produto** : Retorna todos os dados da API 

**rota_api/produto/produto/id** : Retorna um dado específico da API pelo *ID*

**(POST)**
> Enviando novos dados para a API
```json

    {
    "nome": "",
    "descricao": "",
    "quantidade": 1,
    "preco": 1.5,
    "categoria_produto": choice,
    "marca_do_produto": choice,
    }

```

**(PUT)**
> Atualizando dados da API: *rota_api/produto/produto/id*
```json

    {
    "nome": "Iphone XS",
    "descricao": "Iphone com 4gb de ram ",
    "quantidade": 5,
    "preco": 1999.99,
    "categoria_produto": "Eletronico", **O NOME DA CATEGORIA APARECE NAS OPÇÕES DE ESCOLHA APÓS INSERIR NA ROTA DE CATEGORIAS**
    "marca_do_produto": "Apple",
    }

```

**(DELETE)**
> Deletando um dado específico da API: *rota_api/produto/produto/id*


## Acessando as rotas da Categoria do Produto

**(GET)**

**rota_api/produto/categoria** : Retorna todos os dados da API 

**rota_api/produto/categoria/id** : Retorna um dado específico da API pelo *ID*

**(POST)**
> Enviando um novo dado para a API
```json

    {
    "categoria": "",
    }

```

**(PUT)**
> Atualizando o dado da API: *rota_api/produto/categoria/id*
```json

    {
    "categoria": "Eletronico",
    }

```

**(DELETE)**
> Deletando um dado específico da API: *rota_api/produto/produto/id*

## Acessando as rotas da Marca do Produto

**(GET)**

**rota_api/produto/marca** : Retorna todos os dados da API 

**rota_api/produto/marca/id** : Retorna um dado específico da API pelo *ID*

**(POST)**
> Enviando um novo dado para a API
```json

    {
    "marca": "",
    }

```

**(PUT)**
> Atualizando o dado da API: *rota_api/produto/marca/id*
```json

    {
    "marca": "Apple",
    }

```

**(DELETE)**
> Deletando um dado específico da API: *rota_api/produto/produto/id*