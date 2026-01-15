class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        return var_rcsn(arg_ihhe.find_smallest_number(arg_xdvx, 0, 0, 0))

    def func_bacg(arg_ihhe, arg_xdvx: var_rcsn, arg_hqta: var_osiz,
        arg_rgwu: var_osiz, arg_wrnh: var_osiz) ->var_osiz:
        if arg_hqta > var_ayzf(arg_xdvx):
            return arg_wrnh
        var_wnki = var_egyk('inf')
        var_dcmd = arg_wrnh % 10
        var_llti = arg_hqta == 0 or arg_xdvx[arg_hqta - 1] == 'I'
        for var_zbxo in var_rdmc(1, 10):
            if arg_rgwu & 1 << var_zbxo == 0 and (var_zbxo > var_dcmd
                ) == var_llti:
                var_wnki = var_rjut(var_wnki, arg_ihhe.find_smallest_number
                    (arg_xdvx, arg_hqta + 1, arg_rgwu | 1 << var_zbxo, 
                    arg_wrnh * 10 + var_zbxo))
        return var_wnki
