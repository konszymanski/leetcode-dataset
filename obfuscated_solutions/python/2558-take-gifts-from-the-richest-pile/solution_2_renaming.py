class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in var_ayzf(arg_rcsn):
            var_wnki = var_rgwu[-1]
            var_rgwu.pop()
            var_egyk = var_dcmd((var_llti for var_llti, var_zbxo in
                var_rdmc(var_rgwu) if var_zbxo > var_rjut.floor(var_rjut.
                sqrt(var_wnki))), var_bacg)
            var_rgwu.insert(var_egyk, var_rjut.floor(var_rjut.sqrt(var_wnki)))
        var_lsgw = var_cbvh(var_rgwu)
        return var_lsgw
