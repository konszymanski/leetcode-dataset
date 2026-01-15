class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = []
        for var_ayzf in var_wnki(var_hqta):
            for var_egyk in var_wnki(var_rgwu):
                if arg_xdvx[var_ayzf][var_egyk]:
                    var_dcmd, var_llti = var_ayzf, var_egyk
                    while var_dcmd < var_hqta and arg_xdvx[var_dcmd][var_egyk]:
                        var_llti = var_egyk
                        while var_llti < var_rgwu and arg_xdvx[var_dcmd][
                            var_llti]:
                            arg_xdvx[var_dcmd][var_llti] = 0
                            var_llti += 1
                        var_dcmd += 1
                    var_osiz.append([var_ayzf, var_egyk, var_dcmd - 1, 
                        var_llti - 1])
        return var_osiz
