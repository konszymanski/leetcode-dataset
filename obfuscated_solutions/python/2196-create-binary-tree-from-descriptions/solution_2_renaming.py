class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_lsgw[
        var_rjut]:
        var_hqta = {}
        var_rgwu = var_wrnh()
        var_osiz = var_wrnh()
        for var_ayzf, var_wnki, var_egyk in arg_xdvx:
            if var_ayzf not in var_hqta:
                var_hqta[var_ayzf] = []
            var_hqta[var_ayzf].append((var_wnki, var_egyk))
            var_rgwu.add(var_ayzf)
            var_rgwu.add(var_wnki)
            var_osiz.add(var_wnki)
        var_dcmd = (var_rgwu - var_osiz).pop()

        def func_llti(arg_zbxo):
            var_rdmc = var_rjut(arg_zbxo)
            if arg_zbxo in var_hqta:
                for var_wnki, var_egyk in var_hqta[arg_zbxo]:
                    if var_egyk:
                        var_rdmc.left = func_llti(var_wnki)
                    else:
                        var_rdmc.right = func_llti(var_wnki)
            return var_rdmc
        return func_llti(var_dcmd)
