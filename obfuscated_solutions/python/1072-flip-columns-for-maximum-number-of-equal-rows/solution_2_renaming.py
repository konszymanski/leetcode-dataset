class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = {}
        for var_rgwu in arg_xdvx:
            var_wrnh = ''.join('T' if var_osiz == var_rgwu[0] else 'F' for
                var_osiz in var_rgwu)
            var_hqta[var_wrnh] = var_hqta.get(var_wrnh, 0) + 1
        return var_ayzf(var_hqta.values(), default=0)
