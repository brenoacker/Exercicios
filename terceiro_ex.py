import requests, json

abrir_json = open('data.json')
data = json.load(abrir_json)
lista_cnpjs = data['cnpjs']

num_ddds = len(lista_cnpjs)

i = 0
j = 0
k = 0

lista_ufs = []

while i < num_ddds:

    r = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/{lista_cnpjs[i]}')

    r_dict = r.json()
    uf = r_dict['uf']
    
    lista_ufs.append(uf)
    i = i + 1


regioes = []

while j < num_ddds:
    r = requests.get(f'https://brasilapi.com.br/api/ibge/uf/v1/{lista_ufs[j]}')
    r_dict = r.json()

    regiao = r_dict

    regioes.append(regiao['regiao']['nome'])

    j += 1

numero_socios = {
    "Norte": 0,
    "Nordeste":0,
    "Sul":0,
    "Sudeste":0,
    "Centro-Oeste":0
}

cont_regiao = {
    "Norte": 0,
    "Nordeste":0,
    "Sul":0,
    "Sudeste":0,
    "Centro-Oeste":0
}

cnaes_secundarias = 0

while k < len(regioes):
    
    r = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/{lista_cnpjs[k]}')
    r_dict = r.json()
    try:
        num_socios_local = len(r_dict['qsa'])
    except Exception:
        num_socios_local = 0
    
    if r_dict['cnaes_secundarias'] is not None:
        if len(r_dict['cnaes_secundarias']) > 2:
            cnaes_secundarias += 1

    numero_socios[regioes[k]] += num_socios_local
    cont_regiao[regioes[k]] += 1

    k += 1


dicionario_json1 = {}
dicionario_json2 = {}
dicionario_json3 = {}

print('3a-')
for key in numero_socios:
    dicionario_json1[key] = cont_regiao[key]

json_object = json.dumps(dicionario_json1, indent=4)
print(json_object)

print('\n3b-')
media = {}
for key in numero_socios:
    media[key]=numero_socios[key]/cont_regiao[key]
    dicionario_json2[key] = media[key]

json_object = json.dumps(dicionario_json2, indent=4)
print(json_object)

print('\n3c-')
dicionario_json3['numero de empresas com mais de 2 cnaes secundarias'] = cnaes_secundarias

json_object = json.dumps(dicionario_json3, indent=4)
print(json_object)
