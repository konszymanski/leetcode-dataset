class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        arg_ihhe.index = 0

        def func_rgwu():
            var_wrnh = var_osiz(var_ayzf)
            while arg_ihhe.index < var_bacg and arg_xdvx[arg_ihhe.index
                ] != ')':
                if arg_xdvx[arg_ihhe.index] == '(':
                    arg_ihhe.index += 1
                    var_wnki = func_rgwu()
                    for var_egyk in var_wnki:
                        var_wrnh[var_egyk] += var_wnki[var_egyk]
                else:
                    var_dcmd = arg_xdvx[arg_ihhe.index]
                    arg_ihhe.index += 1
                    while arg_ihhe.index < var_bacg and arg_xdvx[arg_ihhe.index
                        ].islower():
                        var_dcmd += arg_xdvx[arg_ihhe.index]
                        arg_ihhe.index += 1
                    var_llti = ''
                    while arg_ihhe.index < var_bacg and arg_xdvx[arg_ihhe.index
                        ].isdigit():
                        var_llti += arg_xdvx[arg_ihhe.index]
                        arg_ihhe.index += 1
                    if var_llti == '':
                        var_wrnh[var_dcmd] += 1
                    else:
                        var_wrnh[var_dcmd] += var_ayzf(var_llti)
            arg_ihhe.index += 1
            var_zbxo = ''
            while arg_ihhe.index < var_bacg and arg_xdvx[arg_ihhe.index
                ].isdigit():
                var_zbxo += arg_xdvx[arg_ihhe.index]
                arg_ihhe.index += 1
            if var_zbxo:
                var_zbxo = var_ayzf(var_zbxo)
                for var_egyk in var_wrnh:
                    var_wrnh[var_egyk] *= var_zbxo
            return var_wrnh
        var_rdmc = func_rgwu()
        var_rdmc = var_rjut(var_lsgw(var_rdmc.items()))
        var_cbvh = ''
        for var_egyk in var_rdmc:
            var_cbvh += var_egyk
            if var_rdmc[var_egyk] > 1:
                var_cbvh += var_rcsn(var_rdmc[var_egyk])
        return var_cbvh
