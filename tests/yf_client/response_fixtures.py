FULL_JSON_RESPONSE = """
{
  "quoteSummary": {
    "result": [
      {
        "summaryProfile": {
          "address1": "One Apple Park Way",
          "city": "Cupertino",
          "state": "CA",
          "zip": "95014",
          "country": "United States",
          "phone": "408 996 1010",
          "website": "https://www.apple.com",
          "industry": "Consumer Electronics",
          "industryDisp": "Consumer Electronics",
          "sector": "Technology",
          "longBusinessSummary": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, and HomePod. It also provides AppleCare support and cloud services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. In addition, the company offers various services, such as Apple Arcade, a game subscription service; Apple Fitness+, a personalized fitness service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.",
          "fullTimeEmployees": 164000,
          "companyOfficers": [],
          "maxAge": 86400
        },
        "financialData": {
          "maxAge": 86400,
          "currentPrice": 180.95,
          "targetHighPrice": 209,
          "targetLowPrice": 118,
          "targetMeanPrice": 180.27,
          "targetMedianPrice": 184.43,
          "recommendationMean": 2,
          "recommendationKey": "buy",
          "numberOfAnalystOpinions": 38,
          "totalCash": 55872000000,
          "totalCashPerShare": 3.552,
          "ebitda": 123788001280,
          "totalDebt": 109614997504,
          "quickRatio": 0.764,
          "currentRatio": 0.94,
          "totalRevenue": 385095008256,
          "debtToEquity": 176.349,
          "revenuePerShare": 24.116,
          "returnOnAssets": 0.20559,
          "returnOnEquity": 1.4560499,
          "grossProfits": 170782000000,
          "freeCashflow": 83796623360,
          "operatingCashflow": 109583998976,
          "earningsGrowth": 0,
          "revenueGrowth": -0.025,
          "grossMargins": 0.43181,
          "ebitdaMargins": 0.32145,
          "operatingMargins": 0.29163,
          "profitMargins": 0.24493,
          "financialCurrency": "USD"
        }
      }
    ],
    "error": null
  }
  }
"""

NOT_FOUND_JSON_RESPONSE = """
{"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"Quote not found for ticker symbol: 333"}}}
"""

PARTIAL_JSON_RESPONSE = """
{
  "quoteSummary": {
    "result": [
      {
        "summaryProfile": {
          "address1": "One Apple Park Way",
          "city": "Cupertino",
          "state": "CA",
          "zip": "95014",
          "country": "United States",
          "phone": "408 996 1010",
          "website": "https://www.apple.com",
          "industry": "Consumer Electronics",
          "industryDisp": "Consumer Electronics",
          "sector": "Technology",
          "companyOfficers": [],
          "maxAge": 86400
        },
        "financialData": {
          "maxAge": 86400,
          "recommendationKey": "none",
          "currentPrice": 180.95,
          "targetHighPrice": 209,
          "targetLowPrice": 118,
          "targetMeanPrice": 180.27,
          "targetMedianPrice": 184.43,
          "recommendationMean": 2,
          "numberOfAnalystOpinions": 38,
          "totalCash": 55872000000,
          "grossMargins": 0.43181,
          "ebitdaMargins": 0.32145,
          "profitMargins": 0.24493,
          "financialCurrency": "USD"
        }
      }
    ],
    "error": null
  }
  }
"""

MISSING_FINANCIAL_DATA_JSON_RESPONSE = """
{
  "quoteSummary": {
    "result": [
      {
        "summaryProfile": {
          "address1": "One Apple Park Way",
          "city": "Cupertino",
          "state": "CA",
          "zip": "95014",
          "country": "United States",
          "phone": "408 996 1010",
          "website": "https://www.apple.com",
          "industry": "Consumer Electronics",
          "industryDisp": "Consumer Electronics",
          "sector": "Technology",
          "companyOfficers": [],
          "maxAge": 86400
        }
      }
    ],
    "error": null
  }
  }
"""

UNEXPECTED_JSON_RESPONSE = """
{"something": "something"}
"""
