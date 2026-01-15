class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        if var_bacg == 0:
            return arg_xdvx
        var_rgwu = 0
        for var_wrnh in var_osiz(var_bacg - 1, -1, -1):
            if arg_xdvx[var_wrnh] == arg_xdvx[var_rgwu]:
                var_rgwu += 1
        if var_rgwu == var_bacg:
            return arg_xdvx
        var_ayzf = arg_xdvx[var_rgwu:]
        var_wnki = var_ayzf[::-1]
        return var_wnki + arg_ihhe.shortestPalindrome(arg_xdvx[:var_rgwu]
            ) + var_ayzf
