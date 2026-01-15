class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh, var_osiz = var_ayzf(arg_xdvx), var_ayzf(arg_rcsn)
        var_wnki, var_egyk = 0, 0
        while var_wnki < var_wrnh and arg_xdvx[var_wnki] < 0:
            var_wnki += 1
        while var_egyk < var_osiz and arg_rcsn[var_egyk] < 0:
            var_egyk += 1
        var_dcmd, var_llti = var_rgwu(-10000000000.0), var_rgwu(10000000000.0)
        while var_dcmd <= var_llti:
            var_zbxo = (var_dcmd + var_llti) // 2
            var_rdmc = 0
            var_rjut, var_lsgw = 0, var_egyk - 1
            while var_rjut < var_wnki and var_lsgw >= 0:
                if arg_xdvx[var_rjut] * arg_rcsn[var_lsgw] > var_zbxo:
                    var_rjut += 1
                else:
                    var_rdmc += var_wnki - var_rjut
                    var_lsgw -= 1
            var_rjut, var_lsgw = var_wnki, var_osiz - 1
            while var_rjut < var_wrnh and var_lsgw >= var_egyk:
                if arg_xdvx[var_rjut] * arg_rcsn[var_lsgw] > var_zbxo:
                    var_lsgw -= 1
                else:
                    var_rdmc += var_lsgw - var_egyk + 1
                    var_rjut += 1
            var_rjut, var_lsgw = 0, var_egyk
            while var_rjut < var_wnki and var_lsgw < var_osiz:
                if arg_xdvx[var_rjut] * arg_rcsn[var_lsgw] > var_zbxo:
                    var_lsgw += 1
                else:
                    var_rdmc += var_osiz - var_lsgw
                    var_rjut += 1
            var_rjut, var_lsgw = var_wnki, 0
            while var_rjut < var_wrnh and var_lsgw < var_egyk:
                if arg_xdvx[var_rjut] * arg_rcsn[var_lsgw] > var_zbxo:
                    var_rjut += 1
                else:
                    var_rdmc += var_wrnh - var_rjut
                    var_lsgw += 1
            if var_rdmc < arg_bacg:
                var_dcmd = var_zbxo + 1
            else:
                var_llti = var_zbxo - 1
        return var_dcmd
