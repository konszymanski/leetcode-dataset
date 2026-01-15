class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = [0]
        for var_rgwu in arg_rcsn:
            var_hqta.append(var_hqta[-1] + var_rgwu)

        def func_wrnh(arg_osiz, arg_ayzf):
            return (var_hqta[arg_ayzf] - var_hqta[arg_osiz]) / var_wnki(
                arg_ayzf - arg_osiz)
        var_egyk = var_dcmd(arg_rcsn)
        var_llti = [func_wrnh(arg_osiz, var_egyk) for arg_osiz in var_zbxo(
            var_egyk)]
        for var_rdmc in var_zbxo(arg_bacg - 1):
            for arg_osiz in var_zbxo(var_egyk):
                for arg_ayzf in var_zbxo(arg_osiz + 1, var_egyk):
                    var_llti[arg_osiz] = var_rjut(var_llti[arg_osiz], 
                        func_wrnh(arg_osiz, arg_ayzf) + var_llti[arg_ayzf])
        return var_llti[0]
