class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [var_wrnh for var_wrnh in arg_xdvx]
        var_osiz = 0
        var_ayzf = var_bacg - 1
        while var_osiz <= var_ayzf:
            if var_rgwu[var_osiz] == '1':
                var_osiz += 1
            if var_rgwu[var_ayzf] == '0':
                var_ayzf -= 1
            if var_osiz <= var_ayzf and var_rgwu[var_osiz] == '0' and var_rgwu[
                var_ayzf] == '1':
                var_rgwu[var_osiz] = '1'
                var_rgwu[var_ayzf] = '0'
        var_rgwu[var_osiz - 1] = '0'
        var_rgwu[var_bacg - 1] = '1'
        return ''.join(var_rgwu)
