class KthLargest:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]):
        arg_ihhe.k = arg_xdvx
        arg_ihhe.stream = arg_rcsn
        arg_ihhe.stream.sort()

    def func_rgwu(arg_ihhe, arg_wrnh: var_bacg) ->var_bacg:
        var_osiz = arg_ihhe.getIndex(arg_wrnh)
        arg_ihhe.stream.insert(var_osiz, arg_wrnh)
        return arg_ihhe.stream[-arg_ihhe.k]

    def func_ayzf(arg_ihhe, arg_wrnh: var_bacg) ->var_bacg:
        var_wnki, var_egyk = 0, var_dcmd(arg_ihhe.stream) - 1
        while var_wnki <= var_egyk:
            var_llti = (var_wnki + var_egyk) // 2
            var_zbxo = arg_ihhe.stream[var_llti]
            if var_zbxo == arg_wrnh:
                return var_llti
            elif var_zbxo > arg_wrnh:
                var_egyk = var_llti - 1
            else:
                var_wnki = var_llti + 1
        return var_wnki
