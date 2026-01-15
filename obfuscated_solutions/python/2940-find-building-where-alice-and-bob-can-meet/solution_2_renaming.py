class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = [-1] * var_rgwu(arg_rcsn)
        var_wrnh = [[] for var_osiz in arg_xdvx]
        for var_ayzf, var_wnki in var_egyk(arg_rcsn):
            var_dcmd, var_llti = var_wnki
            if var_dcmd < var_llti and arg_xdvx[var_dcmd] < arg_xdvx[var_llti]:
                var_hqta[var_ayzf] = var_llti
            elif var_dcmd > var_llti and arg_xdvx[var_dcmd] > arg_xdvx[var_llti
                ]:
                var_hqta[var_ayzf] = var_dcmd
            elif var_dcmd == var_llti:
                var_hqta[var_ayzf] = var_dcmd
            else:
                var_wrnh[var_zbxo(var_dcmd, var_llti)].append((var_zbxo(
                    arg_xdvx[var_dcmd], arg_xdvx[var_llti]), var_ayzf))
        for var_ayzf, var_rdmc in var_egyk(arg_xdvx):
            while var_bacg and var_bacg[0][0] < var_rdmc:
                var_osiz, var_rjut = var_lsgw.heappop(var_bacg)
                var_hqta[var_rjut] = var_ayzf
            for var_cbvh in var_wrnh[var_ayzf]:
                var_lsgw.heappush(var_bacg, var_cbvh)
        return var_hqta
