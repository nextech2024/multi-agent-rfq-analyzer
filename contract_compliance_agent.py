import os
import openai
from dotenv import load_dotenv

# Load OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def check_contract_compliance(contract_text: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Contract Compliance Agent. Analyze the provided contract terms and identify any clauses that may conflict with corporate compliance policies or legal best practices."},
                {"role": "user", "content": contract_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error in Contract Compliance Agent: {str(e)}"
