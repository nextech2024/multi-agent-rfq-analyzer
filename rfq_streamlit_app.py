import streamlit as st
import pdfplumber
import pandas as pd
from rfq_manager import process_rfq

st.set_page_config(page_title="📄 Nextech Proposal Evaluator", layout="wide")

st.title("📄 Nextech Multi-Agent Proposal Evaluator")
st.markdown("Upload multiple vendor proposals (PDF). The system will extract the content from each file, analyze it using multiple AI agents, and give you a side-by-side comparison table for decision-making.")

# MULTI-FILE UPLOAD
uploaded_files = st.file_uploader("📤 Upload Vendor Proposal PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    results = []

    for file in uploaded_files:
        with st.spinner(f"🔍 Processing {file.name}..."):
            with pdfplumber.open(file) as pdf:
                text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

            result = process_rfq(text)

            # Show full analysis per file
            with st.expander(f"📂 Full AI Analysis for {file.name}"):
                st.subheader("🧠 Scope Summary")
                st.write(result["Scope_Summary"])

                st.subheader("💰 Pricing Estimate")
                st.write(result["Pricing_Estimate"])

                st.subheader("🛡️ Compliance Check")
                st.write(result["Compliance_Check"])

                st.subheader("🏢 Vendor Evaluation")
                st.write(result["Vendor_Evaluation"])

                st.subheader("⏱️ Estimated Lead Time")
                st.write(result["Estimated_Lead_Time"])

                st.subheader("🤝 Negotiation Strategy")
                st.write(result["Negotiation_Strategy"])

                st.subheader("🚨 Risk Assessment")
                st.write(result["Risk_Assessment"])

                st.subheader("📊 RFQ Match Score")
                st.metric(label="Score", value=result["RFQ_Score"]["Match_Score"])
                st.write(result["RFQ_Score"]["Summary"])
                st.write("Reasons:", result["RFQ_Score"]["Reasons"])

            # Add result to comparison table
            results.append({
                "Vendor": file.name,
                "Score": result["RFQ_Score"]["Match_Score"],
                "Score Summary": result["RFQ_Score"]["Summary"],
                "Price (Est)": result["Pricing_Estimate"],
                "Compliance": result["Compliance_Check"],
                "Risk": result["Risk_Assessment"]
            })

    st.success("✅ All proposals analyzed.")

    # DISPLAY COMPARISON TABLE
    df = pd.DataFrame(results)
    st.subheader("📊 Vendor Comparison Table")
    st.dataframe(df)

    # DOWNLOAD CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Comparison Table", csv, "comparison_table.csv", "text/csv")
