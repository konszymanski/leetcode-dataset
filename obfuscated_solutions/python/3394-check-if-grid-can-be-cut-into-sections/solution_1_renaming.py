class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_rdmc:

        def func_rgwu(arg_rcsn: var_hqta[var_hqta[var_bacg]], arg_wrnh:
            var_bacg) ->var_rdmc:
            var_osiz = 0
            arg_rcsn.sort(key=lambda rect: var_ayzf[arg_wrnh])
            var_wnki = arg_rcsn[0][arg_wrnh + 2]
            for var_egyk in var_dcmd(1, var_llti(arg_rcsn)):
                var_ayzf = arg_rcsn[var_egyk]
                if var_wnki <= var_ayzf[arg_wrnh]:
                    var_osiz += 1
                var_wnki = var_zbxo(var_wnki, var_ayzf[arg_wrnh + 2])
            return var_osiz >= 2
        return func_rgwu(arg_rcsn, 0) or func_rgwu(arg_rcsn, 1)
