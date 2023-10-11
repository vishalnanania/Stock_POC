from av_connection import AVConnection

def get_lowest_highest(symbol, n, low):
    av_conn = AVConnection();
    try:
        recent_data = av_conn.get_recent_stock_data(symbol, n)
        if not recent_data:
             return {f"No data available for {symbol} in period {n}"}
        
        if low:
            price = min(float(data_point[1]['3. low']) for data_point in recent_data)
        else:
            price = max(float(data_point[1]['2. high']) for data_point in recent_data)   
        return price
    except Exception as e:
        return {f"Error occured while get details for {symbol} in period {n}"}

if __name__ == "__main__":
    print(get_lowest_highest('AAPL', 5, True)) # get real data for low
    print(get_lowest_highest('AAPL', 5, False)) # get real data for high
    print(get_lowest_highest('APPL', 5, True)) # Exception case low
    print(get_lowest_highest('APPL', 5, False)) # Exception case high