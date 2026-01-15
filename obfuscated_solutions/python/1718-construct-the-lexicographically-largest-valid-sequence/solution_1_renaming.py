class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rgwu[var_rcsn]:
        var_bacg = [0] * (arg_xdvx * 2 - 1)
        var_hqta = [False] * (arg_xdvx + 1)
        arg_ihhe.find_lexicographically_largest_sequence(0, var_bacg,
            var_hqta, arg_xdvx)
        return var_bacg

    def func_wrnh(arg_ihhe, arg_osiz, var_bacg, var_hqta, arg_xdvx):
        if arg_osiz == var_ayzf(var_bacg):
            return True
        if var_bacg[arg_osiz] != 0:
            return arg_ihhe.find_lexicographically_largest_sequence(
                arg_osiz + 1, var_bacg, var_hqta, arg_xdvx)
        for var_wnki in var_egyk(arg_xdvx, 0, -1):
            if var_hqta[var_wnki]:
                continue
            var_hqta[var_wnki] = True
            var_bacg[arg_osiz] = var_wnki
            if var_wnki == 1:
                if arg_ihhe.find_lexicographically_largest_sequence(
                    arg_osiz + 1, var_bacg, var_hqta, arg_xdvx):
                    return True
            elif arg_osiz + var_wnki < var_ayzf(var_bacg) and var_bacg[
                arg_osiz + var_wnki] == 0:
                var_bacg[arg_osiz + var_wnki] = var_wnki
                if arg_ihhe.find_lexicographically_largest_sequence(
                    arg_osiz + 1, var_bacg, var_hqta, arg_xdvx):
                    return True
                var_bacg[arg_osiz + var_wnki] = 0
            var_bacg[arg_osiz] = 0
            var_hqta[var_wnki] = False
        return False
