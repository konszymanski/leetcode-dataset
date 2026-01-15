class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = {var_rgwu: [] for var_rgwu in var_wrnh(var_osiz(arg_xdvx))}
        for var_ayzf, var_wnki in var_egyk(arg_xdvx):
            var_hqta[var_wnki].append(var_ayzf)
        var_dcmd = 1
        for var_wnki in var_hqta.keys():
            for var_llti in var_hqta[var_wnki]:
                arg_xdvx[var_llti] = var_dcmd
            var_dcmd += 1
        return arg_xdvx
