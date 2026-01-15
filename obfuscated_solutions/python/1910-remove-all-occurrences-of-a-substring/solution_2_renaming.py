class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = []
        var_rgwu = var_wrnh(arg_rcsn)
        for var_osiz in arg_xdvx:
            var_hqta.append(var_osiz)
            if var_wrnh(var_hqta) >= var_rgwu and arg_ihhe._check_match(
                var_hqta, arg_rcsn, var_rgwu):
                for var_ayzf in var_wnki(var_rgwu):
                    var_hqta.pop()
        return ''.join(var_hqta)

    def func_egyk(arg_ihhe, var_hqta: var_dcmd, arg_rcsn: var_bacg,
        var_rgwu: var_llti) ->var_zbxo:
        return ''.join(var_hqta[-var_rgwu:]) == arg_rcsn
