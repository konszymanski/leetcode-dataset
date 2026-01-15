class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = var_bacg(arg_xdvx[0])
        var_rgwu = [['.' for var_wrnh in var_osiz(var_rcsn)] for var_wrnh in
            var_osiz(var_hqta)]
        for var_ayzf in var_osiz(var_rcsn):
            var_wnki = var_hqta - 1
            for var_egyk in var_osiz(var_hqta - 1, -1, -1):
                if arg_xdvx[var_ayzf][var_egyk] == '#':
                    var_rgwu[var_wnki][var_rcsn - var_ayzf - 1] = '#'
                    var_wnki -= 1
                if arg_xdvx[var_ayzf][var_egyk] == '*':
                    var_rgwu[var_egyk][var_rcsn - var_ayzf - 1] = '*'
                    var_wnki = var_egyk - 1
        return var_rgwu
