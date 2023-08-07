import json
import requests

def write_http_response(status, body_dict):

    return_dict = {
        "status": status,
        "body": json.dumps(body_dict),
    }
    return json.dumps(return_dict)


def buscar_cep(cep):
    try:
        cep_encontrado = False
        while len(cep) < 8:
            print("\033[31mDados Inválidos. Digite um CEP válido.\33[m")
            cep = input("Digite o CEP: ")
            # Consumo API
            base_url = f"https://viacep.com.br/ws/{cep}/json/"
            request = requests.get(base_url)
            if request.status_code == 200:
                print(f"\033[32mConnection OK\33[m.")
                request = request.json()
                print("-" *50)
                print(f"Cep: {request['cep']}")
                print(f"Logradouro: {request['logradouro']}")
                print(f"Complemento: {request['complemento']}")
                print(f"Bairro: {request['bairro']}")
                print(f"Localidade: {request['localidade']}")
                print(f"UF: {request['uf']}")
                print("-" *50)
                cep_encontrado = True

        if cep_encontrado == False:
            print(f"CEP \033[31m{cep}\33[m Inválido.")
    except:
        write_http_response(401,
            { 'message': 'Connection Refused'}
        )