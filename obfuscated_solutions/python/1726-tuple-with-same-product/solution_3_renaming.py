class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = {}
        var_wrnh = 0
        for var_osiz in var_ayzf(var_bacg):
            for var_wnki in var_ayzf(var_osiz + 1, var_bacg):
                var_egyk = arg_rcsn[var_osiz] * arg_rcsn[var_wnki]
                if var_egyk in var_rgwu:
                    var_rgwu[var_egyk] += 1
                else:
                    var_rgwu[var_egyk] = 1
        for var_dcmd in var_rgwu.values():
            var_llti = (var_dcmd - 1) * var_dcmd // 2
            var_wrnh += 8 * var_llti
        return var_wrnh
