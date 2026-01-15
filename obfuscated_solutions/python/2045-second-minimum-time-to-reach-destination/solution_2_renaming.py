class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        from collections import defaultdict
        from collections import deque
        var_rgwu = var_wrnh(var_osiz)
        for var_ayzf in arg_rcsn:
            var_wnki, var_egyk = var_ayzf
            var_rgwu[var_wnki].append(var_egyk)
            var_rgwu[var_egyk].append(var_wnki)
        var_dcmd, var_llti = [-1] * (arg_xdvx + 1), [-1] * (arg_xdvx + 1)
        var_zbxo = var_rdmc([(1, 1)])
        var_dcmd[1] = 0
        while var_zbxo:
            var_rjut, var_lsgw = var_zbxo.popleft()
            var_cbvh = var_dcmd[var_rjut] if var_lsgw == 1 else var_llti[
                var_rjut]
            if var_cbvh // arg_hqta % 2 == 1:
                var_cbvh = arg_hqta * (var_cbvh // arg_hqta + 1) + arg_bacg
            else:
                var_cbvh = var_cbvh + arg_bacg
            for var_yjch in var_rgwu[var_rjut]:
                if var_dcmd[var_yjch] == -1:
                    var_dcmd[var_yjch] = var_cbvh
                    var_zbxo.append((var_yjch, 1))
                elif var_llti[var_yjch] == -1 and var_dcmd[var_yjch
                    ] != var_cbvh:
                    if var_yjch == arg_xdvx:
                        return var_cbvh
                    var_llti[var_yjch] = var_cbvh
                    var_zbxo.append((var_yjch, 2))
        return 0
