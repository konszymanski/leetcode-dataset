class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        arg_rcsn, arg_bacg = var_hqta(arg_rcsn), var_hqta(arg_bacg)
        var_rgwu = 100000

        def func_wrnh(arg_osiz):
            var_ayzf = 0
            while arg_osiz:
                var_ayzf = 10 * var_ayzf + arg_osiz % 10
                arg_osiz /= 10
            return var_ayzf

        def func_wnki(arg_osiz):
            return arg_osiz == func_wrnh(arg_osiz)
        var_ayzf = 0
        for var_egyk in var_dcmd(var_rgwu):
            var_llti = var_zbxo(var_egyk)
            var_rdmc = var_llti + var_llti[-2::-1]
            var_rjut = var_hqta(var_rdmc) ** 2
            if var_rjut > arg_bacg:
                break
            if var_rjut >= arg_rcsn and func_wnki(var_rjut):
                var_ayzf += 1
        for var_egyk in var_dcmd(var_rgwu):
            var_llti = var_zbxo(var_egyk)
            var_rdmc = var_llti + var_llti[::-1]
            var_rjut = var_hqta(var_rdmc) ** 2
            if var_rjut > arg_bacg:
                break
            if var_rjut >= arg_rcsn and func_wnki(var_rjut):
                var_ayzf += 1
        return var_ayzf
