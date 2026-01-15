class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if arg_xdvx == 1:
            return 10
        var_bacg = 4
        var_hqta = 2
        var_rgwu = 2
        var_wrnh = 1
        var_osiz = 10 ** 9 + 7
        for var_ayzf in var_wnki(arg_xdvx - 1):
            var_bacg, var_hqta, var_rgwu, var_wrnh = 2 * (var_hqta + var_rgwu
                ) % var_osiz, var_bacg, (var_bacg + 2 * var_wrnh
                ) % var_osiz, var_rgwu
        return (var_bacg + var_hqta + var_rgwu + var_wrnh) % var_osiz
