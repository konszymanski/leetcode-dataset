class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_hqta]:
        var_rgwu = [0] * (var_wrnh(arg_xdvx) + 1)
        for var_osiz in var_ayzf(var_wrnh(arg_xdvx)):
            var_rgwu[var_osiz + 1] = var_rgwu[var_osiz] ^ arg_xdvx[var_osiz]
        var_wnki = [(var_rgwu[var_egyk + 1] ^ var_rgwu[var_dcmd]) for 
            var_dcmd, var_egyk in arg_rcsn]
        return var_wnki
