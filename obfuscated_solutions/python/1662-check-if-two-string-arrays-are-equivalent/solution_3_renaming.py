class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_llti:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = var_ayzf(arg_rcsn)
        var_wnki = [var_ayzf(var_egyk) for var_egyk in arg_rcsn]
        for var_egyk in arg_xdvx:
            for var_dcmd in var_egyk:
                if var_rgwu >= var_osiz or var_dcmd != arg_rcsn[var_rgwu][
                    var_wrnh]:
                    return False
                var_wrnh += 1
                if var_wrnh == var_wnki[var_rgwu]:
                    var_rgwu += 1
                    var_wrnh = 0
        return var_rgwu == var_osiz
