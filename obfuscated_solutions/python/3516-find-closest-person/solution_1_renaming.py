class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx - arg_bacg)
        var_osiz = var_wrnh(arg_rcsn - arg_bacg)
        if var_rgwu < var_osiz:
            return 1
        elif var_rgwu > var_osiz:
            return 2
        else:
            return 0
