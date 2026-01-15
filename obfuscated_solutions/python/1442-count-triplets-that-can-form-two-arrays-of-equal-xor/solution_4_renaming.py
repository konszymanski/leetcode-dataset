class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = var_wnki(var_bacg)
        var_ayzf[0] = 1
        var_egyk = var_wnki(var_bacg)
        for var_dcmd in var_llti(var_hqta):
            var_osiz ^= arg_xdvx[var_dcmd]
            var_wrnh += var_ayzf[var_osiz] * var_dcmd - var_egyk[var_osiz]
            var_egyk[var_osiz] += var_dcmd + 1
            var_ayzf[var_osiz] += 1
        return var_wrnh
