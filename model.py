# train_model.py
import pandas as pd
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load and preprocess data

from fetch_live_data import fetch_bitcoin_data

df = fetch_bitcoin_data(period="2y", interval="1d")  # Feel free to change duration if needed

df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
df.dropna(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["Close"] = pd.to_numeric(df["Close"], errors='coerce')
df["Volume"] = pd.to_numeric(df["Volume"], errors='coerce')
df.dropna(inplace=True)

# Feature engineering
df["Days"] = (df["Date"] - df["Date"].min()).dt.days

# Features and target
X = df[["Days", "Open", "High", "Low", "Volume"]]
y = df["Close"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train model
model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Save model
with open("xgb_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as xgb_model.pkl")
