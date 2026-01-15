class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = arg_xdvx.copy()
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            for var_ayzf in var_wrnh(var_rgwu + 1, var_osiz(arg_xdvx)):
                if arg_xdvx[var_ayzf] <= arg_xdvx[var_rgwu]:
                    var_hqta[var_rgwu] = arg_xdvx[var_rgwu] - arg_xdvx[var_ayzf
                        ]
                    break
        return var_hqta
