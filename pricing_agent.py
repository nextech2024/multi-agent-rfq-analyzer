import openai
import os

try:
    import streamlit as st
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_pricing(vendor_quotes: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Pricing Agent. Compare vendor pricing data for cost effectiveness, fairness, and strategic value."},
                {"role": "user", "content": vendor_quotes}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error in Pricing Agent: {str(e)}"


