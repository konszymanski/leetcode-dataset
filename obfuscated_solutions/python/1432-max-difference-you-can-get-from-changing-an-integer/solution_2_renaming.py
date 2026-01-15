class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg, var_hqta = var_rgwu(arg_xdvx), var_rgwu(arg_xdvx)
        for var_wrnh in var_hqta:
            if var_wrnh != '9':
                var_hqta = var_hqta.replace(var_wrnh, '9')
                break
        for var_osiz, var_wrnh in var_ayzf(var_bacg):
            if var_osiz == 0:
                if var_wrnh != '1':
                    var_bacg = var_bacg.replace(var_wrnh, '1')
                    break
            elif var_wrnh != '0' and var_wrnh != var_bacg[0]:
                var_bacg = var_bacg.replace(var_wrnh, '0')
                break
        return var_rcsn(var_hqta) - var_rcsn(var_bacg)
