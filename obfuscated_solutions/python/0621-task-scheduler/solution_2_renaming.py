class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_rgwu:
        var_wrnh = [0] * 26
        for var_osiz in arg_xdvx:
            var_wrnh[var_ayzf(var_osiz) - var_ayzf('A')] += 1
        var_wrnh.sort()
        var_wnki = var_wrnh[25] - 1
        var_egyk = var_wnki * arg_rcsn
        for var_dcmd in var_llti(24, -1, -1):
            var_egyk -= var_zbxo(var_wnki, var_wrnh[var_dcmd])
        return var_egyk + var_rdmc(arg_xdvx) if var_egyk > 0 else var_rdmc(
            arg_xdvx)
