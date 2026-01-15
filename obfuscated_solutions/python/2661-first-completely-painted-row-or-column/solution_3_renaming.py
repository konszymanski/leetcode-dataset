class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = {}
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx)):
            var_bacg[arg_xdvx[var_hqta]] = var_hqta
        var_osiz = var_ayzf('inf')
        var_wnki, var_egyk = var_wrnh(arg_rcsn), var_wrnh(arg_rcsn[0])
        for var_dcmd in var_rgwu(var_wnki):
            var_llti = var_ayzf('-inf')
            for var_zbxo in var_rgwu(var_egyk):
                var_rdmc = var_bacg[arg_rcsn[var_dcmd][var_zbxo]]
                var_llti = var_rjut(var_llti, var_rdmc)
            var_osiz = var_lsgw(var_osiz, var_llti)
        for var_zbxo in var_rgwu(var_egyk):
            var_llti = var_ayzf('-inf')
            for var_dcmd in var_rgwu(var_wnki):
                var_rdmc = var_bacg[arg_rcsn[var_dcmd][var_zbxo]]
                var_llti = var_rjut(var_llti, var_rdmc)
            var_osiz = var_lsgw(var_osiz, var_llti)
        return var_osiz
