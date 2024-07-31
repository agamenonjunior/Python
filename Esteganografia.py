from stegano import lsb

imagem = './imagem.png'
mensagem = 'Oi tudo bom ?'

secreto = lsb.hide('./'+imagem,mensagem)
secreto.save('./secreto.png')

reverter = lsb.reveal("./secreto.png")
print(reverter)


