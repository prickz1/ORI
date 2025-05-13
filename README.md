# Gerador de Índice Invertido e Modelo Booleano para Recuperação da Informação

## 📚 Descrição

Este projeto foi desenvolvido como parte do **primeiro trabalho prático da disciplina de Organização e Recuperação da Informação (ORI)** do curso de Sistemas de Informação da Universidade Federal de Uberlândia (UFU), sob orientação do professor **Wendel Melo**.

O programa implementa:

1. Um **gerador de índice invertido** a partir de uma base de documentos de texto.
2. Um **sistema de recuperação de informação baseado no modelo booleano**, utilizando operações lógicas `AND`, `OR` e `NOT` sobre os termos lematizados dos documentos.

## 🧠 Objetivo

Permitir a **busca eficiente de documentos relevantes** com base em consultas booleanas realizadas sobre um índice invertido previamente construído. O sistema trata automaticamente:

- Leitura de documentos da base.
- Tokenização, lematização e remoção de stopwords (usando SpaCy).
- Geração do índice invertido.
- Processamento de consultas booleanas.
- Escrita dos arquivos de saída com os resultados da consulta.

---

## 🔧 Tecnologias Utilizadas

- **Python 3**
- **[SpaCy](https://spacy.io/)** (`pt_core_news_lg`): para lematização e remoção de stopwords (obrigatório).
- Leitura e escrita de arquivos de texto (`open`, `read`, `write`).
- Manipulação de estruturas de dados básicas: listas, dicionários e conjuntos.

> ❗ **Importante**: conforme as regras do trabalho, **não foi utilizada a biblioteca `nltk`**, sendo a única biblioteca externa permitida o `SpaCy`.

---

## 📁 Entradas do Programa

O programa recebe dois arquivos como argumentos da linha de comando:

```bash
python modelo_booleano.py base.txt consulta.txt
```

- `base.txt`: contém os caminhos para os arquivos de texto da base de documentos, um por linha.
- `consulta.txt`: contém uma ou mais consultas booleanas, uma por linha, no seguinte formato:

### Exemplo de consulta:
```
casa & amor | casa & !mora
```

Operadores válidos:
- `&` ou `AND`: interseção (documentos que contêm ambos os termos).
- `|` ou `OR`: união (documentos que contêm pelo menos um dos termos).
- `!` ou `NOT`: negação (documentos que **não** contêm o termo).

---

## 📤 Saídas do Programa

O programa gera dois arquivos de saída:

### 1. `indice.txt`
Contém o índice invertido, com os termos lematizados e, para cada termo, os documentos em que ele aparece e sua frequência.

#### Exemplo:
```
amor: 3,1
casa: 1,1 2,4 3,1
casar: 3,2
```

Onde os números representam:
- `3,1`: o termo aparece no documento 3, uma vez.
- A numeração dos documentos segue a ordem em que aparecem no `base.txt`.

---

### 2. `resposta.txt`
Contém os resultados das consultas, listando os documentos que satisfazem cada uma, conforme o modelo booleano.

#### Exemplo:
```
2
b.txt
c.txt
```

- A primeira linha indica o número de documentos que satisfazem a consulta.
- As linhas seguintes listam os nomes dos arquivos correspondentes.

---

## 🧪 Testes

Para testar o código, utilize o **corretor automático** disponibilizado pelo professor, seguindo as instruções da disciplina. Certifique-se de que os arquivos `indice.txt` e `resposta.txt` sejam gerados exatamente com os nomes e formatos especificados.

---

## 📌 Observações Importantes

- O conteúdo dos documentos é lematizado e convertido para minúsculas.
- Stopwords são removidas com base no modelo do `SpaCy`.
- Após a criação do índice invertido, **o conteúdo original dos documentos não é mais acessado**, conforme exigido.
- O operador `NOT` tem **maior precedência** que `AND`, que por sua vez tem **maior precedência** que `OR`.

---

## 👤 Autor

**Paulo Henrique**  
Aluno Sistemas de Informação - UFU 
