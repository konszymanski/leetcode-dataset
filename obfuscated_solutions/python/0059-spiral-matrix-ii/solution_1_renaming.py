class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki[var_wnki[var_rcsn]]:
        var_bacg = [([0] * arg_xdvx) for var_hqta in var_rgwu(arg_xdvx)]
        var_wrnh = 1
        for var_osiz in var_rgwu((arg_xdvx + 1) // 2):
            for var_ayzf in var_rgwu(var_osiz, arg_xdvx - var_osiz):
                var_bacg[var_osiz][var_ayzf] = var_wrnh
                var_wrnh += 1
            for var_ayzf in var_rgwu(var_osiz + 1, arg_xdvx - var_osiz):
                var_bacg[var_ayzf][arg_xdvx - var_osiz - 1] = var_wrnh
                var_wrnh += 1
            for var_ayzf in var_rgwu(arg_xdvx - var_osiz - 2, var_osiz - 1, -1
                ):
                var_bacg[arg_xdvx - var_osiz - 1][var_ayzf] = var_wrnh
                var_wrnh += 1
            for var_ayzf in var_rgwu(arg_xdvx - var_osiz - 2, var_osiz, -1):
                var_bacg[var_ayzf][var_osiz] = var_wrnh
                var_wrnh += 1
        return var_bacg
