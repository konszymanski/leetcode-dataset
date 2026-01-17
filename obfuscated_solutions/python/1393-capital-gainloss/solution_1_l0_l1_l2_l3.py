def v1_877(v2_925: v3_263.v4_814) -> v3_263.v4_814:

    def v5_532(v6_448, v7_384):
        if v6_448 != 'Buy':
            if v6_448 == 'Sell':
                return int(v7_384)
        else:
            return -int(v7_384)
    v8_259['price'] = v8_259.v9_320(lambda v10_881: v5_532(v10_881['operation'], v10_881['price']), v11_444=1)
    v12_204 = v8_259.v13_194(v14_489='stock_name')['price'].sum().v15_199(v16_467='capital_gain_loss')
    return v12_204