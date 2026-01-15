class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * var_rgwu
        var_ayzf, var_wnki = var_egyk(), var_egyk()
        for var_dcmd in var_llti(var_rgwu):
            var_ayzf.add(arg_xdvx[var_dcmd])
            var_wnki.add(arg_rcsn[var_dcmd])
            var_zbxo = 0
            for var_rdmc in var_ayzf:
                if var_rdmc in var_wnki:
                    var_zbxo += 1
            var_osiz[var_dcmd] = var_zbxo
        return var_osiz
