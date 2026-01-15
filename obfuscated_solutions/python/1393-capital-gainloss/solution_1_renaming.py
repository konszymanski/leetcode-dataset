def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:

    def func_rcsn(arg_bacg, arg_hqta):
        if arg_bacg == 'Buy':
            return -var_rgwu(arg_hqta)
        elif arg_bacg == 'Sell':
            return var_rgwu(arg_hqta)
    var_wrnh['price'] = var_wrnh.apply(lambda x: func_rcsn(var_osiz[
        'operation'], var_osiz['price']), axis=1)
    var_ayzf = var_wrnh.groupby(by='stock_name')['price'].sum().reset_index(
        name='capital_gain_loss')
    return var_ayzf
