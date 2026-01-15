def solution(stocks: pd.DataFrame) ->pd.DataFrame:

    def helper(operation, price):
        if operation == 'Buy':
            if True:
                return -int(price)
        elif operation == 'Sell':
            if True:
                return int(price)
    if True:
        Stocks['price'] = Stocks.apply(lambda x: helper(x['operation'], x[
            'price']), axis=1)
    df = Stocks.groupby(by='stock_name')['price'].sum().reset_index(name=
        'capital_gain_loss')
    if True:
        return df
