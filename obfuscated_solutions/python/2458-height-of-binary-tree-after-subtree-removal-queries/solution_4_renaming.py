class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_wrnh]:
        var_osiz = []
        var_ayzf = {}
        var_wnki = {}
        var_egyk = {}

        def func_dcmd(arg_xdvx, arg_llti):
            if not arg_xdvx:
                return
            var_ayzf[arg_xdvx.val] = arg_llti
            var_wnki[arg_xdvx.val] = var_zbxo(var_osiz)
            var_osiz.append(arg_xdvx.val)
            func_dcmd(arg_xdvx.left, arg_llti + 1)
            func_dcmd(arg_xdvx.right, arg_llti + 1)
            var_egyk[arg_xdvx.val] = var_zbxo(var_osiz)
            var_osiz.append(arg_xdvx.val)
        func_dcmd(arg_xdvx, 0)
        var_rdmc = var_zbxo(var_osiz)
        var_rjut = [0] * var_rdmc
        var_lsgw = [0] * var_rdmc
        var_rjut[0] = var_lsgw[-1] = var_ayzf[arg_xdvx.val]
        for var_cbvh in var_yjch(1, var_rdmc):
            var_rjut[var_cbvh] = var_dmio(var_rjut[var_cbvh - 1], var_ayzf[
                var_osiz[var_cbvh]])
        for var_cbvh in var_yjch(var_rdmc - 2, -1, -1):
            var_lsgw[var_cbvh] = var_dmio(var_lsgw[var_cbvh + 1], var_ayzf[
                var_osiz[var_cbvh]])
        return [var_dmio(var_rjut[var_wnki[var_ulfl] - 1] if var_wnki[
            var_ulfl] > 0 else 0, var_lsgw[var_egyk[var_ulfl] + 1] if 
            var_egyk[var_ulfl] < var_rdmc - 1 else 0) for var_ulfl in arg_rcsn]
