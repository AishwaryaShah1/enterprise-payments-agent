from fastapi import FastAPI
from pydantic import BaseModel

from app.harness.graph import payments_graph


app = FastAPI(
    title="Enterprise Payments Operations AI Agent"
)


class InvestigationRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/investigate")
def investigate(
    request: InvestigationRequest,
):

    result = payments_graph.invoke(
        {
            "user_request":
                request.question
        }
    )

    return result