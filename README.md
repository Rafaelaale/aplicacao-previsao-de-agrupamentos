# Grupos de interesse para marketing

Aplicação de aprendizado de máquina que utiliza **K-means** para agrupar usuários por interesses e apoiar a segmentação de campanhas de marketing.

## O que o projeto faz

- Carrega um arquivo CSV enviado pelo usuário.
- Codifica a coluna `sexo` usando o encoder treinado.
- Escala os dados com o scaler treinado.
- Prevê o grupo de cada registro com o modelo K-means.
- Exibe os dez primeiros resultados e permite baixar o CSV completo com a coluna `grupos`.

## Tecnologias

- Python
- Streamlit
- pandas
- scikit-learn
- joblib

## Executar localmente

Use Python 3.11 e, no terminal, a partir da pasta do projeto:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run App.py
```

Abra no navegador o endereço local exibido pelo Streamlit.

## Arquivo de entrada

Envie um arquivo CSV com as colunas usadas durante o treinamento do modelo, incluindo `sexo`. Os nomes, a quantidade e a ordem das demais colunas devem corresponder aos dados usados para treinar `scaler.pkl` e `kmeans.pkl`. A coluna `sexo` deve conter categorias reconhecidas pelo encoder salvo em `encoder.pkl`.

## Artefatos do modelo

O repositório inclui `encoder.pkl`, `scaler.pkl` e `kmeans.pkl`, necessários para transformar os dados e realizar as previsões. O arquivo `grafico_cotovelo.png` registra a análise do método do cotovelo.

## Notebook

`coletando_dados_sem_rotulo.ipynb` documenta o processo de exploração e desenvolvimento da clusterização.

## Observação

Os grupos representam padrões encontrados nos dados de treinamento; não são categorias universais. As descrições dos grupos devem ser interpretadas conforme os dados e os interesses utilizados no treinamento.
