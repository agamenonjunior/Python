from stegano import lsb

imagem = './imagem.png'
mensagem = 'Oi tudo bom ?'
#realiza a Esteganografia
secreto = lsb.hide('./'+imagem,mensagem)
secreto.save('./secreto.png')
#Exibe a mensagem escondida na imagem
reverter = lsb.reveal("./secreto.png")
print(reverter)


