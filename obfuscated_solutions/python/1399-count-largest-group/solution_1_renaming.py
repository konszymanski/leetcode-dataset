class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta.Counter()
        for var_rgwu in var_wrnh(1, arg_xdvx + 1):
            var_osiz = var_ayzf([var_rcsn(var_wnki) for var_wnki in
                var_egyk(var_rgwu)])
            var_bacg[var_osiz] += 1
        var_dcmd = var_llti(var_bacg.values())
        var_zbxo = var_ayzf(1 for var_rdmc in var_bacg.values() if var_rdmc ==
            var_dcmd)
        return var_zbxo
