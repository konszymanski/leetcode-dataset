class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_bacg:
        return (arg_xdvx == 'a' or arg_xdvx == 'e' or arg_xdvx == 'i' or 
            arg_xdvx == 'o' or arg_xdvx == 'u')

    def func_hqta(arg_ihhe, arg_rgwu: var_rcsn, arg_wrnh: var_osiz) ->var_osiz:
        var_ayzf = 0
        var_wnki = var_egyk = 0
        var_dcmd = {}
        var_llti = 0
        var_zbxo = [0] * var_rdmc(arg_rgwu)
        var_rjut = var_rdmc(arg_rgwu)
        for var_lsgw in var_cbvh(var_rdmc(arg_rgwu) - 1, -1, -1):
            var_zbxo[var_lsgw] = var_rjut
            if not arg_ihhe._isVowel(arg_rgwu[var_lsgw]):
                var_rjut = var_lsgw
        while var_egyk < var_rdmc(arg_rgwu):
            var_yjch = arg_rgwu[var_egyk]
            if arg_ihhe._isVowel(var_yjch):
                var_dcmd[var_yjch] = var_dcmd.get(var_yjch, 0) + 1
            else:
                var_llti += 1
            while var_llti > arg_wrnh:
                var_dmio = arg_rgwu[var_wnki]
                if arg_ihhe._isVowel(var_dmio):
                    var_dcmd[var_dmio] -= 1
                    if var_dcmd[var_dmio] == 0:
                        del var_dcmd[var_dmio]
                else:
                    var_llti -= 1
                var_wnki += 1
            while var_wnki < var_rdmc(arg_rgwu) and var_rdmc(var_dcmd
                ) == 5 and var_llti == arg_wrnh:
                var_ayzf += var_zbxo[var_egyk] - var_egyk
                var_dmio = arg_rgwu[var_wnki]
                if arg_ihhe._isVowel(var_dmio):
                    var_dcmd[var_dmio] -= 1
                    if var_dcmd[var_dmio] == 0:
                        del var_dcmd[var_dmio]
                else:
                    var_llti -= 1
                var_wnki += 1
            var_egyk += 1
        return var_ayzf
