from typing import Optional
from yf_client.client import YahooClient
from app.model.enriched_stock_data import EnrichedStockData

import json

def get_one(ticker: str) -> Optional[EnrichedStockData]:
    with YahooClient() as client:
        response = client.get_one(ticker)
        
        if not response:
            return None

        return EnrichedStockData.from_yahoo_finance_response(ticker, response)


def get_multiple(tickers: list[str]) -> list[EnrichedStockData]:
    with YahooClient() as client:
        results = []
        
        for ticker in tickers:
            response = client.get_one(ticker)
            if response:
                results.append(EnrichedStockData.from_yahoo_finance_response(ticker, response))
                
        return results

if __name__ == "__main__":
    # example usage
    test_tickers = ["AAPL", "MSFT"]
    results = get_multiple(test_tickers)

    for stock in results:
        print(json.dumps(stock.__dict__, indent=2))
