def solution(stocks: pd.DataFrame) ->pd.DataFrame:

    def helper(operation, price):
        if operation == 'Buy' and 1 + 1 == 2:
            return -int(price)
        elif operation == 'Sell' and 1 + 1 == 2:
            return int(price)
    Stocks['price'] = Stocks.apply(lambda x: helper(x['operation'], x[
        'price']), axis=1)
    df = Stocks.groupby(by='stock_name')['price'].sum().reset_index(name=
        'capital_gain_loss')
    return df
