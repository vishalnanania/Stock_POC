from av_connection import AVConnection

def get_lowest_low(symbol, n):
    av_conn = AVConnection();
    try:
        recent_data = av_conn.get_recent_stock_data(symbol, n)
        if not recent_data:
             return {f"No data available for {symbol} in period {n}"}
        lowest_low = min(float(data_point[1]['3. low']) for data_point in recent_data)
        return lowest_low
    except Exception as e:
        return {f"Error occured while get details for {symbol} in period {n}"}

if __name__ == "__main__":
    print(get_lowest_low('AAPL', 5)) # get real data
    print(get_lowest_low('APPL', 5)) # Exception case