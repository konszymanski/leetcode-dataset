class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = {}
        var_wrnh = []
        for var_osiz, var_ayzf in arg_rcsn:
            if var_ayzf in var_rgwu:
                var_wrnh.append((var_rgwu[var_ayzf], var_ayzf))
                var_wrnh.append((var_osiz, var_ayzf))
            else:
                var_rgwu[var_ayzf] = var_osiz

        def func_wnki(arg_egyk):
            var_dcmd = var_llti()
            while arg_egyk in var_rgwu and arg_egyk not in var_dcmd:
                var_dcmd.add(arg_egyk)
                arg_egyk = var_rgwu[arg_egyk]
            return arg_egyk, var_dcmd
        var_zbxo = func_wnki(1)[0]
        if not var_wrnh:
            var_rdmc = func_wnki(var_zbxo)[1]
            for var_osiz, var_ayzf in arg_rcsn:
                if var_osiz in var_rdmc and var_ayzf in var_rdmc:
                    var_rjut = var_osiz, var_ayzf
            return var_rjut
        var_lsgw = var_cbvh.defaultdict(var_yjch)
        for var_ayzf in var_rgwu:
            var_lsgw[var_rgwu[var_ayzf]].append(var_ayzf)
        var_dcmd = [True] + [False] * var_bacg
        var_dmio = [var_zbxo]
        while var_dmio:
            arg_egyk = var_dmio.pop()
            if not var_dcmd[arg_egyk]:
                var_dcmd[arg_egyk] = True
                var_dmio.extend(var_lsgw[arg_egyk])
        return var_wrnh[var_ulfl(var_dcmd)]
