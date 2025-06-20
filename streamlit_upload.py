import streamlit as st
import requests

st.title("📤 Nextech Procurement AI: Upload Multiple Proposals")

uploaded_files = st.file_uploader("Select one or more PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    if st.button("Analyze All Proposals"):
        for uploaded_file in uploaded_files:
            st.markdown(f"---\n### 📄 {uploaded_file.name}")
            st.info("Uploading to FastAPI...")

            try:
                # Convert to bytes
                file_bytes = uploaded_file.read()
                files = {
                    "file": (uploaded_file.name, file_bytes, "application/pdf")
                }

                response = requests.post("https://ad91-2600-1700-1111-38d0-f96a-887a-3e85-b3c9.ngrok-free.app/upload-rfp-pdf", files=files)



                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ AI Analysis Complete")
                    st.json(result)
                else:
                    st.error(f"❌ FastAPI responded with status: {response.status_code}")
                    st.text(response.text)

            except Exception as e:
                st.error(f"❌ Connection to FastAPI failed: {e}")
