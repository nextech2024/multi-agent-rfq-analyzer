import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="🧠 Nextech Multi-AI Procurement Agents", layout="wide")

st.title("🤖 Nextech Multi-AI Agent Dashboard")
st.caption("Trigger individual procurement agents backed by GPT-4o")

agents = {
    "RFQ Manager Agent": "/rfq-manager",
    "Vendor Evaluation Agent": "/vendor-evaluation",
    "Contract Compliance Agent": "/contract-compliance",
    "Pricing Agent": "/pricing-analysis",
    "Lead Time Estimator Agent": "/lead-time",
    "Negotiation Agent": "/negotiate",
    "Risk & Fraud Agent": "/risk-detection"
}

# Create one tab per agent
tabs = st.tabs(list(agents.keys()))

for i, (agent_name, endpoint) in enumerate(agents.items()):
    with tabs[i]:
        st.subheader(agent_name)
        user_input = st.text_area(f"Enter input for {agent_name}", height=150)
        if st.button(f"Run {agent_name}", key=agent_name):
            if user_input.strip():
                try:
                    response = requests.post(
                        f"{BASE_URL}{endpoint}",
                        json={"prompt": user_input}
                    )
                    if response.status_code == 200:
                        st.success("✅ Agent Response")
                        st.json(response.json())
                    else:
                        st.error(f"❌ Failed with {response.status_code}")
                        st.text(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("⚠️ Please enter input text.")
