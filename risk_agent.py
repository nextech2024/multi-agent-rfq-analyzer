import os
import openai
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_risk_fraud(vendor_data: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Risk and Fraud Detection Agent. Analyze vendor offers, pricing patterns, and contract language to detect red flags, inconsistencies, or unusual behaviors that may indicate fraud, collusion, or compliance risk."},
                {"role": "user", "content": vendor_data}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error in Risk Agent: {str(e)}"
