from fastapi import FastAPI, Request, UploadFile, File
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load OpenAI API key from .env
load_dotenv()
print("✅ Loaded API KEY:", os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")
print("🔑 FastAPI Loaded OpenAI Key:", openai.api_key[:10])


app = FastAPI()

# Allow simple root check
@app.get("/")
def read_root():
    return {"message": "✅ Nextech Procurement API is running"}

# Input schema for agents
class AIRequest(BaseModel):
    prompt: str

# Scope Summary Agent (for raw text)
class ScopeRequest(BaseModel):
    text: str

@app.post("/scope-summary")
async def scope_summary(payload: ScopeRequest):
    prompt = f"Summarize the business scope of this proposal:\n\n{payload.text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        summary = response['choices'][0]['message']['content']
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

# General AI Assistant
@app.post("/ask-ai")
def ask_openai(req: AIRequest):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": req.prompt}]
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

# 🔗 Agent imports
from rfq_manager import process_rfq
from vendor_evaluation_agent import evaluate_vendors
from contract_compliance_agent import check_contract_compliance
from pricing_agent import analyze_pricing
from lead_time_agent import estimate_lead_time
from negotiation_agent import negotiate_terms
from risk_agent import detect_risk_fraud
from upload_rfp_agent import extract_text_from_pdf

# Agent endpoints
@app.post("/rfq-manager")
def call_rfq_manager(req: AIRequest):
    result = process_rfq(req.prompt)
    return {"manager_response": result}

@app.post("/vendor-evaluation")
def call_vendor_evaluator(req: AIRequest):
    result = evaluate_vendors(req.prompt)
    return {"vendor_analysis": result}

@app.post("/contract-compliance")
def call_contract_checker(req: AIRequest):
    result = check_contract_compliance(req.prompt)
    return {"compliance_review": result}

@app.post("/pricing-analysis")
def call_pricing_agent(req: AIRequest):
    result = analyze_pricing(req.prompt)
    return {"pricing_insights": result}

@app.post("/lead-time")
def call_lead_time_agent(req: AIRequest):
    result = estimate_lead_time(req.prompt)
    return {"lead_time_analysis": result}

@app.post("/negotiate")
def call_negotiation_agent(req: AIRequest):
    result = negotiate_terms(req.prompt)
    return {"negotiation_strategy": result}

@app.post("/risk-detection")
def call_risk_agent(req: AIRequest):
    result = detect_risk_fraud(req.prompt)
    return {"risk_assessment": result}

# ✅ PDF Upload Endpoint used by both Swagger & Streamlit
@app.post("/upload-rfp-pdf")
async def upload_rfp_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = f"uploaded_{file.filename}"
    
    # Save PDF to disk
    with open(file_path, "wb") as f:
        f.write(contents)

    # Extract text from the saved PDF
    extracted_text = extract_text_from_pdf(file_path)
    
    # Use RFQ Manager Agent to analyze proposal
    result = process_rfq(extracted_text)

    return {
        "filename": file.filename,
        "extracted_summary": result
    }

