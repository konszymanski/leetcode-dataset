class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = {}
        arg_xdvx.sort()
        for var_rgwu in arg_xdvx:
            var_wrnh = var_bacg(var_rgwu ** 0.5)
            if var_wrnh * var_wrnh == var_rgwu and var_wrnh in var_hqta:
                var_hqta[var_rgwu] = var_hqta[var_wrnh] + 1
            else:
                var_hqta[var_rgwu] = 1
        var_osiz = var_ayzf(var_hqta.values(), default=0)
        return var_osiz if var_osiz > 1 else -1
