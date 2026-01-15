class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_llti:
        if var_rgwu(arg_xdvx) % arg_rcsn != 0:
            return False
        var_wrnh = var_osiz(arg_xdvx)
        for var_ayzf in arg_xdvx:
            var_wnki = var_ayzf
            while var_wrnh[var_wnki - 1]:
                var_wnki -= 1
            while var_wnki <= var_ayzf:
                while var_wrnh[var_wnki]:
                    for var_egyk in var_dcmd(var_wnki, var_wnki + arg_rcsn):
                        if not var_wrnh[var_egyk]:
                            return False
                        var_wrnh[var_egyk] -= 1
                var_wnki += 1
        return True
