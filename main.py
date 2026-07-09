import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
print(f"Servidor LM-Studio escutando em {API_KEY}\n")

URL_N8N_PRODUCTION = os.getenv("URL_N8N_PRODUCTION")
print(f"Servidor N8n escutando em {URL_N8N_PRODUCTION}\n")


session = requests.Session()

#url_path_n8n = "http://localhost:5678/webhook-test/93e3e8f7-57ac-4290-97b9-a92f3197d675"

print("Mode Chat com o AI Agent de N8N\n\n")

control=""

while control != "/bye":
    prompt = input("Chat:\n")
    session_id = "1234" #memória

    dados = {"human-chat":prompt,
             "session_id":session_id} #para memória do agente

    print("Encaminhando mensagem para AI Agent N8N...\n")
    #print(prompt)

    request = session.post(url=URL_N8N_PRODUCTION, json=dados)
    #request = session.post(url=url_path_n8n, data=dados)
    #request = session.post(url=url_path_n8n, json=dados)


    if request.status_code == 200:
        print("Requisição enviada com sucesso\n")
        print(f"Resposta da IA: {request.text}")
        print("*"*20)
        control = input("Para sair digite '/bye', ou tecle enter para continuar!\t")
    else:
        print("Erro de execução")