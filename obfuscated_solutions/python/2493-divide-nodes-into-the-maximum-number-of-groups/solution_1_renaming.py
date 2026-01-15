class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [[] for var_hqta in var_rgwu(arg_xdvx)]
        for var_wrnh in arg_rcsn:
            var_bacg[var_wrnh[0] - 1].append(var_wrnh[1] - 1)
            var_bacg[var_wrnh[1] - 1].append(var_wrnh[0] - 1)
        var_osiz = [-1] * arg_xdvx
        for var_ayzf in var_rgwu(arg_xdvx):
            if var_osiz[var_ayzf] != -1:
                continue
            var_osiz[var_ayzf] = 0
            if not arg_ihhe._is_bipartite(var_bacg, var_ayzf, var_osiz):
                return -1
        var_wnki = [arg_ihhe._get_longest_shortest_path(var_bacg, var_ayzf,
            arg_xdvx) for var_ayzf in var_rgwu(arg_xdvx)]
        var_egyk = 0
        var_dcmd = [False] * arg_xdvx
        for var_ayzf in var_rgwu(arg_xdvx):
            if var_dcmd[var_ayzf]:
                continue
            var_egyk += arg_ihhe._get_number_of_groups_for_component(var_bacg,
                var_ayzf, var_wnki, var_dcmd)
        return var_egyk

    def func_llti(arg_ihhe, var_bacg, var_ayzf, var_osiz):
        for var_zbxo in var_bacg[var_ayzf]:
            if var_osiz[var_zbxo] == var_osiz[var_ayzf]:
                return False
            if var_osiz[var_zbxo] != -1:
                continue
            var_osiz[var_zbxo] = (var_osiz[var_ayzf] + 1) % 2
            if not arg_ihhe._is_bipartite(var_bacg, var_zbxo, var_osiz):
                return False
        return True

    def func_rdmc(arg_ihhe, var_bacg, arg_rjut, arg_xdvx):
        var_lsgw = var_cbvh([arg_rjut])
        var_dcmd = [False] * arg_xdvx
        var_dcmd[arg_rjut] = True
        var_yjch = 0
        while var_lsgw:
            for var_hqta in var_rgwu(var_dmio(var_lsgw)):
                var_ulfl = var_lsgw.popleft()
                for var_zbxo in var_bacg[var_ulfl]:
                    if var_dcmd[var_zbxo]:
                        continue
                    var_dcmd[var_zbxo] = True
                    var_lsgw.append(var_zbxo)
            var_yjch += 1
        return var_yjch

    def func_lgvi(arg_ihhe, var_bacg, var_ayzf, var_wnki, var_dcmd):
        var_egyk = var_wnki[var_ayzf]
        var_dcmd[var_ayzf] = True
        for var_zbxo in var_bacg[var_ayzf]:
            if var_dcmd[var_zbxo]:
                continue
            var_egyk = var_wvuc(var_egyk, arg_ihhe.
                _get_number_of_groups_for_component(var_bacg, var_zbxo,
                var_wnki, var_dcmd))
        return var_egyk
