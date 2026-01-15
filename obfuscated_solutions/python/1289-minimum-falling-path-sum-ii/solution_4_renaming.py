class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = None
        var_osiz = None
        var_ayzf = None
        var_wnki = None
        for var_egyk in var_dcmd(var_hqta):
            if var_ayzf is None or arg_xdvx[var_hqta - 1][var_egyk
                ] <= var_ayzf:
                var_wnki = var_ayzf
                var_osiz = var_wrnh
                var_ayzf = arg_xdvx[var_hqta - 1][var_egyk]
                var_wrnh = var_egyk
            elif var_wnki is None or arg_xdvx[var_hqta - 1][var_egyk
                ] <= var_wnki:
                var_wnki = arg_xdvx[var_hqta - 1][var_egyk]
                var_osiz = var_egyk
        for var_llti in var_dcmd(var_hqta - 2, -1, -1):
            var_zbxo = None
            var_rdmc = None
            var_rjut = None
            var_lsgw = None
            for var_egyk in var_dcmd(var_hqta):
                if var_egyk != var_wrnh:
                    var_cbvh = arg_xdvx[var_llti][var_egyk] + var_ayzf
                else:
                    var_cbvh = arg_xdvx[var_llti][var_egyk] + var_wnki
                if var_rjut is None or var_cbvh <= var_rjut:
                    var_lsgw = var_rjut
                    var_rdmc = var_zbxo
                    var_rjut = var_cbvh
                    var_zbxo = var_egyk
                elif var_lsgw is None or var_cbvh <= var_lsgw:
                    var_lsgw = var_cbvh
                    var_rdmc = var_egyk
            var_wrnh = var_zbxo
            var_osiz = var_rdmc
            var_ayzf = var_rjut
            var_wnki = var_lsgw
        return var_ayzf
