from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict, Any
from yf_client.model.response_types import (
    SummaryProfileJson,
    SummaryDetailJson,
    FinancialDataJson,
    YahooFinanceJsonResponse,
)


@dataclass
class YahooFinanceResponse:
    financial_data: Optional[FinancialDataJson] = None
    summary_profile: Optional[SummaryProfileJson] = None
    summary_details: Optional[SummaryDetailJson] = None

    @classmethod
    def from_json_response(
        cls, json_response: YahooFinanceJsonResponse
    ) -> YahooFinanceResponse:
        try:
            results = json_response["quoteSummary"]["result"][0]

            financial_data: Optional[FinancialDataJson] = None
            if "financialData" in results:
                financial_data = cls.substitute_none_strings(results.get("financialData"))  # type: ignore

            summary_profile: Optional[SummaryProfileJson] = None
            if "summaryProfile" in results:
                summary_profile = cls.substitute_none_strings(results.get("summaryProfile"))  # type: ignore

            return YahooFinanceResponse(
                financial_data, summary_profile, results.get("summaryDetail")
            )
        except Exception as e:
            print(f"error parsing json response. {e} ---- {json_response} ")
            return YahooFinanceResponse()

    """
    This method is used to substitute the string 'none' with None
    because occasionally the yahoo finance api will return the string 'none'
    """

    @staticmethod
    def substitute_none_strings(dict: Dict[Any, Any]) -> dict[Any, Any]:
        return {k: None if v == "none" else v for k, v in dict.items()}
