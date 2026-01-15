class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_dcmd:
        var_hqta = var_rgwu(arg_xdvx)
        if var_hqta % 2 == 1:
            return False
        var_wrnh = 0
        var_osiz = 0
        for var_ayzf in var_wnki(var_hqta):
            if arg_rcsn[var_ayzf] == '0':
                var_osiz += 1
            elif arg_xdvx[var_ayzf] == '(':
                var_wrnh += 1
            elif arg_xdvx[var_ayzf] == ')':
                if var_wrnh > 0:
                    var_wrnh -= 1
                elif var_osiz > 0:
                    var_osiz -= 1
                else:
                    return False
        var_egyk = 0
        for var_ayzf in var_wnki(var_hqta - 1, -1, -1):
            if arg_rcsn[var_ayzf] == '0':
                var_egyk -= 1
                var_osiz -= 1
            elif arg_xdvx[var_ayzf] == '(':
                var_egyk += 1
                var_wrnh -= 1
            elif arg_xdvx[var_ayzf] == ')':
                var_egyk -= 1
            if var_egyk > 0:
                return False
        if var_wrnh > 0:
            return False
        return True
