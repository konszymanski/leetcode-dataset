class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [['' for var_ayzf in var_wnki(var_hqta)] for var_ayzf in
            var_wnki(var_wrnh)]
        for var_egyk in var_wnki(var_wrnh):
            for var_dcmd in var_wnki(var_hqta):
                var_osiz[var_egyk][var_dcmd] = arg_xdvx[var_dcmd][var_egyk]
        for var_egyk in var_wnki(var_wrnh):
            var_osiz[var_egyk].reverse()
        for var_dcmd in var_wnki(var_hqta):
            var_llti = var_wrnh - 1
            for var_egyk in var_wnki(var_wrnh - 1, -1, -1):
                if var_osiz[var_egyk][var_dcmd] == '#':
                    var_osiz[var_egyk][var_dcmd] = '.'
                    var_osiz[var_llti][var_dcmd] = '#'
                    var_llti -= 1
                if var_osiz[var_egyk][var_dcmd] == '*':
                    var_llti = var_egyk - 1
        return var_osiz
