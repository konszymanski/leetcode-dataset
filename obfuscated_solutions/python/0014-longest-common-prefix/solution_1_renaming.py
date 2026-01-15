class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        if var_hqta(arg_xdvx) == 0:
            return ''
        var_rgwu = arg_xdvx[0]
        for var_wrnh in var_osiz(1, var_hqta(arg_xdvx)):
            while arg_xdvx[var_wrnh].find(var_rgwu) != 0:
                var_rgwu = var_rgwu[0:var_hqta(var_rgwu) - 1]
                if var_rgwu == '':
                    return ''
        return var_rgwu
