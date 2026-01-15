class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_zbxo:
        var_rgwu = {}
        for var_wrnh, var_osiz in var_ayzf(arg_rcsn):
            var_rgwu[var_osiz] = var_wrnh
        for var_wnki in var_egyk(var_dcmd(arg_xdvx) - 1):
            for var_llti in var_egyk(var_dcmd(arg_xdvx[var_wnki])):
                if var_llti >= var_dcmd(arg_xdvx[var_wnki + 1]):
                    return False
                if arg_xdvx[var_wnki][var_llti] != arg_xdvx[var_wnki + 1][
                    var_llti]:
                    if var_rgwu[arg_xdvx[var_wnki][var_llti]] > var_rgwu[
                        arg_xdvx[var_wnki + 1][var_llti]]:
                        return False
                    break
        return True
