class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = arg_ihhe.reverse_list(arg_xdvx)
        var_hqta = 0
        var_rgwu, var_wrnh = var_bacg, None
        while var_rgwu:
            var_osiz = var_rgwu.val * 2 + var_hqta
            var_rgwu.val = var_osiz % 10
            var_hqta = 1 if var_osiz > 9 else 0
            var_wrnh, var_rgwu = var_rgwu, var_rgwu.next
        if var_hqta:
            var_wrnh.next = var_rcsn(var_hqta)
        var_ayzf = arg_ihhe.reverse_list(var_bacg)
        return var_ayzf

    def func_wnki(arg_ihhe, arg_egyk: var_rcsn) ->var_rcsn:
        var_wrnh, var_rgwu = None, arg_egyk
        while var_rgwu:
            var_dcmd = var_rgwu.next
            var_rgwu.next = var_wrnh
            var_wrnh, var_rgwu = var_rgwu, var_dcmd
        return var_wrnh
