# prediction_agent.py
import pandas as pd
import pickle
from fetch_live_data import fetch_bitcoin_data  # ✅ Import live fetch function

# Load model
with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# ✅ Fetch live data instead of reading CSV
df = fetch_bitcoin_data()

df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
df.dropna(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["Close"] = pd.to_numeric(df["Close"], errors='coerce')
df["Volume"] = pd.to_numeric(df["Volume"], errors='coerce')
df.dropna(inplace=True)

# Create feature set for next day prediction
df["Days"] = (df["Date"] - df["Date"].min()).dt.days
last_row = df.iloc[-1]

next_day_data = pd.DataFrame([{
    "Days": last_row["Days"] + 1,
    "Open": last_row["Open"],
    "High": last_row["High"],
    "Low": last_row["Low"],
    "Volume": last_row["Volume"]
}])

# Predict next day's closing price
predicted_price = model.predict(next_day_data)[0]
print(f"Predicted price for next day: ${predicted_price:.2f}")
def get_prediction():
    return float(predicted_price)

if __name__ == "__main__":
    print(f"Predicted price for next day: ${predicted_price:.2f}")
