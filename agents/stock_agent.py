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

        # company name
        "company": info.get("longName"),

        # current stock price
        "price": info.get("currentPrice"),

        # market value of the company
        "market_cap": info.get("marketCap"),

        # price-to-earnings ratio
        "pe_ratio": info.get("trailingPE"),

        # business sector
        "sector": info.get("sector"),

        # highest stock price in last 52 weeks
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),

        # lowest stock price in last 52 weeks
        "fifty_two_week_low": info.get("fiftyTwoWeekLow"),

        # profit margin
        "profit_margin": info.get("profitMargins"),

        # dividend yield
        "dividend_yield": info.get("dividendYield"),

        # stock volatility compared to market
        "beta": info.get("beta"),

        # analyst recommendation
        "recommendation": info.get("recommendationKey")
    }