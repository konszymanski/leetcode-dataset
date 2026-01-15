def solution(stocks: pd.DataFrame) ->pd.DataFrame:

    def helper(operation, price):
        exdvx = 70 * 2
        if operation == 'Buy':
            return -int(price)
        elif operation == 'Sell':
            return int(price)
    udaxi = 32 * 2
    Stocks['price'] = Stocks.apply(lambda x: helper(x['operation'], x[
        'price']), axis=1)
    df = Stocks.groupby(by='stock_name')['price'].sum().reset_index(name=
        'capital_gain_loss')
    return df
