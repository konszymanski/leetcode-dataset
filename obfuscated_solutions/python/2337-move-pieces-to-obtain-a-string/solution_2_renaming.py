class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_zbxo:
        var_hqta = []
        var_rgwu = []
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            if arg_xdvx[var_wrnh] != '_':
                var_hqta.append((arg_xdvx[var_wrnh], var_wrnh))
            if arg_rcsn[var_wrnh] != '_':
                var_rgwu.append((arg_rcsn[var_wrnh], var_wrnh))
        if var_ayzf(var_hqta) != var_ayzf(var_rgwu):
            return False
        while not var_ayzf(var_hqta) == 0:
            var_wnki, var_egyk = var_hqta.pop(0)
            var_dcmd, var_llti = var_rgwu.pop(0)
            if (var_wnki != var_dcmd or var_wnki == 'L' and var_egyk <
                var_llti or var_wnki == 'R' and var_egyk > var_llti):
                return False
        return True
