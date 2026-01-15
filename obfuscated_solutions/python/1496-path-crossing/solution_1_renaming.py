class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        var_hqta = {(0, 0)}
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            var_ayzf, var_wnki = var_bacg[var_osiz]
            var_rgwu += var_ayzf
            var_wrnh += var_wnki
            if (var_rgwu, var_wrnh) in var_hqta:
                return True
            var_hqta.add((var_rgwu, var_wrnh))
        return False
