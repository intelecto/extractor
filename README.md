# Extractor

Extrair informações de fontes de dados diversas para um arquivo CSV para análise de dados.

[![Build Status](https://travis-ci.org/intelecto/extractor.svg?branch=master)](https://travis-ci.org/intelecto/extractor)

Pré requisitos
-------

  * Instalação da versão do Python >= 3 (http://www.python.org/download)
  
Instalação das dependências
-------

```bash
$ pip install -r requirements.txt
```

Extratores
----------
* extract.py: Extrair nome dos arquivos e nome dos formulários em todos os diretórios de todos os projetos.
* forms.py: Gerar instrução SQL a partir do CSV gerado.
* mysql_table_batch.py: Extrair informações de uma tabela MySQL em batch-mode. 
* mysql_table_line.py: Extrair informações de uma tabela MySQL linha-a-linha.

Executar
-------

```bash
$ python extractor.py
```

Testes unitários
---------

```bash
$ python .\test_extractor.py
..................................
----------------------------------------------------------------------
Ran 34 tests in 0.017s

OK
```
