class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = arg_xdvx.copy()
        var_rgwu = var_wrnh()
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            while var_rgwu and arg_xdvx[var_rgwu[-1]] >= arg_xdvx[var_osiz]:
                var_hqta[var_rgwu.pop()] -= arg_xdvx[var_osiz]
            var_rgwu.append(var_osiz)
        return var_hqta
