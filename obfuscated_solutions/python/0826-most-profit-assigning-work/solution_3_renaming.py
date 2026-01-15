class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_hqta[var_rgwu]) ->var_rgwu:
        var_wrnh = [(arg_xdvx[var_osiz], arg_rcsn[var_osiz]) for var_osiz in
            var_ayzf(var_wnki(arg_xdvx))]
        arg_bacg.sort()
        var_wrnh.sort()
        var_egyk, var_dcmd, var_llti = 0, 0, 0
        for var_zbxo in arg_bacg:
            while var_llti < var_wnki(arg_xdvx) and var_zbxo >= var_wrnh[
                var_llti][0]:
                var_dcmd = var_rdmc(var_dcmd, var_wrnh[var_llti][1])
                var_llti += 1
            var_egyk += var_dcmd
        return var_egyk
