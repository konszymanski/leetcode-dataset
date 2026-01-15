class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_hqta[var_rgwu]],
        arg_rcsn: var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = var_wnki(arg_xdvx)
        var_egyk = 0
        var_dcmd = 0

        def func_llti(var_wrnh: var_rgwu, var_osiz: var_rgwu) ->var_rgwu:
            if arg_xdvx[var_osiz][0] <= arg_rcsn:
                return arg_rcsn - arg_xdvx[var_wrnh][0]
            elif arg_xdvx[var_wrnh][0] >= arg_rcsn:
                return arg_xdvx[var_osiz][0] - arg_rcsn
            else:
                return var_zbxo(var_rdmc(arg_rcsn - arg_xdvx[var_osiz][0]),
                    var_rdmc(arg_rcsn - arg_xdvx[var_wrnh][0])) + arg_xdvx[
                    var_osiz][0] - arg_xdvx[var_wrnh][0]
        while var_osiz < var_ayzf:
            var_egyk += arg_xdvx[var_osiz][1]
            while var_wrnh <= var_osiz and func_llti(var_wrnh, var_osiz
                ) > arg_bacg:
                var_egyk -= arg_xdvx[var_wrnh][1]
                var_wrnh += 1
            var_dcmd = var_rjut(var_dcmd, var_egyk)
            var_osiz += 1
        return var_dcmd
