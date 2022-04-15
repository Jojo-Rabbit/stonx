from dotenv import load_dotenv
import os, requests, json

load_dotenv()

IEX_API_KEY = os.getenv("IEX_API_KEY")
ticker='AAPL'
api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={IEX_API_KEY}")
api = json.loads(api_request.content)
print(api)