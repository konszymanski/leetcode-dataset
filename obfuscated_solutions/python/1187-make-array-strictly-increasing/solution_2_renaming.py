class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = {(-1): 0}
        arg_rcsn.sort()
        var_wrnh = var_osiz(arg_rcsn)
        for var_ayzf in var_wnki(var_osiz(arg_xdvx)):
            var_egyk = var_dcmd.defaultdict(lambda : var_llti('inf'))
            for var_zbxo in var_rgwu:
                if arg_xdvx[var_ayzf] > var_zbxo:
                    var_egyk[arg_xdvx[var_ayzf]] = var_rdmc(var_egyk[
                        arg_xdvx[var_ayzf]], var_rgwu[var_zbxo])
                var_rjut = var_lsgw.bisect_right(arg_rcsn, var_zbxo)
                if var_rjut < var_wrnh:
                    var_egyk[arg_rcsn[var_rjut]] = var_rdmc(var_egyk[
                        arg_rcsn[var_rjut]], 1 + var_rgwu[var_zbxo])
            var_rgwu = var_egyk
        return var_rdmc(var_rgwu.values()) if var_rgwu else -1
