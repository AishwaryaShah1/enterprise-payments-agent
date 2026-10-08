from openai import OpenAI

from app.config import get_settings
from app.models.base import BaseInvestigationModel
from app.models.schemas import InvestigationResult


class OpenAIInvestigationModel(BaseInvestigationModel):

    def __init__(self):
        settings = get_settings()

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

        self.model = settings.openai_model

    def analyze(
        self,
        user_request: str,
        merchant_id: str,
        business_date: str,
        settlement_metrics: dict,
    ) -> InvestigationResult:

        prompt = f"""
You are an enterprise payments operations investigation assistant.

Your job is to analyze only the evidence supplied to you.

Rules:
1. Facts must be directly supported by supplied evidence.
2. Hypotheses must be clearly separated from facts.
3. Do not invent missing information.
4. If evidence is insufficient, recommend INVESTIGATE_FURTHER.
5. OPEN_INCIDENT should require human approval.
6. Return a confidence between 0 and 1.

User request:
{user_request}

Merchant:
{merchant_id}

Business date:
{business_date}

Settlement metrics:
{settlement_metrics}
"""

        response = self.client.responses.parse(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are a careful payments operations "
                        "investigation assistant."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            text_format=InvestigationResult,
        )

        if response.output_parsed is None:
            raise RuntimeError(
                "OpenAI returned no parsed investigation result."
            )

        return response.output_parsed