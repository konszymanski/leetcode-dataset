class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_hqta:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = arg_xdvx
        arg_xdvx = arg_xdvx + arg_xdvx
        var_wnki = var_egyk.gcd(arg_bacg, var_wrnh)

        def func_dcmd(arg_llti, arg_zbxo):
            var_rdmc = var_rgwu(arg_llti[arg_zbxo])
            var_rjut, var_lsgw = 10, 0
            for var_cbvh in var_yjch(10):
                var_dmio = (var_rdmc + var_cbvh * arg_rcsn) % 10
                if var_dmio < var_rjut:
                    var_rjut = var_dmio
                    var_lsgw = var_cbvh
            var_ulfl = var_lgvi(arg_llti)
            for var_cbvh in var_yjch(arg_zbxo, var_wrnh, 2):
                var_ulfl[var_cbvh] = var_hqta((var_rgwu(var_ulfl[var_cbvh]) +
                    var_lsgw * arg_rcsn) % 10)
            return ''.join(var_ulfl)
        for var_cbvh in var_yjch(0, var_wrnh, var_wnki):
            arg_llti = arg_xdvx[var_cbvh:var_cbvh + var_wrnh]
            arg_llti = func_dcmd(arg_llti, 1)
            if arg_bacg % 2:
                arg_llti = func_dcmd(arg_llti, 0)
            if arg_llti < var_ayzf:
                var_ayzf = arg_llti
        return var_ayzf
