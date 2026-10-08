from .state import InvestigationState


def parse_request(
    state: InvestigationState,
) -> InvestigationState:

    return {
        **state,
        "merchant_id": "ABC",
        "business_date": "2026-10-07",
    }


def gather_metrics(
    state: InvestigationState,
) -> InvestigationState:

    return {
        **state,
        "settlement_metrics": {
            "yesterday_volume": 8_100_000,
            "baseline_volume": 10_400_000,
            "variance_percent": -22.1,
        },
    }


def analyze_case(
    state: InvestigationState,
) -> InvestigationState:

    metrics = state["settlement_metrics"]

    return {
        **state,
        "facts": [
            f"Settlement volume is "
            f"{metrics['variance_percent']}% below baseline."
        ],
        "hypotheses": [
            "Further operational evidence is required."
        ],
        "recommended_action":
            "INVESTIGATE_FURTHER",
    }


def respond(
    state: InvestigationState,
) -> InvestigationState:

    return {
        **state,
        "final_response": (
            "Merchant ABC settlement volume "
            "is 22.1% below baseline."
        ),
    }