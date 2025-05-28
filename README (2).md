
# 🌸 Clusterização no Dataset Iris

Este projeto tem como objetivo aplicar técnicas de **Machine Learning não supervisionado** no clássico dataset **Iris**, utilizando três algoritmos de clusterização:

- 🔵 **K-Means**
- 🟢 **DBSCAN**
- 🟣 **Agglomerative Clustering (Hierárquico)**

O projeto também inclui visualização dos clusters e análise dos agrupamentos por meio de **matriz de confusão**.

## 📂 Sobre o Dataset

O dataset **Iris** é composto por 150 amostras de flores da espécie _Iris_, contendo 4 características:

- Comprimento da Sépala
- Largura da Sépala
- Comprimento da Pétala
- Largura da Pétala

As classes alvo são:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

## 🚀 Tecnologias e Bibliotecas Utilizadas

- Python
- Scikit-learn
- Pandas
- Matplotlib
- Scipy

## 🔧 Algoritmos Aplicados

- **K-Means**  
  Algoritmo baseado na divisão dos dados em clusters esféricos.

- **DBSCAN**  
  Algoritmo baseado em densidade, identificando ruídos e agrupamentos de diferentes formas.

- **Agglomerative Clustering**  
  Método hierárquico que agrupa os dados de maneira sucessiva.

## 📊 Resultados Obtidos

| Algoritmo                | Observações                                                                                           |
|--------------------------|-------------------------------------------------------------------------------------------------------|
| K-Means                  | Agrupou bem, mas classes podem ser embaralhadas.                                                      |
| DBSCAN                   | Identificou bem alguns clusters, porém classifica alguns pontos como ruído dependendo dos parâmetros. |
| Agglomerative Clustering | Bom desempenho visual, agrupa de forma hierárquica.                                                   |

✔️ Também foram geradas **matrizes de confusão** para avaliar como os agrupamentos se relacionam com as classes reais do dataset.

## 🖼️ Visualizações

Foram plotados:

- Gráficos de dispersão dos clusters
- Dendrograma do agrupamento hierárquico

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/danccoelho/iris-clustering.git
```

2. Instale as dependências (se não tiver):

```bash
pip install -r requirements.txt
```

3. Rode o script no Jupyter Notebook ou diretamente no VSCode.

## 📌 Estrutura do Projeto

```
/clusterizacao-iris
├── clusterizacao.ipynb
├── clusterizacao.py
├── README.md
└── .gitignore
```

## 💡 Aprendizados

✔️ Compreensão dos principais algoritmos de clusterização.  
✔️ Análise de agrupamentos e comparação com rótulos reais.  
✔️ Geração de visualizações para melhor interpretação dos clusters.

## 🤝 Contribuição

Sinta-se à vontade para abrir issues, sugerir melhorias ou fazer um fork deste projeto.

## 📬 Contato

Nome: Daniel Campos Coelho
[🔗 Meu LinkedIn](https://www.linkedin.com/in/daniel-coelho-818381293/)  
[🐙 Meu GitHub](https://github.com/danccoelho)
