import spacy
import sys

nlp = spacy.load("pt_core_news_lg")




def abrirArq(base_file):
    listas_termos = []
    nomes_arquivos = []
    
    with open(base_file, "r", encoding='utf-8') as base:
        for linha in base:
            caminho_arquivo = linha.strip()
            if caminho_arquivo:
                nomes_arquivos.append(caminho_arquivo)
    
    def processar_arquivo(caminho):
        with open(caminho, "r", encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            doc = nlp(conteudo)
            
            tokens_sem_stopwords = [
                token.lemma_.lower() for token in doc  
                if not token.is_stop and not token.is_punct and not token.is_space and ' ' not in token.lemma_
            ]
            return tokens_sem_stopwords

    for nome in nomes_arquivos:
        termos = processar_arquivo(nome)
        listas_termos.append(termos)

    return listas_termos, nomes_arquivos






def contar_ocorrencias(listas_termos, nomes_arquivos):
    indice_invertido = {}

    for i, termos in enumerate(listas_termos):
        arquivo_id = i + 1
        contagem = {}

        for termo in termos:
            if termo in contagem:
                contagem[termo] += 1
            else:
                contagem[termo] = 1

        for termo, freq in contagem.items():
            if termo not in indice_invertido:
                indice_invertido[termo] = {}
            indice_invertido[termo][arquivo_id] = freq

    return indice_invertido






def salvar_indice(indice_invertido):
    termos_ordenados = sorted(indice_invertido.keys())
    
    with open("indice.txt", "w", encoding='utf-8') as f:
        for termo in termos_ordenados:
            ocorrencias = " ".join([f"{arquivo},{freq}" for arquivo, freq in indice_invertido[termo].items()])
            f.write(f"{termo}: {ocorrencias}\n")






def realizar_consulta(consulta, indice_invertido, nomes_arquivos):
    consulta = consulta.replace("&", "AND").replace("|", "OR").replace("!", "NOT ")
    partes = consulta.split(" OR ")
    
    arquivos_finais = set()
    
    for parte in partes:
        arquivos_permitidos = set()
        arquivos_proibidos = set()
        subpartes = parte.split(" AND ")

        for subparte in subpartes:
            if 'NOT' in subparte:
                arquivos_permitidos = set(range(1, len(nomes_arquivos) + 1))
                palavra = subparte.replace('NOT ', '').strip().lower()
                if palavra in indice_invertido:
                    arquivos_proibidos.update(indice_invertido[palavra].keys())
            else:
                palavra = subparte.strip().lower()
                if palavra in indice_invertido:
                    arquivos_temp = set(indice_invertido[palavra].keys())
                    if not arquivos_permitidos:
                        arquivos_permitidos = arquivos_temp
                    else:
                        arquivos_permitidos.intersection_update(arquivos_temp)

        arquivos_permitidos.difference_update(arquivos_proibidos)
        arquivos_finais.update(arquivos_permitidos)

    return [nomes_arquivos[i - 1] for i in sorted(arquivos_finais)]






def main():
    base_file = sys.argv[1]
    consulta_file = sys.argv[2]

    listas_termos, nomes_arquivos = abrirArq(base_file)
    indice_invertido = contar_ocorrencias(listas_termos, nomes_arquivos)
    salvar_indice(indice_invertido)

    with open(consulta_file, "r", encoding='utf-8') as consultas:
        resultados = []
        for consulta in consultas:
            consulta = consulta.strip()
            if consulta:
                arquivos_correspondentes = realizar_consulta(consulta, indice_invertido, nomes_arquivos)
                resultados.append(arquivos_correspondentes)

    with open("resposta.txt", "w", encoding='utf-8') as f:
        for arquivos in resultados:
            f.write(f"{len(arquivos)}\n")
            for arquivo in arquivos:
                f.write(f"{arquivo}\n")
            f.write("\n")


if __name__ == "__main__":
    main()
