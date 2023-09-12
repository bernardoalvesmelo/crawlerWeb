import numpy as np
import re

def avaliar_comentarios(comentarios):
    avaliados = []
    
    regexNegativo = re.compile("n(ã|a)ogost|odi(e|o)|horr(í|i)vel|horrendo|horroros|decep|medioc|ru(i|í)m|pior|fei(o|a)|"+
                               "n(ã|a)orecomend|frac(a|o)|menti|vergonh|frustr|meiaboca")
    
    regexPositivo = re.compile("gost|amo|amei|ador|incr|maravilh|bom|melh|curt|(ó|o)tim|lind|sensa|excelen|recomend" +
                               "perf|comovent|emocion|muit(o|a)(bem|boa)|surpreend|impec(á|a)vel|obraprima|cl(á|a)ssico")
    
    for comentario in comentarios:
        comentarioTratado = re.sub("\s", "", comentario).lower()

        if(regexNegativo.search(comentarioTratado) is not None):
            avaliados.append('<NEGATIVO> ' + comentario)
        
        elif(regexPositivo.search(comentarioTratado) is not None):
            avaliados.append('<POSITIVO> ' + comentario)
        
        else:
            avaliados.append('<NEUTRO> ' + comentario)
    
    return avaliados

def salvarComentariosAvaliadosFilme(filme, comentariosOriginais):
        comentarios = avaliar_comentarios(comentariosOriginais)
        arq_saida = open(filme+'_comentarios_avaliados.txt', 'w', encoding='utf-8')
        for comentario in comentarios:
            arq_saida.write(comentario + '\n\n')
        arq_saida.close()

def mostrar_porcentagens(comentarios):
    porcentagens = obter_porcentagens(comentarios)
    print(f"Total de comentários: {porcentagens['total']}")
    print(f"Positivos: {porcentagens['positivo']}%")
    print(f"Negativos: {porcentagens['negativo']}%")
    print(f"Neutros: {porcentagens['neutro']}%")

def obter_porcentagens(comentarios):
    classificacoes = obter_classificacoes(comentarios)
    
    porcentagens =  {
        "positivo" : 0,
        "negativo" : 0,
        "neutro" : 0,
        "total" : classificacoes["total"]
    }

    total = porcentagens["total"] / 100
    porcentagens["positivo"] = np.round(classificacoes["positivo"] / total, 2)
    porcentagens["negativo"] = np.round(classificacoes["negativo"] / total, 2)
    porcentagens["neutro"] = np.round(classificacoes["neutro"] / total, 2)

    return porcentagens

def obter_classificacoes(comentariosOriginais):
    comentarios = avaliar_comentarios(comentariosOriginais)
    
    classificacoes = {
        "positivo" : 0,
        "negativo" : 0,
        "neutro" : 0,
        "total" : 0
    }

    regexPositivo = re.compile("<POSITIVO>")
    regexNegativo = re.compile("<NEGATIVO>")
    regexNeutro = re.compile("<NEUTRO>")
    
    for comentario in comentarios:
        if(regexNegativo.search(comentario) is not None):
            classificacoes["negativo"] += 1
            classificacoes["total"] += 1

        elif(regexPositivo.search(comentario) is not None):
            classificacoes["positivo"] += 1
            classificacoes["total"] += 1

        elif(regexNeutro.search(comentario) is not None):
            classificacoes["neutro"] += 1
            classificacoes["total"] += 1

    return classificacoes

