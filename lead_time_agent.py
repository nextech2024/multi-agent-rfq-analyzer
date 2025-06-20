import os
import openai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def estimate_lead_time(delivery_info: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Lead Time Estimator Agent. Assess the feasibility of delivery timelines based on vendor info, urgency, geography, production time, and holidays. Highlight any risks or unrealistic commitments."},
                {"role": "user", "content": delivery_info}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error in Lead Time Agent: {str(e)}"
