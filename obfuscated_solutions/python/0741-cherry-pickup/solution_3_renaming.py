class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = [([var_wrnh('-inf')] * var_bacg) for var_osiz in
            var_ayzf(var_bacg)]
        var_rgwu[0][0] = arg_rcsn[0][0]
        for var_wnki in var_ayzf(1, 2 * var_bacg - 1):
            var_egyk = [([var_wrnh('-inf')] * var_bacg) for var_osiz in
                var_ayzf(var_bacg)]
            for var_dcmd in var_ayzf(var_llti(0, var_wnki - (var_bacg - 1)),
                var_zbxo(var_bacg - 1, var_wnki) + 1):
                for var_rdmc in var_ayzf(var_llti(0, var_wnki - (var_bacg -
                    1)), var_zbxo(var_bacg - 1, var_wnki) + 1):
                    if arg_rcsn[var_dcmd][var_wnki - var_dcmd
                        ] == -1 or arg_rcsn[var_rdmc][var_wnki - var_rdmc
                        ] == -1:
                        continue
                    var_rjut = arg_rcsn[var_dcmd][var_wnki - var_dcmd]
                    if var_dcmd != var_rdmc:
                        var_rjut += arg_rcsn[var_rdmc][var_wnki - var_rdmc]
                    var_egyk[var_dcmd][var_rdmc] = var_llti(var_rgwu[
                        var_lsgw][var_cbvh] + var_rjut for var_lsgw in (
                        var_dcmd - 1, var_dcmd) for var_cbvh in (var_rdmc -
                        1, var_rdmc) if var_lsgw >= 0 and var_cbvh >= 0)
            var_rgwu = var_egyk
        return var_llti(0, var_rgwu[var_bacg - 1][var_bacg - 1])
