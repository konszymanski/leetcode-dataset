class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_hqta:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = arg_xdvx
        arg_xdvx = arg_xdvx + arg_xdvx
        var_wnki = var_egyk.gcd(arg_bacg, var_wrnh)
        for var_dcmd in var_llti(0, var_wrnh, var_wnki):
            for var_zbxo in var_llti(10):
                var_rdmc = 0 if arg_bacg % 2 == 0 else 9
                for var_rjut in var_llti(var_rdmc + 1):
                    var_lsgw = var_cbvh(arg_xdvx[var_dcmd:var_dcmd + var_wrnh])
                    for var_yjch in var_llti(1, var_wrnh, 2):
                        var_lsgw[var_yjch] = var_hqta((var_rgwu(var_lsgw[
                            var_yjch]) + var_zbxo * arg_rcsn) % 10)
                    for var_yjch in var_llti(0, var_wrnh, 2):
                        var_lsgw[var_yjch] = var_hqta((var_rgwu(var_lsgw[
                            var_yjch]) + var_rjut * arg_rcsn) % 10)
                    var_dmio = ''.join(var_lsgw)
                    if var_dmio < var_ayzf:
                        var_ayzf = var_dmio
        return var_ayzf
