import os
from google import genai

# 1. Configuração da chave de API
API_KEY = "Insira_sua_chave_API_do_Gemini_aqui"

# 2. Inicialização do cliente
client = genai.Client(api_key=API_KEY)

def iniciar_chat_com_historico():
    """
    Cria uma sessão de chat que armazena e gerencia
    o histórico das mensagens enviadas e recebidas.
    """
    # 3. Criação da sessão de chat com o modelo gemini-2.5-flash
    chat = client.chats.create(model="gemini-3.6-flash")
    
    print("=== Chat Contínuo com Gemini (com histórico) ===")
    print("O modelo lembrará das mensagens anteriores!")
    print("Digite 'sair' a qualquer momento para encerrar.\n")
    
    while True:
        pergunta = input("Você: ")
        
        # Encerra o programa se o usuário digitar 'sair'
        if pergunta.lower().strip() == "sair":
            print("\nEncerrando o chat... Até logo!")
            break
            
        # Evita o envio de mensagens em branco
        if not pergunta.strip():
            print("Por favor, digite uma pergunta válida.\n")
            continue
            
        try:
            print("\nGemini pensando...")
            # 4. Envia a mensagem dentro da sessão mantendo o histórico
            resposta = chat.send_message(pergunta)
            
            print("\nGemini:")
            print(resposta.text)
            print("-" * 50 + "\n")
            
        except Exception as e:
            print(f"\nOcorreu um erro ao enviar a mensagem: {e}\n")

# --- Execução do Código ---
if __name__ == "__main__":
    iniciar_chat_com_historico()