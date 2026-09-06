from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
client = Anthropic()
conversation_history = []


def analyze_reciept(receipt_text):
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system="Du är en svensk bokföringsassistent. Analysera kvitton och returnera alltid: kostnadstyp, BAS-kontokod och momssats (0%, 6%, 12% eller 25%).",
        messages=[
            {"role": "user", "content": receipt_text}
        ],

    ) 
    return response.content[0].text

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    
    })
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system="Du är en svensk bokföringsassistent som hjälper frilansare och konsulter med bokföringsfrågor.",
        messages=conversation_history
       
    )
    assistant_message = response.content[0].text
    conversation_history.append({
                "role": "assistant",
                "content": assistant_message
     })

    return assistant_message





if __name__ == "__main__":
    while True:
        user_input = input("DU: ")
        if user_input.lower() == "avsluta":
            break
        svar = chat(user_input)
        print(f"Agent: {svar}\n")