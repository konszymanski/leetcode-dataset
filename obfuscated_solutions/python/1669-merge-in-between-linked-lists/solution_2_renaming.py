class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh,
        arg_bacg: var_wrnh, arg_hqta: var_rgwu) ->var_rgwu:
        var_osiz = var_rgwu()
        var_ayzf = arg_xdvx
        for var_wnki in var_egyk(arg_bacg):
            if var_wnki == arg_rcsn - 1:
                var_osiz = var_ayzf
            var_ayzf = var_ayzf.next
        var_osiz.next = arg_hqta
        while arg_hqta.next is not None:
            arg_hqta = arg_hqta.next
        arg_hqta.next = var_ayzf.next
        var_ayzf.next = None
        return arg_xdvx
