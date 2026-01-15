class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_ihhe.total_sum = var_rgwu(arg_xdvx)
        var_wrnh = [([var_osiz('-inf')] * (2 * arg_ihhe.total_sum + 1)) for
            var_ayzf in var_wnki(var_egyk(arg_xdvx))]
        return arg_ihhe.calculate_ways(arg_xdvx, 0, 0, arg_rcsn, var_wrnh)

    def func_dcmd(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_llti:
        var_hqta, arg_zbxo: var_hqta, arg_rcsn: var_hqta, var_wrnh:
        var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        if arg_llti == var_egyk(arg_xdvx):
            return 1 if arg_zbxo == arg_rcsn else 0
        else:
            if var_wrnh[arg_llti][arg_zbxo + arg_ihhe.total_sum] != var_osiz(
                '-inf'):
                return var_wrnh[arg_llti][arg_zbxo + arg_ihhe.total_sum]
            var_rdmc = arg_ihhe.calculate_ways(arg_xdvx, arg_llti + 1, 
                arg_zbxo + arg_xdvx[arg_llti], arg_rcsn, var_wrnh)
            var_rjut = arg_ihhe.calculate_ways(arg_xdvx, arg_llti + 1, 
                arg_zbxo - arg_xdvx[arg_llti], arg_rcsn, var_wrnh)
            var_wrnh[arg_llti][arg_zbxo + arg_ihhe.total_sum
                ] = var_rdmc + var_rjut
            return var_wrnh[arg_llti][arg_zbxo + arg_ihhe.total_sum]
