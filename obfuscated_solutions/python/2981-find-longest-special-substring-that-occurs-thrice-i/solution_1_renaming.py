class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti:
        var_bacg = {}
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx)):
            var_osiz = []
            for var_ayzf in var_rgwu(var_hqta, var_wrnh(arg_xdvx)):
                if not var_osiz or var_osiz[-1] == arg_xdvx[var_ayzf]:
                    var_osiz.append(arg_xdvx[var_ayzf])
                    var_wnki = ''.join(var_osiz)
                    if var_wnki in var_bacg:
                        var_bacg[var_wnki] += 1
                    else:
                        var_bacg[var_wnki] = 1
                else:
                    break
        var_egyk = 0
        for var_rcsn, var_dcmd in var_bacg.items():
            if var_dcmd >= 3 and var_wrnh(var_rcsn) > var_egyk:
                var_egyk = var_wrnh(var_rcsn)
        if var_egyk == 0:
            return -1
        return var_egyk
