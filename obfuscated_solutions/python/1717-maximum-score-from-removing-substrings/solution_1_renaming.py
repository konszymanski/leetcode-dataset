class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = 0
        var_osiz = 'ab' if arg_rcsn > arg_bacg else 'ba'
        var_ayzf = 'ba' if var_osiz == 'ab' else 'ab'
        var_wnki = arg_ihhe.remove_substring(arg_xdvx, var_osiz)
        var_egyk = (var_dcmd(arg_xdvx) - var_dcmd(var_wnki)) // 2
        var_wrnh += var_egyk * var_llti(arg_rcsn, arg_bacg)
        var_zbxo = arg_ihhe.remove_substring(var_wnki, var_ayzf)
        var_egyk = (var_dcmd(var_wnki) - var_dcmd(var_zbxo)) // 2
        var_wrnh += var_egyk * var_rdmc(arg_rcsn, arg_bacg)
        return var_wrnh

    def func_rjut(arg_ihhe, arg_lsgw: var_hqta, arg_cbvh: var_hqta) ->var_hqta:
        var_yjch = []
        for var_dmio in arg_lsgw:
            if var_dmio == arg_cbvh[1] and var_yjch and var_yjch[-1
                ] == arg_cbvh[0]:
                var_yjch.pop()
            else:
                var_yjch.append(var_dmio)
        return ''.join(var_yjch)
