url = 'https://bytebank.com/cambio?moedaOrigem=real'
print(url)

# para acessarmos uma parte da string/fatiar ela
urlParteUm = url[0:16]
#print(urlParteUm)

# esse método não altera a string original

# método find()
indice_interrogaçao = url.find('?')
url_base = url[:indice_interrogaçao]
#print(url_base)

url_parametros = url[indice_interrogaçao+1:]
print(url_parametros)

# método len()
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)

print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]

print(valor)