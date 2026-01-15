class Solution:
    var_udax = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz(arg_rcsn), var_osiz(arg_rcsn[0])
        var_ayzf = 0
        var_wnki = [([var_egyk('inf')] * var_wrnh) for var_dcmd in var_llti
            (var_rgwu)]
        var_zbxo = var_rdmc.deque()
        arg_xdvx._dfs(arg_rcsn, 0, 0, var_wnki, var_ayzf, var_zbxo)
        while var_zbxo:
            var_ayzf += 1
            var_rjut = var_osiz(var_zbxo)
            for var_dcmd in var_llti(var_rjut):
                var_lsgw, var_cbvh = var_zbxo.popleft()
                for var_yjch, (var_dmio, var_ulfl) in var_lgvi(arg_xdvx._dirs):
                    arg_xdvx._dfs(arg_rcsn, var_lsgw + var_dmio, var_cbvh +
                        var_ulfl, var_wnki, var_ayzf, var_zbxo)
        return var_wnki[var_rgwu - 1][var_wrnh - 1]

    def func_wvuc(arg_xdvx, arg_rcsn: var_bacg[var_bacg[var_hqta]],
        var_lsgw: var_hqta, var_cbvh: var_hqta, var_wnki: var_bacg[var_bacg
        [var_hqta]], var_ayzf: var_hqta, var_zbxo: var_rdmc.deque) ->None:
        if not arg_xdvx._is_unvisited(var_wnki, var_lsgw, var_cbvh):
            return
        var_wnki[var_lsgw][var_cbvh] = var_ayzf
        var_zbxo.append((var_lsgw, var_cbvh))
        var_tufr = arg_rcsn[var_lsgw][var_cbvh] - 1
        var_dmio, var_ulfl = arg_xdvx._dirs[var_tufr]
        arg_xdvx._dfs(arg_rcsn, var_lsgw + var_dmio, var_cbvh + var_ulfl,
            var_wnki, var_ayzf, var_zbxo)

    def func_xhfo(arg_xdvx, var_wnki: var_bacg[var_bacg[var_hqta]],
        var_lsgw: var_hqta, var_cbvh: var_hqta) ->var_miuw:
        return 0 <= var_lsgw < var_osiz(var_wnki) and 0 <= var_cbvh < var_osiz(
            var_wnki[0]) and var_wnki[var_lsgw][var_cbvh] == var_egyk('inf')
