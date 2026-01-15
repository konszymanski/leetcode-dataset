class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_wnki:
        var_hqta = [False] * (24 * 60)
        for var_rgwu in arg_xdvx:
            var_wrnh, var_osiz = var_ayzf(var_wnki, var_rgwu.split(':'))
            var_egyk = var_wrnh * 60 + var_osiz
            if var_hqta[var_egyk]:
                return 0
            var_hqta[var_egyk] = True
        var_dcmd = var_llti('inf')
        var_zbxo = var_llti('inf')
        var_rdmc = var_llti('inf')
        var_rjut = var_llti('inf')
        for var_lsgw in var_cbvh(24 * 60):
            if var_hqta[var_lsgw]:
                if var_dcmd != var_llti('inf'):
                    var_rjut = var_yjch(var_rjut, var_lsgw - var_dcmd)
                var_dcmd = var_lsgw
                if var_zbxo == var_llti('inf'):
                    var_zbxo = var_lsgw
                var_rdmc = var_lsgw
        return var_yjch(var_rjut, 24 * 60 - var_rdmc + var_zbxo)
