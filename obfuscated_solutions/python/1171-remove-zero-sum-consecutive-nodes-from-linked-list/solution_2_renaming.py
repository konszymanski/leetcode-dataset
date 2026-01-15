class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_bacg(0, arg_xdvx)
        var_rgwu = var_hqta
        var_wrnh = 0
        var_osiz = {(0): var_hqta}
        while var_rgwu is not None:
            var_wrnh += var_rgwu.val
            var_osiz[var_wrnh] = var_rgwu
            var_rgwu = var_rgwu.next
        var_wrnh = 0
        var_rgwu = var_hqta
        while var_rgwu is not None:
            var_wrnh += var_rgwu.val
            var_rgwu.next = var_osiz[var_wrnh].next
            var_rgwu = var_rgwu.next
        return var_hqta.next
