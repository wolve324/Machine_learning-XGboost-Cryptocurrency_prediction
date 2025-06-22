Bitcoin Price Prediction with Live Data
This project predicts the next day's Bitcoin closing price using XGBoost regression and real-time market data. It also features a clean Flask web interface to display live predictions.

    
 Features:
Real-time Bitcoin data fetch using yfinance
Trained using XGBoost Regressor on historical data
Flask-powered prediction UI
Responsive HTML+CSS frontend
Clean modular architecture

Installation & Running Locally: 
1. Clone the repository
git clone https://github.com/yourusername/bitcoin-price-prediction.git
cd "Bitcoin project"
2. Create virtual environment (optional but recommended)
     python -m venv venv
     venv\Scripts\activate    # On Windows
3. Install dependencies
     pip install -r requirements.txt
4. Run the web app
     python app.py
   
Visit http://127.0.0.1:5000 in your browser.




 Model Info::

 
Algorithm: XGBoost Regressor

Input Features: Day number, Open, High, Low, Volume

Target Variable: Next day's Close price




Need deployment help? Just ask!
