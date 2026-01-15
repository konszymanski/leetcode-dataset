class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = {}
        var_rgwu = var_wrnh(var_osiz(arg_xdvx))
        var_ayzf = 1
        for var_wnki in var_rgwu:
            var_hqta[var_wnki] = var_ayzf
            var_ayzf += 1
        for var_egyk in var_dcmd(var_llti(arg_xdvx)):
            arg_xdvx[var_egyk] = var_hqta[arg_xdvx[var_egyk]]
        return arg_xdvx
