class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        arg_xdvx.sort()
        var_wrnh = 0
        var_osiz = var_ayzf(var_rgwu)
        var_wnki = var_egyk()

        def func_dcmd(arg_llti):
            var_wnki.add(arg_llti)
            if arg_llti - arg_rcsn >= arg_xdvx[0]:
                var_wnki.add(arg_llti - arg_rcsn)
            if arg_llti + arg_rcsn <= arg_xdvx[-1]:
                var_wnki.add(arg_llti + arg_rcsn)
        var_zbxo = 0
        for var_rdmc in var_rjut(var_lsgw(arg_xdvx)):
            if arg_xdvx[var_rdmc] != arg_xdvx[var_zbxo]:
                var_osiz[arg_xdvx[var_zbxo]] = var_rdmc - var_zbxo
                var_wrnh = var_cbvh(var_wrnh, var_rdmc - var_zbxo)
                func_dcmd(arg_xdvx[var_zbxo])
                var_zbxo = var_rdmc
        var_osiz[arg_xdvx[var_zbxo]] = var_lsgw(arg_xdvx) - var_zbxo
        var_wrnh = var_cbvh(var_wrnh, var_lsgw(arg_xdvx) - var_zbxo)
        func_dcmd(arg_xdvx[var_zbxo])
        for var_yjch in var_dmio(var_wnki):
            var_ulfl = var_lgvi.bisect_left(arg_xdvx, var_yjch - arg_rcsn)
            var_wvuc = var_lgvi.bisect_right(arg_xdvx, var_yjch + arg_rcsn) - 1
            if var_yjch in var_osiz:
                var_tufr = var_xhfo(var_wvuc - var_ulfl + 1, var_osiz[
                    var_yjch] + arg_bacg)
            else:
                var_tufr = var_xhfo(var_wvuc - var_ulfl + 1, arg_bacg)
            var_wrnh = var_cbvh(var_wrnh, var_tufr)
        return var_wrnh
