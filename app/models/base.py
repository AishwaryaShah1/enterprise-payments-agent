from abc import ABC, abstractmethod

from app.models.schemas import InvestigationResult


class BaseInvestigationModel(ABC):

    @abstractmethod
    def analyze(
        self,
        user_request: str,
        merchant_id: str,
        business_date: str,
        settlement_metrics: dict,
    ) -> InvestigationResult:
        pass