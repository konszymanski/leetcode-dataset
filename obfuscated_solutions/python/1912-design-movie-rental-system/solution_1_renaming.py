class MovieRentingSystem:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]):
        arg_ihhe.t_price = var_rgwu()
        arg_ihhe.t_valid = var_wrnh(var_osiz.SortedList)
        arg_ihhe.t_rent = var_osiz.SortedList()
        for var_ayzf, var_wnki, var_egyk in arg_rcsn:
            arg_ihhe.t_price[var_ayzf, var_wnki] = var_egyk
            arg_ihhe.t_valid[var_wnki].add((var_egyk, var_ayzf))

    def func_dcmd(arg_ihhe, var_wnki: var_bacg) ->var_hqta[var_bacg]:
        var_llti = arg_ihhe.t_valid
        if var_wnki not in var_llti:
            return []
        return [var_ayzf for var_egyk, var_ayzf in var_llti[var_wnki][:5]]

    def func_zbxo(arg_ihhe, var_ayzf: var_bacg, var_wnki: var_bacg) ->None:
        var_egyk = arg_ihhe.t_price[var_ayzf, var_wnki]
        arg_ihhe.t_valid[var_wnki].discard((var_egyk, var_ayzf))
        arg_ihhe.t_rent.add((var_egyk, var_ayzf, var_wnki))

    def func_rdmc(arg_ihhe, var_ayzf: var_bacg, var_wnki: var_bacg) ->None:
        var_egyk = arg_ihhe.t_price[var_ayzf, var_wnki]
        arg_ihhe.t_valid[var_wnki].add((var_egyk, var_ayzf))
        arg_ihhe.t_rent.discard((var_egyk, var_ayzf, var_wnki))

    def func_rjut(arg_ihhe) ->var_hqta[var_hqta[var_bacg]]:
        return [(var_ayzf, var_wnki) for var_egyk, var_ayzf, var_wnki in
            arg_ihhe.t_rent[:5]]
