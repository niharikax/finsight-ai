# import yfinance
# yfinance lets us access stock market data from yahoo finance
import yfinance as yf


# function that gets stock information for a company
def get_stock_data(ticker):

    # create a stock object using the ticker symbol
    stock = yf.Ticker(ticker)

    # download company information
    info = stock.info

    # return company information
    return {
        "company": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "sector": info.get("sector")
    }