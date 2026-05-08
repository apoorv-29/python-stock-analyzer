import yfinance as yf
import matplotlib.pyplot as plt

# User input
ticker = input("Enter stock ticker: ")

# Download data
data = yf.download(ticker, period="6mo")
stock= yf.Ticker(ticker)
print(stock.info["longName"])

# Latest price
latest_price = data["Close"].iloc[-1].item()

# Highest and lowest prices
highest_price = data["High"].max() .item()
lowest_price = data["Low"].min() .item()

# 20-day moving average
moving_average = data["Close"].rolling(window=20).mean() 

# Print analysis
print("\n------ STOCK ANALYSIS ------")
print(f"Ticker: {ticker}")

print(f"\nLatest Closing Price: {latest_price:.2f}")
print(f"Highest Price (6mo): {highest_price:.2f}")
print(f"Lowest Price (6mo): {lowest_price:.2f}")

# Trend logic
if latest_price > moving_average.iloc[-1] .item():
    print("\nTrend: Bullish 📈")
else:
    print("\nTrend: Bearish 📉")

# Plot graph
plt.figure(figsize=(10,5))

plt.plot(data["Close"], label="Closing Price")
plt.plot(moving_average, label="20-Day Moving Average")

plt.title(f"{ticker} Stock Analysis")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()

plt.show()
