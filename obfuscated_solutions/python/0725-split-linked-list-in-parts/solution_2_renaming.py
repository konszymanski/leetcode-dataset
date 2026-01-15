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
        var_dcmd = var_ayzf
        for var_llti in var_zbxo(arg_rcsn):
            var_rdmc = var_ayzf
            var_rjut = var_wnki
            if var_egyk > 0:
                var_egyk -= 1
                var_rjut += 1
            var_lsgw = 0
            while var_lsgw < var_rjut:
                var_dcmd = var_ayzf
                if var_ayzf is not None:
                    var_ayzf = var_ayzf.next
                var_lsgw += 1
            if var_dcmd is not None:
                var_dcmd.next = None
            var_wrnh[var_llti] = var_rdmc
        return var_wrnh
