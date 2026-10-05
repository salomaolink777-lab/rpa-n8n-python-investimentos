import json
import requests

# Dados de exemplo de clientes para a automação RPA
clientes = [
    {
        "nome": "Ana Silva",
        "email": "ana.silva@example.com",
        "perfil": "conservador",
        "investimento": 100000.00
    },
    {
        "nome": "Carlos Oliveira",
        "email": "carlos.oliveira@example.com",
        "perfil": "moderado",
        "investimento": 50000.00
    }
]

def enviar_para_n8n(webhook_url, dados):
    """Envia os dados extraídos para o webhook do n8n."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(dados), headers=headers)
    return response.status_code

if __name__ == "__main__":
    print("Processando extração de dados de clientes...")
    print(f"Total de clientes extraídos: {len(clientes)}")
    # URL de exemplo do webhook no n8n
    N8N_WEBHOOK_URL = "https://seu-n8n.app/webhook/clientes"
    print("Simulação de envio concluída.")
