from scoring_agent import score_rfq
from pricing_agent import analyze_pricing
from contract_compliance_agent import check_contract_compliance
from vendor_evaluation_agent import evaluate_vendors
from lead_time_agent import estimate_lead_time
from negotiation_agent import negotiate_terms
from risk_agent import detect_risk_fraud

def process_rfq(rfq_text):
    # Extracted or pasted RFI text will flow through each agent
    pricing = analyze_pricing(rfq_text)
    compliance = check_contract_compliance(rfq_text)
    vendors = evaluate_vendors(rfq_text)
    lead_time = estimate_lead_time(rfq_text)
    negotiation = negotiate_terms(rfq_text)
    risks = detect_risk_fraud(rfq_text)
    score = score_rfq(rfq_text)  # ✅ Add this line

    return {
        "Scope_Summary": "This is an AI-generated proposal manager summary.",
        "Pricing_Estimate": pricing,
        "Compliance_Check": compliance,
        "Vendor_Evaluation": vendors,
        "Estimated_Lead_Time": lead_time,
        "Negotiation_Strategy": negotiation,
        "Risk_Assessment": risks,
        "RFQ_Score": score  # ✅ Add this line
    }


   