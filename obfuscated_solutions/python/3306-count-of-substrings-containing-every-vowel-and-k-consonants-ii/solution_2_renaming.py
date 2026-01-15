class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_bacg:
        return arg_xdvx in ['a', 'e', 'i', 'o', 'u']

    def func_hqta(arg_ihhe, arg_rgwu: var_rcsn, arg_wrnh: var_osiz) ->var_osiz:
        var_ayzf = 0
        var_wnki = 0
        var_egyk = 0
        var_dcmd = {}
        var_llti = 0
        while var_egyk < var_zbxo(arg_rgwu):
            var_rdmc = arg_rgwu[var_egyk]
            if arg_ihhe._isVowel(var_rdmc):
                var_dcmd[var_rdmc] = var_dcmd.get(var_rdmc, 0) + 1
            else:
                var_llti += 1
            while var_zbxo(var_dcmd) == 5 and var_llti >= arg_wrnh:
                var_ayzf += var_zbxo(arg_rgwu) - var_egyk
                var_rjut = arg_rgwu[var_wnki]
                if arg_ihhe._isVowel(var_rjut):
                    var_dcmd[var_rjut] = var_dcmd.get(var_rjut) - 1
                    if var_dcmd.get(var_rjut) == 0:
                        var_dcmd.pop(var_rjut)
                else:
                    var_llti -= 1
                var_wnki += 1
            var_egyk += 1
        return var_ayzf

    def func_lsgw(arg_ihhe, arg_rgwu: var_rcsn, arg_wrnh: var_osiz) ->var_osiz:
        return arg_ihhe._atLeastK(arg_rgwu, arg_wrnh) - arg_ihhe._atLeastK(
            arg_rgwu, arg_wrnh + 1)
