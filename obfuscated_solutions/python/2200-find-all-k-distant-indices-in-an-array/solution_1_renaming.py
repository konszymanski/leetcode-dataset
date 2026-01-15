class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_hqta[var_rgwu]:
        var_wrnh = []
        var_osiz = var_ayzf(arg_xdvx)
        for var_wnki in var_egyk(var_osiz):
            for var_dcmd in var_egyk(var_osiz):
                if arg_xdvx[var_dcmd] == arg_rcsn and var_llti(var_wnki -
                    var_dcmd) <= arg_bacg:
                    var_wrnh.append(var_wnki)
                    break
        return var_wrnh
