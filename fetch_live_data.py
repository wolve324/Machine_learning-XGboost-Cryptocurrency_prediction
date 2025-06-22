import yfinance as yf
import pandas as pd

def fetch_bitcoin_data(period="1y", interval="1d", save_path="BTC-USD.csv"):
    # Download historical BTC-USD data
    btc_data = yf.download("BTC-USD", period=period, interval=interval)
    btc_data.reset_index(inplace=True)

    # Rename and format columns to match your model
    btc_data = btc_data[["Date", "Close", "High", "Low", "Open", "Volume"]]
    btc_data.dropna(inplace=True)

    # Save as CSV for reuse if needed
    btc_data.to_csv(save_path, index=False)
    print(f"[✔] Data saved to {save_path}")

    return btc_data

# Run when this script is executed directly
if __name__ == "__main__":
    fetch_bitcoin_data()
