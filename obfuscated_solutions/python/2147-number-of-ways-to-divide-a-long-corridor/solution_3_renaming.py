class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = 1000000007
        var_hqta = 0
        var_rgwu = 0
        var_wrnh = 1
        for var_osiz in arg_xdvx:
            if var_osiz == 'S':
                var_hqta = var_rgwu
                var_rgwu, var_wrnh = var_wrnh, var_rgwu
            else:
                var_wrnh = (var_wrnh + var_hqta) % var_bacg
        return var_hqta
