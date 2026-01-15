class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rjut:
        arg_xdvx = ''.join(var_bacg for var_bacg, var_hqta in var_rgwu.
            groupby(arg_xdvx))
        var_wrnh = {}

        def func_osiz(arg_ayzf, arg_wnki) ->var_rjut:
            if arg_ayzf > arg_wnki:
                return 0
            if (arg_ayzf, arg_wnki) in var_wrnh:
                return var_wrnh[arg_ayzf, arg_wnki]
            var_egyk = 1 + func_osiz(arg_ayzf + 1, arg_wnki)
            for var_dcmd in var_llti(arg_ayzf + 1, arg_wnki + 1):
                if arg_xdvx[var_dcmd] == arg_xdvx[arg_ayzf]:
                    var_zbxo = func_osiz(arg_ayzf, var_dcmd - 1) + func_osiz(
                        var_dcmd + 1, arg_wnki)
                    var_egyk = var_rdmc(var_egyk, var_zbxo)
            var_wrnh[arg_ayzf, arg_wnki] = var_egyk
            return var_egyk
        return func_osiz(0, var_lsgw(arg_xdvx) - 1)
