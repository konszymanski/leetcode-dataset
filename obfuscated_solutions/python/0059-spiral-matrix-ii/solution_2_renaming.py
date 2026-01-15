class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_lsgw[var_lsgw[var_rcsn]]:

        def func_bacg(arg_hqta):
            return arg_hqta // arg_xdvx, arg_hqta % arg_xdvx

        def func_rgwu(arg_wrnh, arg_osiz):
            return (arg_wrnh < 0 or arg_wrnh >= arg_xdvx or arg_osiz < 0 or
                arg_osiz >= arg_xdvx)
        var_ayzf = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        var_wnki = [([0] * arg_xdvx) for var_egyk in var_dcmd(arg_xdvx)]
        var_llti = 0
        arg_wrnh, arg_osiz = 0, 0
        for var_zbxo in var_dcmd(1, arg_xdvx * arg_xdvx + 1):
            var_wnki[arg_wrnh][arg_osiz] = var_zbxo
            var_rdmc, var_rjut = var_ayzf[var_llti]
            if func_rgwu(arg_wrnh + var_rdmc, arg_osiz + var_rjut) or var_wnki[
                arg_wrnh + var_rdmc][arg_osiz + var_rjut] > 0:
                var_llti = (var_llti + 1) % 4
            var_rdmc, var_rjut = var_ayzf[var_llti]
            arg_wrnh, arg_osiz = arg_wrnh + var_rdmc, arg_osiz + var_rjut
        return var_wnki
