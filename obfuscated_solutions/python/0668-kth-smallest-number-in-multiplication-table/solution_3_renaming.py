class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):

        def func_rgwu(arg_wrnh):
            var_osiz = 0
            for var_ayzf in var_wnki(1, arg_rcsn + 1):
                var_osiz += var_egyk(arg_wrnh // var_ayzf, arg_bacg)
            return var_osiz >= arg_hqta
        var_dcmd, var_llti = 1, arg_rcsn * arg_bacg
        while var_dcmd < var_llti:
            var_zbxo = (var_dcmd + var_llti) / 2
            if not func_rgwu(var_zbxo):
                var_dcmd = var_zbxo + 1
            else:
                var_llti = var_zbxo
        return var_dcmd
