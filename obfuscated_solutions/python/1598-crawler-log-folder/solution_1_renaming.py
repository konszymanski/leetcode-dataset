class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_osiz:
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            if var_rgwu == '../':
                var_hqta = var_wrnh(0, var_hqta - 1)
            elif var_rgwu != './':
                var_hqta += 1
        return var_hqta
