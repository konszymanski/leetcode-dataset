class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_rgwu]
        ) ->var_bacg:
        var_wrnh = []
        var_osiz = 0
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            if var_osiz < var_egyk(arg_rcsn) and var_ayzf == arg_rcsn[var_osiz
                ]:
                var_wrnh.append(' ')
                var_osiz += 1
            var_wrnh.append(arg_xdvx[var_ayzf])
        return ''.join(var_wrnh)
