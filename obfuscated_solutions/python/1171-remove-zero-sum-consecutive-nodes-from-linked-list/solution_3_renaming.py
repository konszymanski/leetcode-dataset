class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_bacg(0, arg_xdvx)
        var_rgwu = var_hqta
        var_wrnh = 0
        var_osiz = {}
        while var_rgwu is not None:
            var_wrnh += var_rgwu.val
            if var_wrnh in var_osiz:
                var_ayzf = var_osiz[var_wrnh]
                var_rgwu = var_ayzf.next
                var_wnki = var_wrnh + var_rgwu.val
                while var_wnki != var_wrnh:
                    del var_osiz[var_wnki]
                    var_rgwu = var_rgwu.next
                    var_wnki += var_rgwu.val
                var_ayzf.next = var_rgwu.next
            else:
                var_osiz[var_wrnh] = var_rgwu
            var_rgwu = var_rgwu.next
        return var_hqta.next
