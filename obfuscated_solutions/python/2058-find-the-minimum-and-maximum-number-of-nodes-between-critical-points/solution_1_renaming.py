class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rdmc[var_rjut]:
        var_hqta = [-1, -1]
        var_rgwu = var_wrnh('inf')
        var_osiz = arg_xdvx
        var_ayzf = arg_xdvx.next
        var_wnki = 1
        var_egyk = 0
        var_dcmd = 0
        while var_ayzf.next is not None:
            if (var_ayzf.val < var_osiz.val and var_ayzf.val < var_ayzf.
                next.val or var_ayzf.val > var_osiz.val and var_ayzf.val >
                var_ayzf.next.val):
                if var_egyk == 0:
                    var_egyk = var_wnki
                    var_dcmd = var_wnki
                else:
                    var_rgwu = var_llti(var_rgwu, var_wnki - var_egyk)
                    var_egyk = var_wnki
            var_wnki += 1
            var_osiz = var_ayzf
            var_ayzf = var_ayzf.next
        if var_rgwu != var_wrnh('inf'):
            var_zbxo = var_egyk - var_dcmd
            var_hqta = [var_rgwu, var_zbxo]
        return var_hqta
