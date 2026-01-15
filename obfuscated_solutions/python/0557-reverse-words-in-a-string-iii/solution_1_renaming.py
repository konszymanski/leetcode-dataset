class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = []
        var_hqta = -1
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            if var_rgwu == var_osiz(arg_xdvx) - 1 or arg_xdvx[var_rgwu] == ' ':
                var_ayzf = var_rgwu if var_rgwu == var_osiz(arg_xdvx
                    ) - 1 else var_rgwu - 1
                while var_ayzf > var_hqta:
                    var_bacg.append(arg_xdvx[var_ayzf])
                    var_ayzf -= 1
                if var_rgwu != var_osiz(arg_xdvx) - 1:
                    var_bacg.append(' ')
                var_hqta = var_rgwu
        return ''.join(var_bacg)
