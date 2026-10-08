from typing import TypedDict


class InvestigationState(TypedDict, total=False):
    user_request: str

    merchant_id: str
    business_date: str

    settlement_metrics: dict

    runbook_evidence: list[dict]
    incidents: list[dict]
    deployments: list[dict]
    processor_health: dict

    facts: list[str]
    hypotheses: list[str]

    recommended_action: str
    confidence: float

    approval_required: bool
    approval_status: str

    final_response: str