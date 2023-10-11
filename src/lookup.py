from av_connection import AVConnection

def lookup(symbol, date):
    av_conn = AVConnection();
    try:
        data = av_conn.get_daily_stock_data(symbol, date)
        if data:
            return data
        else: 
            return {f"No data available for {symbol} on {date}"}
    except Exception as e:
        return {f"Error occured while get details for {symbol} on {date}"}

if __name__ == "__main__":
    print(lookup('AAPL', '2023-10-06')) # get real data
    print(lookup('AAPL', '2024-10-06')) # get no data
    print(lookup('APPL', '2023-10-06')) # Exception case