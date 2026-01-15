class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu: var_wrnh[var_hqta, var_osiz[var_hqta]] = {}
        arg_ihhe.convert(arg_xdvx, 0, var_rgwu)
        var_ayzf = var_wnki([arg_rcsn])
        var_egyk = 0
        var_dcmd = {arg_rcsn}
        while var_ayzf:
            var_llti = var_zbxo(var_ayzf)
            while var_llti > 0:
                var_rdmc = var_ayzf.popleft()
                for var_rjut in var_rgwu[var_rdmc]:
                    if var_rjut not in var_dcmd:
                        var_dcmd.add(var_rjut)
                        var_ayzf.append(var_rjut)
                var_llti -= 1
            var_egyk += 1
        return var_egyk - 1

    def func_lsgw(arg_ihhe, var_rdmc: var_bacg, arg_cbvh: var_hqta,
        var_rgwu: var_wrnh[var_hqta, var_osiz[var_hqta]]):
        if var_rdmc is None:
            return
        if var_rdmc.val not in var_rgwu:
            var_rgwu[var_rdmc.val] = var_yjch()
        var_dmio = var_rgwu[var_rdmc.val]
        if arg_cbvh != 0:
            var_dmio.add(arg_cbvh)
        if var_rdmc.left:
            var_dmio.add(var_rdmc.left.val)
        if var_rdmc.right:
            var_dmio.add(var_rdmc.right.val)
        arg_ihhe.convert(var_rdmc.left, var_rdmc.val, var_rgwu)
        arg_ihhe.convert(var_rdmc.right, var_rdmc.val, var_rgwu)
