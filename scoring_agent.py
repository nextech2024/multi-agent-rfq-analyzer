def score_rfq(rfq_text):
    # Initialize individual scores
    qualification_score = 0
    price_score = 0
    compliance_score = 0
    risk_score = 0
    reasons = []

    text = rfq_text.lower()

    # ---- Qualification & Experience (40%) ----
    if "workday" in text or "sap" in text or "oracle" in text:
        qualification_score += 20
        reasons.append("Mentions specific platforms like Workday, SAP, or Oracle")

    if "project manager" in text or "engineer" in text or "technical support" in text:
        qualification_score += 10
        reasons.append("Covers qualified technical roles")

    if "fte" in text:
        qualification_score += 10
        reasons.append("Defines full-time resource needs (FTEs)")

    # ---- Price (30%) ----
    if "$" in text or "dollars" in text:
        price_score += 20
        reasons.append("Includes pricing estimate")

    if "monthly rate" in text or "hourly rate" in text:
        price_score += 10
        reasons.append("Mentions billing structure")

    # ---- Compliance (20%) ----
    if "soc2" in text or "hipaa" in text or "pci" in text:
        compliance_score += 15
        reasons.append("Mentions compliance standards like SOC2 or HIPAA")

    if "insurance" in text:
        compliance_score += 5
        reasons.append("Includes insurance requirements")

    # ---- Risk (10%) ----
    if "delay" in text or "onboarding" in text or "risk" in text:
        risk_score += 5
        reasons.append("Mentions delivery risks")

    if "backup resources" in text or "escalation" in text:
        risk_score += 5
        reasons.append("Mentions mitigation plans")

    # ---- Normalize to 100 ----
    total_score = (
        (qualification_score * 0.4) +
        (price_score * 0.3) +
        (compliance_score * 0.2) +
        (risk_score * 0.1)
    )

    return {
        "Match_Score": round(total_score),
        "Summary": "High match" if total_score >= 75 else "Moderate" if total_score >= 50 else "Low",
        "Reasons": reasons,
        "Breakdown": {
            "Qualification & Experience": qualification_score,
            "Price": price_score,
            "Compliance": compliance_score,
            "Risk": risk_score
        }
    }
