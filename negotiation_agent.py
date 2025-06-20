import os
import openai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def negotiate_terms(rfq_context: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Procurement Negotiation Agent. Based on the RFQ and vendor terms provided, propose fair counteroffers, better payment terms, or delivery improvements. Be tactful but firm, and aim for win-win."},
                {"role": "user", "content": rfq_context}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error in Negotiation Agent: {str(e)}"
