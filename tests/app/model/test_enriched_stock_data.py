import json
import pytest

from src.app.model.enriched_stock_data import EnrichedStockData
from src.yf_client.model.yahoo_response import YahooFinanceResponse
from tests.yf_client.response_fixtures import (
    FULL_JSON_RESPONSE,
    PARTIAL_JSON_RESPONSE,
)

TICKER = "AAPL"


@pytest.fixture
def full_yahoo_finance_response() -> YahooFinanceResponse:
    return YahooFinanceResponse.from_json_response(json.loads(FULL_JSON_RESPONSE))


@pytest.fixture
def yahoo_finance_response_with_no_founding_date(
    full_yahoo_finance_response: YahooFinanceResponse,
) -> YahooFinanceResponse:
    summary_with_no_date = "The company does a lot of business and is very profitable. The founding date is unfortunately not known."
    full_yahoo_finance_response.summary_profile["longBusinessSummary"] = summary_with_no_date  # type: ignore
    return full_yahoo_finance_response


@pytest.fixture
def yahoo_finance_response_missing_data() -> YahooFinanceResponse:
    return YahooFinanceResponse().from_json_response(json.loads(PARTIAL_JSON_RESPONSE))


def test_from_yahoo_finance_response_with_partial_data(
    yahoo_finance_response_missing_data: YahooFinanceResponse,
):
    enriched = convert(yahoo_finance_response_missing_data)

    assert enriched.ticker == TICKER
    assert enriched.recommendationMean == 2
    assert enriched.numberOfAnalystOpinions == 38
    assert enriched.totalCash == 55872000000
    assert enriched.grossMargins == 0.43181
    assert enriched.ebitdaMargins == 0.32145
    assert enriched.profitMargins == 0.24493
    assert enriched.financialCurrency == "USD"

    assert enriched.recommendationKey == None
    assert enriched.ebitda == None
    assert enriched.totalDebt == None
    assert enriched.quickRatio == None
    assert enriched.currentRatio == None
    assert enriched.totalRevenue == None
    assert enriched.debtToEquity == None
    assert enriched.revenuePerShare == None
    assert enriched.returnOnAssets == None
    assert enriched.returnOnEquity == None
    assert enriched.grossProfits == None
    assert enriched.freeCashflow == None
    assert enriched.operatingCashflow == None
    assert enriched.earningsGrowth == None
    assert enriched.revenueGrowth == None
    assert enriched.operatingMargins == None
    assert enriched.foundingDate == None


def test_from_yahoo_finance_response_with_founding_date(
    full_yahoo_finance_response: YahooFinanceResponse,
):
    enriched = convert(full_yahoo_finance_response)

    assert enriched.ticker == TICKER
    assert enriched.recommendationMean == 2
    assert enriched.recommendationKey == "buy"
    assert enriched.numberOfAnalystOpinions == 38
    assert enriched.totalCash == 55872000000
    assert enriched.totalCashPerShare == 3.552
    assert enriched.ebitda == 123788001280
    assert enriched.totalDebt == 109614997504
    assert enriched.quickRatio == 0.764
    assert enriched.currentRatio == 0.94
    assert enriched.totalRevenue == 385095008256
    assert enriched.debtToEquity == 176.349
    assert enriched.revenuePerShare == 24.116
    assert enriched.returnOnAssets == 0.20559
    assert enriched.returnOnEquity == 1.4560499
    assert enriched.grossProfits == 170782000000
    assert enriched.freeCashflow == 83796623360
    assert enriched.operatingCashflow == 109583998976
    assert enriched.earningsGrowth == 0
    assert enriched.revenueGrowth == -0.025
    assert enriched.grossMargins == 0.43181
    assert enriched.ebitdaMargins == 0.32145
    assert enriched.operatingMargins == 0.29163
    assert enriched.profitMargins == 0.24493
    assert enriched.financialCurrency == "USD"
    assert enriched.foundingDate == 1977


def test_from_yahoo_finance_response_without_founding_date(
    yahoo_finance_response_with_no_founding_date: YahooFinanceResponse,
):
    enriched = convert(yahoo_finance_response_with_no_founding_date)
    assert enriched.foundingDate == None


def convert(stock_data: YahooFinanceResponse) -> EnrichedStockData:
    return EnrichedStockData.from_yahoo_finance_response(TICKER, stock_data)
