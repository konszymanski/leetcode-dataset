class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = 0
        var_wnki = {}
        while var_ayzf < var_egyk(arg_xdvx):
            var_dcmd = arg_xdvx[var_ayzf]
            var_llti = var_wnki.get(var_dcmd, -1)
            while var_osiz <= var_llti or var_ayzf - var_osiz + 1 > arg_rcsn:
                var_wrnh -= arg_xdvx[var_osiz]
                var_osiz += 1
            var_wnki[var_dcmd] = var_ayzf
            var_wrnh += arg_xdvx[var_ayzf]
            if var_ayzf - var_osiz + 1 == arg_rcsn:
                var_rgwu = var_zbxo(var_rgwu, var_wrnh)
            var_ayzf += 1
        return var_rgwu
