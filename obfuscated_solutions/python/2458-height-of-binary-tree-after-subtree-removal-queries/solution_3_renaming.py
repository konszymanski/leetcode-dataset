class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_wrnh]:
        var_osiz = {}
        var_ayzf = {}
        var_wnki = []
        var_egyk = []
        var_dcmd = []
        arg_ihhe._dfs(arg_xdvx, 0, var_osiz, var_wnki)
        var_llti = var_zbxo(var_wnki)
        arg_ihhe._calculate_subtree_size(arg_xdvx, var_ayzf)
        var_egyk.append(var_wnki[0])
        var_dcmd.append(var_wnki[-1])
        for var_rdmc in var_rjut(1, var_llti):
            var_egyk.append(var_lsgw(var_egyk[var_rdmc - 1], var_wnki[
                var_rdmc]))
            var_dcmd.append(var_lsgw(var_dcmd[var_rdmc - 1], var_wnki[
                var_llti - var_rdmc - 1]))
        var_dcmd.reverse()
        var_cbvh = []
        for var_yjch in arg_rcsn:
            var_dmio = var_osiz[var_yjch] - 1
            var_ulfl = var_dmio + 1 + var_ayzf[var_yjch]
            var_lgvi = var_egyk[var_dmio]
            if var_ulfl < var_llti:
                var_lgvi = var_lsgw(var_lgvi, var_dcmd[var_ulfl])
            var_cbvh.append(var_lgvi)
        return var_cbvh

    def func_wvuc(arg_ihhe, arg_xdvx, arg_tufr, var_osiz, var_wnki):
        if not arg_xdvx:
            return
        var_osiz[arg_xdvx.val] = var_zbxo(var_wnki)
        var_wnki.append(arg_tufr)
        arg_ihhe._dfs(arg_xdvx.left, arg_tufr + 1, var_osiz, var_wnki)
        arg_ihhe._dfs(arg_xdvx.right, arg_tufr + 1, var_osiz, var_wnki)

    def func_xhfo(arg_ihhe, arg_xdvx, var_ayzf):
        if not arg_xdvx:
            return 0
        var_miuw = arg_ihhe._calculate_subtree_size(arg_xdvx.left, var_ayzf)
        var_rhvk = arg_ihhe._calculate_subtree_size(arg_xdvx.right, var_ayzf)
        var_yybh = var_miuw + var_rhvk + 1
        var_ayzf[arg_xdvx.val] = var_yybh
        return var_yybh
