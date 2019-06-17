
import json
import funcoes as fun
from bs4 import BeautifulSoup
import os
import bot

def minerar():
  #--coleta a resposta http
  linkPage = "http://www.ifb.edu.br/brasilia/noticiasbrasilia"
  respostaHttp = fun.getPage(linkPage)
  soup = BeautifulSoup(respostaHttp.read(), features="html.parser")

  #--atribui as chamadas das funcoes para uma variavel
  capturaDataHora = fun.getDataHora(soup)
  capturaImg = fun.getImagem(soup)
  capturaTitulo = fun.getTitle(soup)
  capturaDescricao = fun.getDescricao(soup)
  capturaLink = fun.getUrlNoticia(soup)

  #cria as lista para cada tipo de informação a ser guardada
  listaDataHora = []
  listaImg = []
  listaTitulo = []
  listaDescricao = []
  listaLinkNoticia = []

  #verifica se existe algo no retorno
  if(capturaDataHora!=None and capturaImg!=None and capturaTitulo!=None and capturaDescricao!=None and capturaLink!=None):
    #variavel negrito
    iBold = "<b>"
    fBold = "</b>"
    #variavel italico
    iItalic = "<i>"
    fItalic = "</i>"
    #adiciona os textos formatados às listas correspondente
    for i in range(len(capturaTitulo)):
      listaDataHora.append(iItalic+capturaDataHora[i].strip()+fItalic)
      listaImg.append('<a href="{}{}">.</a>'.format("https://www.ifb.edu.br",capturaImg[i]))
      listaTitulo.append(iBold+capturaTitulo[i].get_text().strip()+fBold)
      listaDescricao.append(capturaDescricao[i].get_text().strip())
      listaLinkNoticia.append("https://www.ifb.edu.br{}".format(capturaLink[i]))
  else:
    print("Ocorreu um erro na captura das informações!")

  #--criando dicionario de noticias
  listaDeNoticias = {}
  # for i in range(len(listaTitulo)): 
  for i in range(10): 
    listaDeNoticias[listaDataHora[i]] = \
    (
      listaTitulo[i],
      listaDescricao[i],
      listaImg[i],
      listaLinkNoticia[i]
    )
  #print(listaDeNoticias)

  nomeArquivoJson = "noticias.json"
  nomeArquivoTmp = 'arquivo.tmp'

  #--confere se o arquivo json existe, se existir, carrega o arquivo
  if (os.path.exists(nomeArquivoJson)):
    a = open(nomeArquivoJson, "r")
    noticiasJs = json.loads(a.read())
    a.close()

    ultimaDataHora = fun.getTmpData(nomeArquivoTmp)
    ultimaDataHora = fun.getDT(ultimaDataHora)

    # Dentro desse for estamos navegando nas chaves da lista de noticias
    for dataHora in listaDeNoticias.keys():
      dataHoraConvertida = fun.getDT(dataHora)
      # Dentro desse if teremos as datas e horas de noticias novas (que não estão no arquivo .json)
      if dataHoraConvertida > ultimaDataHora:
        noticiasJs[dataHora] = \
          (
            listaDeNoticias[dataHora][0],
            listaDeNoticias[dataHora][1],
            listaDeNoticias[dataHora][2],
            listaDeNoticias[dataHora][3]
          )
    # Fora do for, gerar o JSON novo e salvar no arquivo com o mesmo nome com permissão W
    a = open(nomeArquivoJson, 'w')
    js = json.dumps(noticiasJs, ensure_ascii=False, indent=2)
    js = str(js)
    a.write(js)
    a.close()
  else:
    js = json.dumps(listaDeNoticias, ensure_ascii=False, indent=2)
    js = str(js)
    a = open(nomeArquivoJson, 'w')
    a.write(js)
    a.close()

  #salva a data/hora da última notícia em arquivo temporário
  arquivo_tmp = open(nomeArquivoTmp, 'w')
  arquivo_tmp.write(list(listaDeNoticias.keys())[0])
  arquivo_tmp.close()

  #teste para envio de noticias
  #bot.mandaNoticia(nomeArquivoJson)

if __name__ == "__main__":
  minerar()

