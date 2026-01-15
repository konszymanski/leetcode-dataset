class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_bacg:
        var_rgwu = {}
        arg_rcsn = [0] + var_wrnh(arg_rcsn) + [arg_xdvx]

        def func_osiz(arg_ayzf, arg_wnki):
            if (arg_ayzf, arg_wnki) in var_rgwu:
                return var_rgwu[arg_ayzf, arg_wnki]
            if arg_wnki - arg_ayzf == 1:
                return 0
            var_egyk = var_dcmd(func_osiz(arg_ayzf, var_llti) + func_osiz(
                var_llti, arg_wnki) + arg_rcsn[arg_wnki] - arg_rcsn[
                arg_ayzf] for var_llti in var_zbxo(arg_ayzf + 1, arg_wnki))
            var_rgwu[arg_ayzf, arg_wnki] = var_egyk
            return var_egyk
        return func_osiz(0, var_rdmc(arg_rcsn) - 1)
