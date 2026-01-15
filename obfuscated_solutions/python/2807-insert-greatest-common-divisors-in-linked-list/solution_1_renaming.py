class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:

        def func_hqta(arg_rgwu, arg_wrnh):
            while arg_wrnh != 0:
                arg_rgwu, arg_wrnh = arg_wrnh, arg_rgwu % arg_wrnh
            return arg_rgwu
        if not arg_xdvx.next:
            return arg_xdvx
        var_osiz = arg_xdvx
        var_ayzf = arg_xdvx.next
        while var_ayzf:
            var_wnki = func_hqta(var_osiz.val, var_ayzf.val)
            var_egyk = var_bacg(var_wnki)
            var_osiz.next = var_egyk
            var_egyk.next = var_ayzf
            var_osiz = var_ayzf
            var_ayzf = var_ayzf.next
        return arg_xdvx
