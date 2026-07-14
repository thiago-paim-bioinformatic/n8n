import requests

WEBHOOK_N8N = "http://localhost:5678/webhook-test/be24c4a0-6d10-4ead-9f1a-f2a3d26a8a79"

path_file = r"D:\SCRIPT\webhook-n8n\ALEXANDRE FERREIRA.pdf"

with open(path_file, "rb") as file:
    file_to_n8n = {
        "arquivo_pdf":(path_file, file, "application/pdf")
    }
    dados_extras = {
        "descricao":"teste de arquivo pdf",
    }

    resposta = requests.post(url=WEBHOOK_N8N, files=file_to_n8n, data=dados_extras, timeout=120)

if resposta.status_code == 200:
    print("OK, enviado para o N8N")

    dados_retornados = resposta.json()

    try: 
        if dados_retornados:
            print("Processamento realizado com sucesso!!!\n\n")
            print(dados_retornados)
    except Exception as e:

        print(f"Erro de processamento: {e}")
else:
    print("Erro")
