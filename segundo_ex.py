import requests, json

#Pegar todas as 'siglas' de https://brasilapi.com.br/api/ibge/uf/v1
#Colocar em uma lista todas as UFs
#Fazer um loop que pegue todas as UFs em https://brasilapi.com.br/api/ibge/municipios/v1/{siglaUF}
#dentro do loop, contar o numero de municipios
#dentro do loop, fazer contagem de municipios

r = requests.get('https://brasilapi.com.br/api/ibge/uf/v1')
r_dict = r.json()

lista_siglas = []

i = 0
j = 0
k = 0

#Pegar todas as siglas de estado
while i < len(r_dict):

    sigla_local = r_dict[i]['sigla']

    lista_siglas.append(sigla_local)
    
    i = i + 1

#Fazer o loop
# filtrar pela cidade 
# colocar um dict que tem a sigla e o numero de municipios (len())

uf_numeromunicipios = {}
while j < len(lista_siglas):

    r_local = requests.get(f'https://brasilapi.com.br/api/ibge/municipios/v1/{lista_siglas[j]}')
    r_dict_local = r_local.json()
    #print(len(r_dict_local))
    
    sigla_local = lista_siglas[j]
    uf_numeromunicipios[sigla_local] = len(r_dict_local)

    j = j + 1


print('\n')
print('De acordo com dados do IBGE:\n')

while k < len(lista_siglas):
    var = lista_siglas[k]

    if uf_numeromunicipios[var] == 1:
        print(f'{lista_siglas[k]} possui {uf_numeromunicipios[var]} município')

    else:
        print(f'{lista_siglas[k]} possui {uf_numeromunicipios[var]} municípios')

    k += 1

print('\n')


