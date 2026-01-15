class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = var_osiz(arg_xdvx) - 1
        var_ayzf = 0
        arg_xdvx.sort()
        while var_rgwu <= var_wrnh:
            if arg_rcsn >= arg_xdvx[var_rgwu]:
                var_ayzf += 1
                arg_rcsn -= arg_xdvx[var_rgwu]
                var_rgwu += 1
            elif var_rgwu < var_wrnh and var_ayzf > 0:
                var_ayzf -= 1
                arg_rcsn += arg_xdvx[var_wrnh]
                var_wrnh -= 1
            else:
                return var_ayzf
        return var_ayzf
