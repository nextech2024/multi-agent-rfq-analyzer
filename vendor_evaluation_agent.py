import os
import openai
from dotenv import load_dotenv

# Load the API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_vendors(vendor_info: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Vendor Evaluation Agent. Assess vendor quality based on certifications, delivery timelines, reputation, and RFQ alignment."},
                {"role": "user", "content": vendor_info}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error in Vendor Evaluation: {str(e)}"
