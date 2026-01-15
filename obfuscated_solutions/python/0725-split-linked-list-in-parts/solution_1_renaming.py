class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_cbvh[var_bacg[var_hqta]]:
        var_wrnh = [None] * arg_rcsn
        var_osiz = 0
        var_ayzf = arg_xdvx
        while var_ayzf is not None:
            var_osiz += 1
            var_ayzf = var_ayzf.next
        var_wnki = var_osiz // arg_rcsn
        var_egyk = var_osiz % arg_rcsn
        var_ayzf = arg_xdvx
        for var_dcmd in var_llti(arg_rcsn):
            var_zbxo = var_hqta(0)
            var_rdmc = var_zbxo
            var_rjut = var_wnki
            if var_egyk > 0:
                var_egyk -= 1
                var_rjut += 1
            for var_lsgw in var_llti(var_rjut):
                var_rdmc.next = var_hqta(var_ayzf.val)
                var_rdmc = var_rdmc.next
                var_ayzf = var_ayzf.next
            var_wrnh[var_dcmd] = var_zbxo.next
        return var_wrnh
