def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    def v5_381(v6_350, v7_328):
        if v6_350 == "Buy":
            return  - int(v7_328)
        elif v6_350 == "Sell":
            return int(v7_328)
    v8_242['price'] = v8_242.v9_854(lambda v10_204: v5_381(v10_204['operation'], v10_204['price']), v11_792=1)
    v12_858 = v8_242.v13_658(v14_189='stock_name')['price'].sum().v15_704(v16_532='capital_gain_loss')
    return v12_858
