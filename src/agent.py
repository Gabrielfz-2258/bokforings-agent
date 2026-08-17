from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
client = Anthropic()


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



if __name__ == "__main__":
    resultat =analyze_reciept("ICA Maxi, 2026-08-17, Kaffe 89kr ")
    print(resultat)