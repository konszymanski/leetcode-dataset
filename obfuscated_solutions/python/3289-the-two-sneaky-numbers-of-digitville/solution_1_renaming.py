class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = []
        var_rgwu = {}
        for var_wrnh in arg_xdvx:
            var_rgwu[var_wrnh] = var_rgwu.get(var_wrnh, 0) + 1
            if var_rgwu[var_wrnh] == 2:
                var_hqta.append(var_wrnh)
        return var_hqta
