class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_dcmd:
        var_rgwu = 0
        for var_wrnh in arg_rcsn:
            var_osiz = True
            for var_ayzf in var_wrnh:
                var_wnki = False
                for var_egyk in arg_xdvx:
                    if var_egyk == var_ayzf:
                        var_wnki = True
                        break
                if not var_wnki:
                    var_osiz = False
                    break
            if var_osiz:
                var_rgwu += 1
        return var_rgwu
