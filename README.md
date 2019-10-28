# Mineração Interativa de Repositórios Visando a Melhoria Contínua de Processos

Minicurso apresentado no dia 28/10/2019 no [SBQS](http://sbqs.sbc.org.br/index.php/pt/programacao/minicurso2) - 09:00h - 15:45h.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JoaoFelipe/minicurso-mineracao-interativa)


## Descrição

> O mini-curso tem o objetivo de apresentar mineração interativa de repositórios com o objetivo de melhoria continua de processos. O mini-curso abordará 4 tópicos: interatividade, coleta de dados, análise e visualização. Para interatividade, será apresentada a ferramenta Jupyter Notebook, indicando como ela pode ser usada para tarefas exploratórias e para a construção de dashboards. Para a coleta de dados, será usada a API do GitHub para obter issues de um repositório e a biblioteca PyGit2 para navegar no histórico. Para análise dos dados, será usada a biblioteca pandas. Por fim, para a visualização dos dados, será usada a biblioteca Matplotlib. O mini-curso será guiado por tarefas tais como observar a densidade de defeitos do projeto com o passar do tempo, descobrir quem são os desenvolvedores que mais contibuíram com o projeto no decorrer do tempo, ~~medir a cobertura de testes ao longo do tempo~~, etc.

A parte de cobertura de testes ficou de fora.

## Organização

Os arquivos principais da apresentação são Jupyter Notebooks na raiz do projeto:

- [1.Introducao.ipynb](1.Introducao.ipynb)
- [2.Jupyter.ipynb](2.Jupyter.ipynb)
- [3.IPython.ipynb](3.IPython.ipynb)
- [4.Proxy.ipynb](4.Proxy.ipynb)
- [5.Crawling.ipynb](5.Crawling.ipynb)
- [6.API.v3.ipynb](6.API.v3.ipynb)
- [7.API.v4.ipynb](7.API.v4.ipynb)
- [8.Git.ipynb](8.Git.ipynb)
- [9.Pygit2.ipynb](9.Pygit2.ipynb)
- [10.Visualizacao.Rica.ipynb](10.Visualizacao.Rica.ipynb)
- [11.Widgets.ipynb](11.Widgets.ipynb)

Esses arquivos não estão com resultados das execuções pois serão executados durante o minicurso. Existem versões deles executadas no diretório [resultados](resultados). Além disso, existem versões extraídas em PDF no diretório [pdf](pdf).

## Execução

A forma mais simples de executar os notebooks é abrindo no Gitpod. Clique no seguinte botão para iniciar o Gitpod.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JoaoFelipe/minicurso-mineracao-interativa)

Após a inicialização, digite o seguinte no terminal para iniciar o Jupyter:
```bash
jupyter notebook --NotebookApp.allow_origin=\'$(gp url 8888)\' --ip='*' --NotebookApp.token='' --NotebookApp.password=''
```

## Instalação

Se não quiser usar o Gitpod, é possível instalar as dependências para executar localmente. As dependências de programas são:

```
Python 3.7
cloc 1.74
GraphViz 2.40.1
```

As dependências de bibliotecas do Python são:

```
beautifulsoup4==4.8.1
Flask==1.1.1
ipython==7.8.0
ipywidgets==7.5.1
jupyter==1.0.0
matplotlib==3.1.1
numpy==1.17.2
pandas==0.25.2
pygit2==0.28.2
python-dateutil==2.8.0
radon==4.0.0
requests==2.22.0
simplejson==3.16.0
```

Apesar das versões terem sido especificadas desta forma, versões próximas devem funcionar também.

### Ubuntu + Anaconda

Se você usa Ubuntu e Anaconda, a instalação pode ser feita com os seguintes comandos (assumindo um ambiente completo do Anaconda):

```bash
sudo apt-get install cloc graphviz
pip install simplejson radon
conda install -c conda-forge pygit2
```

## Autor

João Felipe Pimentel - Universidade Federal Fluminense