class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = []
        for var_osiz in arg_xdvx:
            if var_osiz in var_hqta:
                var_wrnh.append(var_osiz * var_hqta[var_osiz])
                del var_hqta[var_osiz]
        for var_ayzf in var_hqta:
            var_wrnh.append(var_ayzf * var_hqta[var_ayzf])
        return ''.join(var_wrnh)
