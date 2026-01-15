class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        arg_ihhe.index = 0

        def func_rgwu():
            var_wrnh = var_osiz(var_ayzf)
            var_wnki = ''
            var_egyk = ''
            while arg_ihhe.index < var_bacg:
                if arg_xdvx[arg_ihhe.index].isupper():
                    if var_wnki:
                        if var_egyk == '':
                            var_wrnh[var_wnki] += 1
                        else:
                            var_wrnh[var_wnki] += var_ayzf(var_egyk)
                    var_wnki = arg_xdvx[arg_ihhe.index]
                    var_egyk = ''
                    arg_ihhe.index += 1
                elif arg_xdvx[arg_ihhe.index].islower():
                    var_wnki += arg_xdvx[arg_ihhe.index]
                    arg_ihhe.index += 1
                elif arg_xdvx[arg_ihhe.index].isdigit():
                    var_egyk += arg_xdvx[arg_ihhe.index]
                    arg_ihhe.index += 1
                elif arg_xdvx[arg_ihhe.index] == '(':
                    arg_ihhe.index += 1
                    var_dcmd = func_rgwu()
                    for var_llti in var_dcmd:
                        var_wrnh[var_llti] += var_dcmd[var_llti]
                elif arg_xdvx[arg_ihhe.index] == ')':
                    if var_wnki:
                        if var_egyk == '':
                            var_wrnh[var_wnki] += 1
                        else:
                            var_wrnh[var_wnki] += var_ayzf(var_egyk)
                    arg_ihhe.index += 1
                    var_zbxo = ''
                    while arg_ihhe.index < var_bacg and arg_xdvx[arg_ihhe.index
                        ].isdigit():
                        var_zbxo += arg_xdvx[arg_ihhe.index]
                        arg_ihhe.index += 1
                    if var_zbxo:
                        var_zbxo = var_ayzf(var_zbxo)
                        for var_llti in var_wrnh:
                            var_wrnh[var_llti] *= var_zbxo
                    return var_wrnh
            if var_wnki:
                if var_egyk == '':
                    var_wrnh[var_wnki] += 1
                else:
                    var_wrnh[var_wnki] += var_ayzf(var_egyk)
            return var_wrnh
        var_rdmc = func_rgwu()
        var_rdmc = var_rjut(var_lsgw(var_rdmc.items()))
        var_cbvh = ''
        for var_llti in var_rdmc:
            var_cbvh += var_llti
            if var_rdmc[var_llti] > 1:
                var_cbvh += var_rcsn(var_rdmc[var_llti])
        return var_cbvh
