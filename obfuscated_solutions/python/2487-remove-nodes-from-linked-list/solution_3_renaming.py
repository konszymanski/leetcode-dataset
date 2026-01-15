class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = None
        var_bacg = arg_xdvx
        var_hqta = None
        while var_bacg:
            var_hqta = var_bacg.next
            var_bacg.next = var_rcsn
            var_rcsn = var_bacg
            var_bacg = var_hqta
        return var_rcsn

    def func_rgwu(arg_ihhe, arg_xdvx: var_wrnh[var_osiz]) ->var_wrnh[var_osiz]:
        arg_xdvx = arg_ihhe.reverse_list(arg_xdvx)
        var_ayzf = 0
        var_rcsn = None
        var_bacg = arg_xdvx
        while var_bacg:
            var_ayzf = var_wnki(var_ayzf, var_bacg.val)
            if var_bacg.val < var_ayzf:
                var_rcsn.next = var_bacg.next
                var_egyk = var_bacg
                var_bacg = var_bacg.next
                var_egyk.next = None
            else:
                var_rcsn = var_bacg
                var_bacg = var_bacg.next
        return arg_ihhe.reverse_list(arg_xdvx)
