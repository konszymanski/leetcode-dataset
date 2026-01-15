class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = {}
        arg_rcsn.sort()

        def func_wrnh(arg_osiz, arg_ayzf):
            if arg_osiz == var_wnki(arg_xdvx):
                return 0
            if (arg_osiz, arg_ayzf) in var_rgwu:
                return var_rgwu[arg_osiz, arg_ayzf]
            var_egyk = var_dcmd('inf')
            if arg_xdvx[arg_osiz] > arg_ayzf:
                var_egyk = func_wrnh(arg_osiz + 1, arg_xdvx[arg_osiz])
            var_llti = var_zbxo.bisect_right(arg_rcsn, arg_ayzf)
            if var_llti < var_wnki(arg_rcsn):
                var_egyk = var_rdmc(var_egyk, 1 + func_wrnh(arg_osiz + 1,
                    arg_rcsn[var_llti]))
            var_rgwu[arg_osiz, arg_ayzf] = var_egyk
            return var_egyk
        var_rjut = func_wrnh(0, -1)
        return var_rjut if var_rjut < var_dcmd('inf') else -1
