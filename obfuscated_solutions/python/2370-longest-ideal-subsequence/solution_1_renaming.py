class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [([-1] * 26) for var_ayzf in var_wnki(var_rgwu)]

        def func_egyk(arg_dcmd: var_hqta, arg_llti: var_hqta, var_osiz:
            var_zbxo, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
            if var_osiz[arg_dcmd][arg_llti] != -1:
                return var_osiz[arg_dcmd][arg_llti]
            var_osiz[arg_dcmd][arg_llti] = 0
            var_rdmc = arg_llti == var_rjut(arg_xdvx[arg_dcmd]) - var_rjut('a')
            if var_rdmc:
                var_osiz[arg_dcmd][arg_llti] = 1
            if arg_dcmd > 0:
                var_osiz[arg_dcmd][arg_llti] = func_egyk(arg_dcmd - 1,
                    arg_llti, var_osiz, arg_xdvx, arg_rcsn)
                if var_rdmc:
                    for var_lsgw in var_wnki(26):
                        if var_cbvh(arg_llti - var_lsgw) <= arg_rcsn:
                            var_osiz[arg_dcmd][arg_llti] = var_yjch(var_osiz
                                [arg_dcmd][arg_llti], func_egyk(arg_dcmd - 
                                1, var_lsgw, var_osiz, arg_xdvx, arg_rcsn) + 1)
            return var_osiz[arg_dcmd][arg_llti]
        var_dmio = 0
        for arg_llti in var_wnki(26):
            var_dmio = var_yjch(var_dmio, func_egyk(var_rgwu - 1, arg_llti,
                var_osiz, arg_xdvx, arg_rcsn))
        return var_dmio
