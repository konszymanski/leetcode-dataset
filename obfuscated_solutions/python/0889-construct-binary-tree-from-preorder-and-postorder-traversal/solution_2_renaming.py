class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_egyk[var_dcmd]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (var_rgwu + 1)
        for var_ayzf in var_wnki(var_rgwu):
            var_osiz[arg_rcsn[var_ayzf]] = var_ayzf
        return arg_ihhe._construct_tree(0, var_rgwu - 1, 0, arg_xdvx, var_osiz)

    def func_llti(arg_ihhe, arg_zbxo: var_hqta, arg_rdmc: var_hqta,
        arg_rjut: var_hqta, arg_xdvx: var_bacg[var_hqta], var_osiz:
        var_bacg[var_hqta]) ->var_egyk[var_dcmd]:
        if arg_zbxo > arg_rdmc:
            return None
        if arg_zbxo == arg_rdmc:
            return var_dcmd(arg_xdvx[arg_zbxo])
        var_lsgw = arg_xdvx[arg_zbxo + 1]
        var_cbvh = var_osiz[var_lsgw] - arg_rjut + 1
        var_yjch = var_dcmd(arg_xdvx[arg_zbxo])
        var_yjch.left = arg_ihhe._construct_tree(arg_zbxo + 1, arg_zbxo +
            var_cbvh, arg_rjut, arg_xdvx, var_osiz)
        var_yjch.right = arg_ihhe._construct_tree(arg_zbxo + var_cbvh + 1,
            arg_rdmc, arg_rjut + var_cbvh, arg_xdvx, var_osiz)
        return var_yjch
