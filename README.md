## Stock data enricher

Small library to fetch financial data tied to a stock ticker 

### Usage 
Import one of the methods exposed by [Main](src/main.py) file. 

### What data is returned
Company Information:
- Industry
- Website
- Country
- Sector
- Business Summary

Financial Metrics:
- Market Capitalization
- Financial Currency
- Analyst Recommendations
  - Recommendation Key
  - Mean Recommendation
  - Number of Analyst Opinions

Balance Sheet & Cash Flow:
- Total Cash
- Total Cash Per Share
- EBITDA
- Total Debt
- Quick Ratio
- Current Ratio
- Total Revenue
- Debt to Equity Ratio
- Revenue Per Share
- Free Cash Flow
- Operating Cash Flow

Performance Metrics:
- Return on Assets (ROA)
- Return on Equity (ROE)
- Gross Profits
- Earnings Growth
- Revenue Growth

Margin Analysis:
- Gross Margins
- EBITDA Margins
- Operating Margins
- Profit Margins

Additional Information:
- Company Founding Date

For a complete list of all data fields returned by the library, see [EnrichedStockData](src/app/model/enriched_stock_data.py).

## Example 
Given ticker MSFT
```json
{
  "ticker": "MSFT",
  "industry": "Software - Infrastructure",
  "website": "https://www.microsoft.com",
  "country": "United States",
  "sector": "Technology",
  "summary": "Microsoft Corporation develops and supports software, services, devices and solutions worldwide. The Productivity and Business Processes segment offers office, exchange, SharePoint, Microsoft Teams, office 365 Security and Compliance, Microsoft viva, and Microsoft 365 copilot; and office consumer services, such as Microsoft 365 consumer subscriptions, Office licensed on-premises, and other office services. This segment also provides LinkedIn; and dynamics business solutions, including Dynamics 365, a set of intelligent, cloud-based applications across ERP, CRM, power apps, and power automate; and on-premises ERP and CRM applications. The Intelligent Cloud segment offers server products and cloud services, such as azure and other cloud services; SQL and windows server, visual studio, system center, and related client access licenses, as well as nuance and GitHub; and enterprise services including enterprise support services, industry solutions, and nuance professional services. The More Personal Computing segment offers Windows, including windows OEM licensing and other non-volume licensing of the Windows operating system; Windows commercial comprising volume licensing of the Windows operating system, windows cloud services, and other Windows commercial offerings; patent licensing; and windows Internet of Things; and devices, such as surface, HoloLens, and PC accessories. Additionally, this segment provides gaming, which includes Xbox hardware and content, and first- and third-party content; Xbox game pass and other subscriptions, cloud gaming, advertising, third-party disc royalties, and other cloud services; and search and news advertising, which includes Bing, Microsoft News and Edge, and third-party affiliates. The company sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online, and retail stores. The company was founded in 1975 and is headquartered in Redmond, Washington.",
  "marketCap": 3189786542080,
  "financialCurrency": "USD",
  "recommendationKey": "strong_buy",
  "recommendationMean": 1.41379,
  "numberOfAnalystOpinions": 50,
  "totalCash": 78429003776,
  "totalCashPerShare": 10.549,
  "ebitda": 136551997440,
  "totalDebt": 96838000640,
  "quickRatio": 1.163,
  "currentRatio": 1.301,
  "totalRevenue": 254189993984,
  "debtToEquity": 33.657,
  "revenuePerShare": 34.202,
  "returnOnAssets": 0.14592,
  "returnOnEquity": 0.35604,
  "grossProfits": 176278994944,
  "freeCashflow": 61280874496,
  "operatingCashflow": 122144997376,
  "earningsGrowth": 0.104,
  "revenueGrowth": 0.16,
  "grossMargins": 0.69348997,
  "ebitdaMargins": 0.53720003,
  "operatingMargins": 0.46583998,
  "profitMargins": 0.35608003,
  "foundingDate": 1975
}
```