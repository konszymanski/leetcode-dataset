class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_dmio[
        var_zbxo]:
        var_hqta = var_rgwu()
        var_wrnh = var_rgwu()
        var_osiz = {}
        for var_ayzf in arg_xdvx:
            var_wnki, var_egyk, var_dcmd = var_ayzf
            var_wrnh.add(var_wnki)
            var_wrnh.add(var_egyk)
            var_hqta.add(var_egyk)
            if var_wnki not in var_osiz:
                var_osiz[var_wnki] = []
            var_osiz[var_wnki].append((var_egyk, var_dcmd))
        for var_wnki in var_wrnh.copy():
            if var_wnki in var_hqta:
                var_wrnh.remove(var_wnki)
        var_llti = var_zbxo(var_rdmc(var_rjut(var_wrnh)))
        var_lsgw = var_cbvh([var_llti])
        while var_lsgw:
            var_wnki = var_lsgw.popleft()
            for var_yjch, var_dcmd in var_osiz.get(var_wnki.val, []):
                var_egyk = var_zbxo(var_yjch)
                var_lsgw.append(var_egyk)
                if var_dcmd == 1:
                    var_wnki.left = var_egyk
                else:
                    var_wnki.right = var_egyk
        return var_llti
