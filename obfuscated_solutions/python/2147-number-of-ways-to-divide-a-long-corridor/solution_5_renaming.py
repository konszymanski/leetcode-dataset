class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = 1000000007
        var_hqta = 1
        var_rgwu = 0
        var_wrnh = None
        for var_osiz, var_ayzf in var_wnki(arg_xdvx):
            if var_ayzf == 'S':
                var_rgwu += 1
                if var_rgwu == 2:
                    var_wrnh = var_osiz
                    var_rgwu = 0
                elif var_rgwu == 1 and var_wrnh is not None:
                    var_hqta *= var_osiz - var_wrnh
                    var_hqta %= var_bacg
        if var_rgwu == 1 or var_wrnh is None:
            return 0
        return var_hqta
