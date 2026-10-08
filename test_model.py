from app.models.openai_model import OpenAIInvestigationModel


model = OpenAIInvestigationModel()

result = model.analyze(
    user_request=(
        "Why did Merchant ABC settlement volume drop yesterday?"
    ),
    merchant_id="ABC",
    business_date="2026-10-07",
    settlement_metrics={
        "yesterday_volume": 8_100_000,
        "baseline_volume": 10_400_000,
        "variance_percent": -22.1,
    },
)

print(result)
print()
print(result.model_dump())