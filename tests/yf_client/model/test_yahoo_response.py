import json
from src.yf_client.model.yahoo_response import YahooFinanceResponse
from src.yf_client.model.response_types import SummaryProfileJson, FinancialDataJson
from tests.yf_client.response_fixtures import (
    FULL_JSON_RESPONSE,
    MISSING_FINANCIAL_DATA_JSON_RESPONSE,
    PARTIAL_JSON_RESPONSE,
    UNEXPECTED_JSON_RESPONSE,
    NOT_FOUND_JSON_RESPONSE,
)


def test_handles_none_from_response():
    json_response = json.loads(FULL_JSON_RESPONSE)
    json_response["quoteSummary"]["result"][0]["financialData"][
        "recommendationKey"
    ] = "none"

    converted = YahooFinanceResponse.from_json_response(json_response)

    assert converted.financial_data is not None
    assert converted.financial_data["recommendationKey"] == None


def test_not_found_response():
    response = YahooFinanceResponse.from_json_response(
        json.loads(NOT_FOUND_JSON_RESPONSE)
    )

    assert response.financial_data is None
    assert response.summary_profile is None


def test_from_unexpected_json_response():
    response = YahooFinanceResponse.from_json_response(
        json.loads(UNEXPECTED_JSON_RESPONSE)
    )
    assert response.financial_data is None
    assert response.summary_profile is None


def test_from_partial_json_response():
    response = YahooFinanceResponse.from_json_response(
        json.loads(PARTIAL_JSON_RESPONSE)
    )
    assert response.financial_data is not None
    assert response.summary_profile is not None


def test_from_missing_financial_data_json_response():
    response = YahooFinanceResponse.from_json_response(
        json.loads(MISSING_FINANCIAL_DATA_JSON_RESPONSE)
    )
    assert response.financial_data is None
    assert response.summary_profile is not None


def test_from_full_json_response():
    response = YahooFinanceResponse.from_json_response(json.loads(FULL_JSON_RESPONSE))

    assert response.financial_data is not None
    assert response.summary_profile is not None


def assert_full_financial_data(converted: FinancialDataJson):
    assert converted["currentPrice"] == 180.95
    assert converted["targetHighPrice"] == 209
    assert converted["targetLowPrice"] == 118
    assert converted["targetMeanPrice"] == 180.27
    assert converted["targetMedianPrice"] == 184.43
    assert converted["recommendationMean"] == 2
    assert converted["recommendationKey"] == "buy"
    assert converted["numberOfAnalystOpinions"] == 38
    assert converted["totalCash"] == 55872000000
    assert converted["totalCashPerShare"] == 3.552
    assert converted["ebitda"] == 123788001280
    assert converted["totalDebt"] == 109614997504
    assert converted["quickRatio"] == 0.764
    assert converted["currentRatio"] == 0.94
    assert converted["totalRevenue"] == 385095008256
    assert converted["debtToEquity"] == 176.349
    assert converted["revenuePerShare"] == 24.116
    assert converted["returnOnAssets"] == 0.20559
    assert converted["returnOnEquity"] == 1.4560499
    assert converted["grossProfits"] == 170782000000
    assert converted["freeCashflow"] == 83796623360
    assert converted["operatingCashflow"] == 109583998976
    assert converted["earningsGrowth"] == 0
    assert converted["revenueGrowth"] == -0.025
    assert converted["grossMargins"] == 0.43181
    assert converted["ebitdaMargins"] == 0.32145
    assert converted["operatingMargins"] == 0.29163
    assert converted["profitMargins"] == 0.24493
    assert converted["financialCurrency"] == "USD"


def assert_full_summary_profile(converted: SummaryProfileJson):
    assert converted["address1"] == "One Apple Park Way"
    assert converted["city"] == "Cupertino"
    assert converted["state"] == "CA"
    assert converted["zip"] == "95014"
    assert converted["country"] == "United States"
    assert converted["phone"] == "408 996 1010"
    assert converted["website"] == "https://www.apple.com"
    assert converted["industry"] == "Consumer Electronics"
    assert converted["industryDisp"] == "Consumer Electronics"
    assert converted["sector"] == "Technology"
    assert (
        converted["longBusinessSummary"]
        == "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, and HomePod. It also provides AppleCare support and cloud services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. In addition, the company offers various services, such as Apple Arcade, a game subscription service; Apple Fitness+, a personalized fitness service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California."
    )
    assert converted["fullTimeEmployees"] == 164000
    assert converted["companyOfficers"] == []
    assert converted["maxAge"] == 86400
