class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf[var_wnki]:
        var_bacg, var_hqta = 0, var_rgwu(arg_xdvx)
        var_wrnh = []
        for var_osiz in arg_xdvx:
            if var_osiz == 'I':
                var_wrnh.append(var_bacg)
                var_bacg += 1
            else:
                var_wrnh.append(var_hqta)
                var_hqta -= 1
        return var_wrnh + [var_bacg]
