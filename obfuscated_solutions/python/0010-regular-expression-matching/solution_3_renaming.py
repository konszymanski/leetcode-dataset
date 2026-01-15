class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn: var_hqta, arg_bacg: var_hqta) ->var_zbxo:
        var_rgwu = {}

        def func_wrnh(arg_osiz: var_wnki, arg_ayzf: var_wnki) ->var_zbxo:
            if (arg_osiz, arg_ayzf) not in var_rgwu:
                if arg_ayzf == var_egyk(arg_bacg):
                    var_dcmd = arg_osiz == var_egyk(arg_rcsn)
                else:
                    var_llti = arg_osiz < var_egyk(arg_rcsn) and arg_bacg[
                        arg_ayzf] in {arg_rcsn[arg_osiz], '.'}
                    if arg_ayzf + 1 < var_egyk(arg_bacg) and arg_bacg[
                        arg_ayzf + 1] == '*':
                        var_dcmd = func_wrnh(arg_osiz, arg_ayzf + 2
                            ) or var_llti and func_wrnh(arg_osiz + 1, arg_ayzf)
                    else:
                        var_dcmd = var_llti and func_wrnh(arg_osiz + 1, 
                            arg_ayzf + 1)
                var_rgwu[arg_osiz, arg_ayzf] = var_dcmd
            return var_rgwu[arg_osiz, arg_ayzf]
        return func_wrnh(0, 0)
