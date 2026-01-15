class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = []
        var_wrnh = [0] * var_bacg
        for var_osiz in var_ayzf(var_bacg):
            if arg_xdvx[var_osiz] == '(':
                var_rgwu.append(var_osiz)
            if arg_xdvx[var_osiz] == ')':
                var_wnki = var_rgwu.pop()
                var_wrnh[var_osiz] = var_wnki
                var_wrnh[var_wnki] = var_osiz
        var_egyk = []
        var_dcmd = 0
        var_llti = 1
        while var_dcmd < var_bacg:
            if arg_xdvx[var_dcmd] == '(' or arg_xdvx[var_dcmd] == ')':
                var_dcmd = var_wrnh[var_dcmd]
                var_llti = -var_llti
            else:
                var_egyk.append(arg_xdvx[var_dcmd])
            var_dcmd += var_llti
        return ''.join(var_egyk)
