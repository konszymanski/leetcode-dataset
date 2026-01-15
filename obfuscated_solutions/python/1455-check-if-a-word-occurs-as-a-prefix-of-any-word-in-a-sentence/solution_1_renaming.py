class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_rdmc:
        var_hqta = []
        var_rgwu = ''
        for var_wrnh in arg_xdvx:
            if var_wrnh != ' ':
                var_rgwu += var_wrnh
            elif var_rgwu:
                var_hqta.append(var_rgwu)
                var_rgwu = ''
        if var_rgwu:
            var_hqta.append(var_rgwu)
        for var_osiz, var_ayzf in var_wnki(var_hqta):
            if var_egyk(var_ayzf) >= var_egyk(arg_rcsn):
                var_dcmd = True
                for var_llti in var_zbxo(var_egyk(arg_rcsn)):
                    if var_ayzf[var_llti] != arg_rcsn[var_llti]:
                        var_dcmd = False
                        break
                if var_dcmd:
                    return var_osiz + 1
        return -1
