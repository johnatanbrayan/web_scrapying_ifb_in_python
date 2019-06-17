import datetime
from urllib.request import urlopen
from urllib.error import HTTPError

def getPage(url):
  try:
    resposta = urlopen(url)
  except HTTPError as e:
    return None
  return resposta

#Função para capturar título da notícia
def getTitle(objeto_soup):
  title = objeto_soup.body.findAll("h2", {"class":"tileHeadline"})
  return title

#Função para capturar descrição da notícia.
def getDescricao(objeto_soup):
  info = objeto_soup.body.findAll("span", {"class":"description"})
  return info

##Função para capturar imagem da notícia.
def getImagem(objeto_soup):
  imagem = []
  lista = objeto_soup.findAll("div", {"class":"tileItem"})
  for item in lista:
    if item.findAll("img"):
      imagem.append(item.findAll('img')[0].attrs['src'])
    else:
      imagem.append("/images/IFBVertical.png")
  return imagem

#função para coletar as urls
def getUrlNoticia(objeto_soup):
  link = []
  lista = objeto_soup.body.findAll("h2", {"class":"tileHeadline"})
  for item in lista:
    link.append(item.find('a').attrs['href'])
  return link

#função para coletar as datas e horas
def getDataHora(objeto_soup):
  horario = []
  lista = objeto_soup.body.findAll("div", {"class":"span2 tileInfo"})
  for item in lista:
    horario.append(item.findAll('li'))
  for i in range(0, len(horario)):
    horario[i] = "{0} {1}".format(horario[i][2].get_text(), horario[i][3].get_text())
  return horario

#obtem os dados sobre data/hora da notícia do arquivo.tmp
def getTmpData(a):
  try:
    arq = open(a, 'r')    
    return arq.read()
  except:
    print("Erro na leitura do arquivo tmp.")

#cria e retorna datetime
def getDT(string):
  string = string.replace("<i>","").replace("</i>","")
  lista_de_dados = string.split()
  ld = lista_de_dados[0].split('/')
  lista_de_hora = lista_de_dados[1].split('h')
  ld.extend(lista_de_hora)
  ld = list(map(int, ld))
  dt = datetime.datetime(2000+ld[2],ld[1],ld[0],ld[3],ld[4])
  return dt
  
'''
#cria e retorna datetime
def getDT(string):
  lista_de_dados = string.split()
  ld = lista_de_dados[0].split('/')
  lista_de_hora = lista_de_dados[1].split('h')
  ld.extend(lista_de_hora)
  ld = list(map(int, ld))
  dt = datetime.datetime(2000+ld[2],ld[1],ld[0],ld[3],ld[4])
  return dt
'''
