class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):

        def func_bacg(arg_hqta):
            var_rgwu = var_wrnh()
            var_rgwu.add((0, 0))
            for var_osiz in arg_hqta:
                var_ayzf = var_wrnh()
                for var_wnki, var_egyk in var_rgwu:
                    var_ayzf.add((var_wnki + var_osiz, var_egyk))
                    var_ayzf.add((var_wnki, var_egyk + var_osiz))
                var_rgwu |= var_ayzf
            var_dcmd = {}
            for var_wnki, var_egyk in var_rgwu:
                var_dcmd[var_wnki - var_egyk] = var_llti(var_dcmd.get(
                    var_wnki - var_egyk, 0), var_wnki)
            return var_dcmd
        var_zbxo = var_rdmc(arg_rcsn)
        var_rjut = func_bacg(arg_rcsn[:var_zbxo // 2])
        var_lsgw = func_bacg(arg_rcsn[var_zbxo // 2:])
        var_cbvh = 0
        for var_yjch in var_rjut:
            if -var_yjch in var_lsgw:
                var_cbvh = var_llti(var_cbvh, var_rjut[var_yjch] + var_lsgw
                    [-var_yjch])
        return var_cbvh
