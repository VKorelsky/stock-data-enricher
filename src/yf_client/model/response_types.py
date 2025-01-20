from typing import List, Optional, TypedDict


class SummaryProfileJson(TypedDict):
    address1: str
    city: str
    state: str
    zip: str
    country: str
    phone: str
    website: str
    industry: str
    industryDisp: str
    sector: str
    longBusinessSummary: str
    fullTimeEmployees: int
    companyOfficers: List[str]
    maxAge: int


class SummaryDetailJson(TypedDict):
    marketCap: Optional[int]


class FinancialDataJson(TypedDict):
    maxAge: Optional[int]
    currentPrice: Optional[float]
    targetHighPrice: Optional[int]
    targetLowPrice: Optional[int]
    targetMeanPrice: Optional[float]
    targetMedianPrice: Optional[float]
    recommendationMean: Optional[float]
    recommendationKey: Optional[str]
    numberOfAnalystOpinions: Optional[int]
    totalCash: Optional[int]
    totalCashPerShare: Optional[float]
    ebitda: Optional[int]
    totalDebt: Optional[int]
    quickRatio: Optional[float]
    currentRatio: Optional[float]
    totalRevenue: Optional[int]
    debtToEquity: Optional[float]
    revenuePerShare: Optional[float]
    returnOnAssets: Optional[float]
    returnOnEquity: Optional[float]
    grossProfits: Optional[int]
    freeCashflow: Optional[int]
    operatingCashflow: Optional[int]
    earningsGrowth: Optional[int]
    revenueGrowth: Optional[float]
    grossMargins: Optional[float]
    ebitdaMargins: Optional[float]
    operatingMargins: Optional[float]
    profitMargins: Optional[float]
    financialCurrency: Optional[str]


class QuoteSummaryResultJsonType(TypedDict):
    summaryProfile: SummaryProfileJson
    financialData: FinancialDataJson


class QuoteSummaryJsonType(TypedDict):
    result: List[QuoteSummaryResultJsonType]
    error: Optional[object]


class YahooFinanceJsonResponse(TypedDict):
    quoteSummary: QuoteSummaryJsonType
