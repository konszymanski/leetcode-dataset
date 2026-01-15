class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_egyk:
        var_rgwu = [False] * var_wrnh(arg_xdvx)
        for var_osiz in var_ayzf(var_wrnh(arg_xdvx)):
            for var_wnki in arg_rcsn:
                if var_osiz < var_wrnh(var_wnki) - 1:
                    continue
                if var_osiz == var_wrnh(var_wnki) - 1 or var_rgwu[var_osiz -
                    var_wrnh(var_wnki)]:
                    if arg_xdvx[var_osiz - var_wrnh(var_wnki) + 1:var_osiz + 1
                        ] == var_wnki:
                        var_rgwu[var_osiz] = True
                        break
        return var_rgwu[-1]
