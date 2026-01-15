class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = []
        var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx) + 1):
            var_bacg.append(var_rcsn(1 + var_rgwu))
            if var_rgwu == var_osiz(arg_xdvx) or arg_xdvx[var_rgwu] == 'I':
                var_bacg[var_hqta:] = var_ayzf(var_bacg[var_hqta:])
                var_hqta = var_rgwu + 1
        return ''.join(var_bacg)
