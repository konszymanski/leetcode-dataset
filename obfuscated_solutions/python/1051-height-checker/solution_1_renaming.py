class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:

        def func_hqta():
            var_rgwu = var_wrnh(var_osiz)
            for var_ayzf in var_wnki(var_rgwu - 1):
                for var_egyk in var_wnki(var_rgwu - var_ayzf - 1):
                    if var_osiz[var_egyk] > var_osiz[var_egyk + 1]:
                        var_osiz[var_egyk], var_osiz[var_egyk + 1] = var_osiz[
                            var_egyk + 1], var_osiz[var_egyk]
        var_osiz = arg_xdvx[:]
        func_hqta()
        var_dcmd = 0
        for var_ayzf in var_wnki(var_wrnh(var_osiz)):
            if arg_xdvx[var_ayzf] != var_osiz[var_ayzf]:
                var_dcmd += 1
        return var_dcmd
