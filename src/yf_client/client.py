import random
import requests
from yf_client.model.yahoo_response import YahooFinanceResponse
from typing import Optional

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 ",
    "Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ",
    "Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 ",
    "Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 ",
    "Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
]

BASE_REQUEST_HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://finance.yahoo.com",
    "referer": "https://finance.yahoo.com",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
}


class YahooClient:
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers = BASE_REQUEST_HEADERS.copy()
        self.session.headers["User-Agent"] = random.choice(USER_AGENTS)
        
        try:
            # set cookie on the session
            self.session.get(url="https://fc.yahoo.com", timeout=self.timeout)
            
            # get crumb required for further calls
            crumb_url = "https://query2.finance.yahoo.com/v1/test/getcrumb"
            response = self.session.get(url=crumb_url, timeout=self.timeout)
            
            if response.status_code == 429:
                raise Exception("Cannot initialize client. Rate limit exceeded - too many requests.")
            
            self.crumb = response.text
        except requests.RequestException as e:
            print(f"Failed to initialize client: {str(e)}")
            raise

    def get_one(self, ticker: str) -> Optional[YahooFinanceResponse]:
            if not ticker or not isinstance(ticker, str):
                raise ValueError("Ticker must be a non-empty string")
            
            try:
                url = self.__get_url(ticker, self.crumb)
                response = self.session.get(url=url, timeout=self.timeout)
            
                if response.status_code == 200:
                    return YahooFinanceResponse.from_json_response(response.json())

                print(
                    f"Error fetching data for {ticker}. Status code: {response.status_code}, "
                    f"Response: {response.text}"
                )
                return None
            
            except requests.RequestException as e:
                print(f"Request failed for ticker {ticker}: {str(e)}")
                return None
        
    @staticmethod
    def __get_url(ticker: str, crumb: str) -> str:
        return f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=financialData,summaryProfile,summaryDetail&formatted=false&lang=en-US&region=US&corsDomain=finance.yahoo.com&crumb={crumb}"
    
    def __enter__(self):
        return self

    def __exit__(self, _, __, ___):
        self.session.close()
    


