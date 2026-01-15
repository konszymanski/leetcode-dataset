class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = 10 ** 9 + 7
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            if var_wrnh == 0 or arg_xdvx[var_wrnh] == arg_xdvx[var_wrnh - 1]:
                var_hqta += 1
            else:
                var_hqta = 1
            var_bacg = (var_bacg + var_hqta) % var_rgwu
        return var_bacg
