'''
import telepot
# import funcoes as fun
import json
import time
import os

bot = telepot.Bot("621015027:AAHARD9PB0YBkvc4kIrAOo0V2777FjlNqjo")
chat_id = -391286650

#função para enviar as noticias para o app
def mandaNoticia(arquivo):
  if (os.path.exists("noticias.json")):
    # nomeArquivoTmp = dataUltimaMsgEnviada.tmp 
    a = open('noticias.json', 'r')
    noticias = json.loads(a.read())
    a.close()

    chaves = sorted(noticias.keys())

    #--variavel separador
    # iSep = "--------------------------------------------------------------------------------------"#s
    # iSep = "================================================="
    # iSep = "**************************************************************************"
    # iSep = "¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨"
    # iSep = ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"#s
    iSep = ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"#s p/ mobile
    # iSep = "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    # iSep = "......................................................................................................."#s
    while chaves!=[]:
      noticia = "{0}\n{1}\n{2}\n\n{3}{4}\n\n{5}".format(
        iSep,
        noticias[chaves[0]][0],
        chaves[0], 
        noticias[chaves[0]][1], 
        noticias[chaves[0]][2], 
        noticias[chaves[0]][3])
      
      # dtUltimaMsgEnviada = chaves[0]
      del noticias[chaves[0]]
      del(chaves[0])

      #bot.sendMessage(chat_id, noticia)
      # bot.sendMessage(chat_id, text="*alo*",parse_mode="Markdown")
      bot.sendMessage(chat_id, noticia,parse_mode="HTML")
      time.sleep(2)
  
    os.remove("noticias.json")
    print("O Arquivo foi deletado.")

    # arquivoTmpEnviado = "dataUltimaMsgEnviada.tmp"
    # a = open(arquivoTmpEnviado,'w')
    # a.write(dtUltimaMsgEnviada)
    # a.close()
  else:
    print("Não existe conteúdo no arquivo. Precisa minerar primeiro.")
    
if __name__ == "__main__":
  mandaNoticia("noticias.json")
'''

import telepot
import funcoes as fun
import json
import time
import os

bot = telepot.Bot("621015027:AAHARD9PB0YBkvc4kIrAOo0V2777FjlNqjo")
chat_id = -391286650

#função para enviar as noticias para o app
def mandaNoticia(arquivo):
  cont=0
  if (os.path.exists("noticias.json")):
    arquivoTmpEnviado = "dataUltimaMsgEnviada.tmp" 
    a = open('noticias.json', 'r')
    noticias = json.loads(a.read())
    a.close()

    chaves = sorted(noticias.keys())

    #--variavel separador
    # iSep = "--------------------------------------------------------------------------------------"#s
    # iSep = "================================================="
    # iSep = "**************************************************************************"
    # iSep = "¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨"
    # iSep = ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"#s
    iSep = ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"#s p/ mobile
    # iSep = "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    # iSep = "......................................................................................................."#s
    
    if(os.path.exists(arquivoTmpEnviado)):
      dtUltimaMsgEnviada = fun.getTmpData(arquivoTmpEnviado)
      dtUltimaMsgEnviada = fun.getDT(dtUltimaMsgEnviada)

      for i in range(len(chaves)):
        dateTimeChavesAtual = fun.getDT(str(chaves[i]))
        if(dateTimeChavesAtual > dtUltimaMsgEnviada):
          cont=cont+1
          noticia = "{0}\n{1}\n{2}\n\n{3}{4}\n\n{5}".format(
            iSep,
            noticias[chaves[i]][0],
            chaves[i], 
            noticias[chaves[i]][1], 
            noticias[chaves[i]][2], 
            noticias[chaves[i]][3])
          
          bot.sendMessage(chat_id, noticia,parse_mode="HTML")
          time.sleep(2)
        elif(cont==0):
          print("Não existe novas mensagens.")
    else:
      while chaves!=[]:
        noticia = "{0}\n{1}\n{2}\n\n{3}{4}\n\n{5}".format(
          iSep,
          noticias[chaves[0]][0],
          chaves[0], 
          noticias[chaves[0]][1], 
          noticias[chaves[0]][2], 
          noticias[chaves[0]][3])
        
        dtUltimaMsgEnviada = chaves[0]
        del noticias[chaves[0]]
        del(chaves[0])

        bot.sendMessage(chat_id, noticia,parse_mode="HTML")
        time.sleep(2)
    
    os.remove("noticias.json")
    print("O Arquivo foi deletado.")

    a = open(arquivoTmpEnviado,'w')
    a.write(str(dtUltimaMsgEnviada))
    a.close()

  else:
    print("Não existe conteúdo no arquivo. Precisa minerar primeiro.")

if __name__ == "__main__":
  mandaNoticia("noticias.json")
