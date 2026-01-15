class SegTree:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.n = var_rcsn(arg_xdvx)
        var_bacg = 2 << (arg_ihhe.n - 1).bit_length()
        arg_ihhe.seg = [0] * var_bacg
        arg_ihhe._build(arg_xdvx, 1, 0, arg_ihhe.n - 1)

    def func_hqta(arg_ihhe, arg_rgwu):
        arg_ihhe.seg[arg_rgwu] = var_wrnh(arg_ihhe.seg[arg_rgwu * 2],
            arg_ihhe.seg[arg_rgwu * 2 + 1])

    def func_osiz(arg_ihhe, arg_ayzf, arg_rgwu, arg_wnki, arg_egyk):
        if arg_wnki == arg_egyk:
            arg_ihhe.seg[arg_rgwu] = arg_ayzf[arg_wnki]
            return
        var_dcmd = (arg_wnki + arg_egyk) // 2
        arg_ihhe._build(arg_ayzf, arg_rgwu * 2, arg_wnki, var_dcmd)
        arg_ihhe._build(arg_ayzf, arg_rgwu * 2 + 1, var_dcmd + 1, arg_egyk)
        arg_ihhe._maintain(arg_rgwu)

    def func_llti(arg_ihhe, arg_rgwu, arg_wnki, arg_egyk, arg_zbxo):
        if arg_ihhe.seg[arg_rgwu] < arg_zbxo:
            return -1
        if arg_wnki == arg_egyk:
            arg_ihhe.seg[arg_rgwu] = -1
            return arg_wnki
        var_dcmd = (arg_wnki + arg_egyk) // 2
        var_rdmc = arg_ihhe.find_first_and_update(arg_rgwu * 2, arg_wnki,
            var_dcmd, arg_zbxo)
        if var_rdmc == -1:
            var_rdmc = arg_ihhe.find_first_and_update(arg_rgwu * 2 + 1, 
                var_dcmd + 1, arg_egyk, arg_zbxo)
        arg_ihhe._maintain(arg_rgwu)
        return var_rdmc


class Solution:

    def func_rjut(arg_ihhe, arg_lsgw: var_cbvh[var_yjch], arg_xdvx:
        var_cbvh[var_yjch]) ->var_yjch:
        var_dcmd = var_rcsn(arg_xdvx)
        if var_dcmd == 0:
            return var_rcsn(arg_lsgw)
        var_dmio = var_ulfl(arg_xdvx)
        var_lgvi = 0
        for var_wvuc in arg_lsgw:
            if var_dmio.find_first_and_update(1, 0, var_dcmd - 1, var_wvuc
                ) == -1:
                var_lgvi += 1
        return var_lgvi
