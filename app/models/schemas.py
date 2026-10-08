from typing import Literal

from pydantic import BaseModel, Field


class InvestigationResult(BaseModel):
    facts: list[str] = Field(
        description="Facts directly supported by the supplied evidence."
    )

    hypotheses: list[str] = Field(
        description=(
            "Possible explanations that are not yet proven. "
            "Do not present hypotheses as facts."
        )
    )

    recommended_action: Literal[
        "NO_ACTION",
        "INVESTIGATE_FURTHER",
        "OPEN_INCIDENT",
    ]

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence in the recommendation from 0 to 1.",
    )

    needs_human_approval: bool