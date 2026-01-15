class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_wrnh) ->var_rgwu:
        var_osiz = var_wrnh(arg_xdvx - 1)
        var_ayzf = var_wrnh(arg_rcsn)
        return arg_ihhe.calculate(var_ayzf, arg_hqta, arg_bacg
            ) - arg_ihhe.calculate(var_osiz, arg_hqta, arg_bacg)

    def func_wnki(arg_ihhe, arg_egyk: var_wrnh, arg_hqta: var_wrnh,
        arg_bacg: var_rgwu) ->var_rgwu:
        if var_dcmd(arg_egyk) < var_dcmd(arg_hqta):
            return 0
        if var_dcmd(arg_egyk) == var_dcmd(arg_hqta):
            return 1 if arg_egyk >= arg_hqta else 0
        var_llti = arg_egyk[var_dcmd(arg_egyk) - var_dcmd(arg_hqta):]
        var_zbxo = 0
        var_rdmc = var_dcmd(arg_egyk) - var_dcmd(arg_hqta)
        for var_rjut in var_lsgw(var_rdmc):
            if arg_bacg < var_rgwu(arg_egyk[var_rjut]):
                var_zbxo += (arg_bacg + 1) ** (var_rdmc - var_rjut)
                return var_zbxo
            var_zbxo += var_rgwu(arg_egyk[var_rjut]) * (arg_bacg + 1) ** (
                var_rdmc - 1 - var_rjut)
        if var_llti >= arg_hqta:
            var_zbxo += 1
        return var_zbxo
