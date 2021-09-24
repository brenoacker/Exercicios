# Mostrar o TOP 5 DDDs que ocorrem no maior número de cidades do Brasil 
# (dica: o documento “data.json” possui uma lista com todos os DDDs válidos);
# https://brasilapi.com.br/api/ddd/v1/{ddd}

#Raciocício: cada DDD tem cidades, filtrar cada ddd por 'cities'
# colocar em uma lista as cidades 
# contar, vendo o tamanho da lista (len)
# criar variavel que recebe essa conta  para cada ddd, criar um {} com 'DDD': 'numero_de_cidades'
# ordenar pelo maior tamanho de 'numero_de_cidades' 
# printar os 5 'DDD' de cada um e o numero de cidades deles

import requests, json

abrir_json = open('data.json')
data = json.load(abrir_json)
lista_ddds = data['ddds']

i = 0


dicionario = {}

#print(len(lista_ddds))

while i < len(lista_ddds):

    r = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{lista_ddds[i]}')

    r_dict = r.json()

    cidades = r_dict['cities']

    num_cidades = len(cidades)

    ddds_local = lista_ddds[i]

    dicionario[ddds_local] = num_cidades
    
    i = i+1


dicionario_organizado = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)


#print('\n')
#print('1-')
#print('\n')

dicionario_json = {}

for i in range(5):
    dicionario_json[dicionario_organizado[i][0]] = dicionario_organizado[i][1]
    #print(f'TOP {i+1}: O DDD {dicionario_organizado[i][0]} está presente em {dicionario_organizado[i][1]} cidades')

#print('\n')

json_object = json.dumps(dicionario_json, indent=4)
print(json_object)

#print('\n')
