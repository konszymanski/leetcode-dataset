class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn['TreeNode']) ->var_llti:
        var_bacg = var_hqta([arg_xdvx])
        var_rgwu = 0
        while var_bacg:
            var_wrnh = var_osiz(var_bacg)
            var_ayzf = []
            for var_wnki in var_egyk(var_wrnh):
                var_dcmd = var_bacg.popleft()
                var_ayzf.append(var_dcmd.val)
                if var_dcmd.left:
                    var_bacg.append(var_dcmd.left)
                if var_dcmd.right:
                    var_bacg.append(var_dcmd.right)
            var_rgwu += arg_ihhe._get_min_swaps(var_ayzf)
        return var_rgwu

    def func_zbxo(arg_ihhe, arg_rdmc: var_rjut) ->var_llti:
        var_lsgw = 0
        var_cbvh = var_yjch(arg_rdmc)
        var_dmio = {var_ulfl: var_lgvi for var_lgvi, var_ulfl in var_wvuc(
            arg_rdmc)}
        for var_tufr in var_egyk(var_osiz(arg_rdmc)):
            if arg_rdmc[var_tufr] != var_cbvh[var_tufr]:
                var_lsgw += 1
                var_xhfo = var_dmio[var_cbvh[var_tufr]]
                var_dmio[arg_rdmc[var_tufr]] = var_xhfo
                arg_rdmc[var_xhfo] = arg_rdmc[var_tufr]
        return var_lsgw
