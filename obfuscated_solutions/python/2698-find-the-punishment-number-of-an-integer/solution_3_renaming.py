class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        if arg_rcsn < 0 or arg_xdvx < arg_rcsn:
            return False
        if arg_xdvx == arg_rcsn:
            return True
        return arg_ihhe.can_partition(arg_xdvx // 10, arg_rcsn - arg_xdvx % 10
            ) or arg_ihhe.can_partition(arg_xdvx // 100, arg_rcsn - 
            arg_xdvx % 100) or arg_ihhe.can_partition(arg_xdvx // 1000, 
            arg_rcsn - arg_xdvx % 1000)

    def func_bacg(arg_ihhe, arg_hqta: var_rgwu) ->var_rgwu:
        var_wrnh = 0
        for var_osiz in var_ayzf(1, arg_hqta + 1):
            var_wnki = var_osiz * var_osiz
            if arg_ihhe.can_partition(var_wnki, var_osiz):
                var_wrnh += var_wnki
        return var_wrnh
