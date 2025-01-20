from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from yf_client.model.yahoo_response import YahooFinanceResponse
from app.lib.founding_date_extractor import parse_founding_date


# variable names should probably be snake_cased
@dataclass
class EnrichedStockData:
    ticker: str
    industry: Optional[str] = None
    website: Optional[str] = None
    country: Optional[str] = None
    sector: Optional[str] = None
    summary: Optional[str] = None

    marketCap: Optional[int] = None
    financialCurrency: Optional[str] = None
    recommendationKey: Optional[str] = None
    recommendationMean: Optional[float] = None
    numberOfAnalystOpinions: Optional[int] = None
    totalCash: Optional[int] = None
    totalCashPerShare: Optional[float] = None
    ebitda: Optional[int] = None
    totalDebt: Optional[int] = None
    quickRatio: Optional[float] = None
    currentRatio: Optional[float] = None
    totalRevenue: Optional[int] = None
    debtToEquity: Optional[float] = None
    revenuePerShare: Optional[float] = None
    returnOnAssets: Optional[float] = None
    returnOnEquity: Optional[float] = None
    grossProfits: Optional[int] = None
    freeCashflow: Optional[int] = None
    operatingCashflow: Optional[int] = None
    earningsGrowth: Optional[float] = None
    revenueGrowth: Optional[float] = None
    grossMargins: Optional[float] = None
    ebitdaMargins: Optional[float] = None
    operatingMargins: Optional[float] = None
    profitMargins: Optional[float] = None
    foundingDate: Optional[int] = None

    @classmethod
    def from_yahoo_finance_response(
        cls, ticker: str, response: YahooFinanceResponse
    ) -> EnrichedStockData:
        founding_date = None

        financial_data = response.financial_data or {}
        summary_profile = response.summary_profile or {}
        summary_details = response.summary_details or {}

        if "longBusinessSummary" in summary_profile:
            founding_date = parse_founding_date(summary_profile["longBusinessSummary"])

        return EnrichedStockData(
            ticker,
            summary_profile.get("industryDisp"),
            summary_profile.get("website"),
            summary_profile.get("country"),
            summary_profile.get("sector"),
            summary_profile.get("longBusinessSummary"),
            summary_details.get("marketCap"),
            financial_data.get("financialCurrency"),
            financial_data.get("recommendationKey"),
            financial_data.get("recommendationMean"),
            financial_data.get("numberOfAnalystOpinions"),
            financial_data.get("totalCash"),
            financial_data.get("totalCashPerShare"),
            financial_data.get("ebitda"),
            financial_data.get("totalDebt"),
            financial_data.get("quickRatio"),
            financial_data.get("currentRatio"),
            financial_data.get("totalRevenue"),
            financial_data.get("debtToEquity"),
            financial_data.get("revenuePerShare"),
            financial_data.get("returnOnAssets"),
            financial_data.get("returnOnEquity"),
            financial_data.get("grossProfits"),
            financial_data.get("freeCashflow"),
            financial_data.get("operatingCashflow"),
            financial_data.get("earningsGrowth"),
            financial_data.get("revenueGrowth"),
            financial_data.get("grossMargins"),
            financial_data.get("ebitdaMargins"),
            financial_data.get("operatingMargins"),
            financial_data.get("profitMargins"),
            founding_date,
        )
