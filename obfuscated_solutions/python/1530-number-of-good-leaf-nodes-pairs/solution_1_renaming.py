class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        if arg_xdvx is None:
            return
        if arg_xdvx.left is None and arg_xdvx.right is None:
            arg_hqta.add(arg_xdvx)
        if arg_rcsn is not None:
            if arg_rcsn not in arg_bacg:
                arg_bacg[arg_rcsn] = []
            arg_bacg[arg_rcsn].append(arg_xdvx)
            if arg_xdvx not in arg_bacg:
                arg_bacg[arg_xdvx] = []
            arg_bacg[arg_xdvx].append(arg_rcsn)
        arg_ihhe._traverse_tree(arg_xdvx.left, arg_xdvx, arg_bacg, arg_hqta)
        arg_ihhe._traverse_tree(arg_xdvx.right, arg_xdvx, arg_bacg, arg_hqta)

    def func_rgwu(arg_ihhe, arg_wrnh, arg_osiz):
        arg_bacg = {}
        arg_hqta = var_ayzf()
        arg_ihhe._traverse_tree(arg_wrnh, None, arg_bacg, arg_hqta)
        var_wnki = 0
        for var_egyk in arg_hqta:
            var_dcmd = []
            var_llti = var_ayzf()
            var_dcmd.append(var_egyk)
            var_llti.add(var_egyk)
            for var_zbxo in var_rdmc(arg_osiz + 1):
                var_rjut = var_lsgw(var_dcmd)
                for var_cbvh in var_rdmc(var_rjut):
                    arg_xdvx = var_dcmd.pop(0)
                    if arg_xdvx in arg_hqta and arg_xdvx != var_egyk:
                        var_wnki += 1
                    if arg_xdvx in arg_bacg:
                        for var_yjch in arg_bacg.get(arg_xdvx):
                            if var_yjch not in var_llti:
                                var_dcmd.append(var_yjch)
                                var_llti.add(var_yjch)
        return var_wnki // 2
