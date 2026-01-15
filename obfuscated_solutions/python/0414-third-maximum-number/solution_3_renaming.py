from sortedcontainers import SortedSet


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu()
        for var_wrnh in arg_xdvx:
            if var_wrnh in var_hqta:
                continue
            if var_osiz(var_hqta) == 3:
                if var_hqta[0] < var_wrnh:
                    var_hqta.discard(var_hqta[0])
                    var_hqta.add(var_wrnh)
            else:
                var_hqta.add(var_wrnh)
        if var_osiz(var_hqta) == 3:
            return var_hqta[0]
        return var_hqta[-1]
