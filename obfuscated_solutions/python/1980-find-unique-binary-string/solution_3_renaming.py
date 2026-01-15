class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu()
        for var_wrnh in arg_xdvx:
            var_hqta.add(var_osiz(var_wrnh, 2))
        var_ayzf = var_osiz(arg_xdvx[0], 2)
        var_wnki = var_egyk(arg_xdvx)
        while var_ayzf in var_hqta:
            var_ayzf = var_dcmd.randrange(0, 2 ** var_wnki)
        var_llti = var_zbxo(var_ayzf)[2:]
        return '0' * (var_wnki - var_egyk(var_llti)) + var_llti
