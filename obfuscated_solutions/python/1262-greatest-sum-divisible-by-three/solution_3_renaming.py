class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = [0, -var_rgwu('inf'), -var_rgwu('inf')]
        for var_wrnh in arg_xdvx:
            var_osiz = var_hqta[:]
            for var_ayzf in var_wnki(3):
                var_osiz[(var_ayzf + var_wrnh % 3) % 3] = var_egyk(var_osiz
                    [(var_ayzf + var_wrnh % 3) % 3], var_hqta[var_ayzf] +
                    var_wrnh)
            var_hqta = var_osiz
        return var_hqta[0]
