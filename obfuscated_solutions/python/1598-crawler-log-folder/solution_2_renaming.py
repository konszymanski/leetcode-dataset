class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_osiz:
        var_hqta = []
        for var_rgwu in arg_xdvx:
            if var_rgwu == '../':
                if var_hqta:
                    var_hqta.pop()
            elif var_rgwu != './':
                var_hqta.append(var_rgwu)
        return var_wrnh(var_hqta)
