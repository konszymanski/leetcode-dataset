class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_wrnh]:
        var_osiz = var_ayzf(arg_xdvx)
        while arg_rcsn and arg_rcsn.val in var_osiz:
            arg_rcsn = arg_rcsn.next
        if not arg_rcsn:
            return None
        var_wnki = arg_rcsn
        while var_wnki.next:
            if var_wnki.next.val in var_osiz:
                var_wnki.next = var_wnki.next.next
            else:
                var_wnki = var_wnki.next
        return arg_rcsn
