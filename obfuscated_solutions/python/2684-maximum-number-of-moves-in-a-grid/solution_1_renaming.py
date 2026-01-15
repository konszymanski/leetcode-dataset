class Solution:
    var_udax = [-1, 0, 1]

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg, var_hqta = var_rgwu(arg_rcsn), var_rgwu(arg_rcsn[0])
        var_wrnh = var_osiz()
        var_ayzf = [([False] * var_hqta) for var_wnki in var_egyk(var_bacg)]
        for var_dcmd in var_egyk(var_bacg):
            var_ayzf[var_dcmd][0] = True
            var_wrnh.append((var_dcmd, 0, 0))
        var_llti = 0
        while var_wrnh:
            var_zbxo = var_rgwu(var_wrnh)
            for var_wnki in var_egyk(var_zbxo):
                var_rdmc, var_rjut, var_lsgw = var_wrnh.popleft()
                var_llti = var_cbvh(var_llti, var_lsgw)
                for var_yjch in arg_xdvx.dirs:
                    var_dmio, var_ulfl = var_rdmc + var_yjch, var_rjut + 1
                    if (0 <= var_dmio < var_bacg and 0 <= var_ulfl <
                        var_hqta and not var_ayzf[var_dmio][var_ulfl] and 
                        arg_rcsn[var_rdmc][var_rjut] < arg_rcsn[var_dmio][
                        var_ulfl]):
                        var_ayzf[var_dmio][var_ulfl] = True
                        var_wrnh.append((var_dmio, var_ulfl, var_lsgw + 1))
        return var_llti
