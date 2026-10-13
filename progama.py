# CP5 Python
# Felipe Luan RM: 569565
# Anderson Macolino RM: 
# Turma: 1EPSPQ

import json

NOME_SISTEMA = "Plantão de TI"
ARQ_OCORRENCIAS = "ocorrencias.json"
ARQ_DIARIO = "diario.txt"
ARQ_PASSAGEM = "passagem.txt"

PRIORIDADES = ["alta", "media", "baixa"]
STATUS = ["aberto", "resolvido"]



# Leitura e gravação do JSON

def carregar_ocorrencias():
    #Retorna a lista salva, [] se o arquivo não existir ou None se o JSON for inválido."""
    try:
        with open(ARQ_OCORRENCIAS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        mostrar_erro_json()
        return None

    if not isinstance(dados, list):
        mostrar_erro_json()
        return None
    return dados


def mostrar_erro_json():
    print("\nERRO: o arquivo " + ARQ_OCORRENCIAS + " está com formato inválido.")
    print("Abra o arquivo, corrija o conteúdo (ele deve ser uma lista JSON, como []) e tente de novo.")
    print("O arquivo não foi alterado. Cadastro, consulta de ocorrências e passagem de plantão")
    print("ficam suspensos até a correção. O diário continua disponível.")


def salvar_ocorrencias(lista):
    with open(ARQ_OCORRENCIAS, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)



# Entrada de dados

def pedir_texto(mensagem):
    texto = input(mensagem).strip()
    while texto == "":
        print("O campo não pode ficar vazio.")
        texto = input(mensagem).strip()
    return texto


def pedir_opcao(mensagem, validas):
    valor = input(mensagem).strip().lower()
    while valor not in validas:
        print("Valor inválido. Use: " + ", ".join(validas) + ".")
        valor = input(mensagem).strip().lower()
    return valor