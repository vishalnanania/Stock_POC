from alpha_vantage.timeseries import TimeSeries

API_KEY = "8YKR5WV7H31IUEBB"

class AVConnection:
    def __init__(self, api_key=API_KEY):
        self.ts = TimeSeries(key=api_key)

    def get_daily_stock_data(self, symbol, date):
        data, _ = self.ts.get_daily(symbol=symbol, outputsize='full')
        return data.get(date)