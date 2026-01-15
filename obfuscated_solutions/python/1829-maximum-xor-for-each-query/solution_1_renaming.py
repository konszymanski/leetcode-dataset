class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = [0] * var_wrnh(arg_xdvx)
        var_rgwu[0] = arg_xdvx[0]
        for var_osiz in var_ayzf(1, var_wrnh(arg_xdvx)):
            var_rgwu[var_osiz] = var_rgwu[var_osiz - 1] ^ arg_xdvx[var_osiz]
        var_wnki = [0] * var_wrnh(arg_xdvx)
        var_egyk = (1 << arg_rcsn) - 1
        for var_osiz in var_ayzf(var_wrnh(arg_xdvx)):
            var_dcmd = var_rgwu[var_wrnh(var_rgwu) - 1 - var_osiz]
            var_wnki[var_osiz] = var_dcmd ^ var_egyk
        return var_wnki
