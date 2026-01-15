class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_bacg[var_hqta]:
        arg_ihhe._quick_sort(arg_rcsn, arg_xdvx, 0, var_wrnh(arg_rcsn) - 1)
        return arg_xdvx

    def func_osiz(arg_ihhe, arg_rcsn: var_bacg[var_rgwu], arg_xdvx:
        var_bacg[var_hqta], arg_ayzf: var_rgwu, arg_wnki: var_rgwu):
        arg_rcsn[arg_ayzf], arg_rcsn[arg_wnki] = arg_rcsn[arg_wnki], arg_rcsn[
            arg_ayzf]
        arg_xdvx[arg_ayzf], arg_xdvx[arg_wnki] = arg_xdvx[arg_wnki], arg_xdvx[
            arg_ayzf]

    def func_egyk(arg_ihhe, arg_rcsn: var_bacg[var_rgwu], arg_xdvx:
        var_bacg[var_hqta], arg_dcmd: var_rgwu, arg_llti: var_rgwu) ->var_rgwu:
        var_zbxo = arg_rcsn[arg_llti]
        var_rdmc = arg_dcmd - 1
        for var_rjut in var_lsgw(arg_dcmd, arg_llti):
            if arg_rcsn[var_rjut] >= var_zbxo:
                var_rdmc += 1
                arg_ihhe._swap(arg_rcsn, arg_xdvx, var_rdmc, var_rjut)
        arg_ihhe._swap(arg_rcsn, arg_xdvx, var_rdmc + 1, arg_llti)
        return var_rdmc + 1

    def func_cbvh(arg_ihhe, arg_rcsn: var_bacg[var_rgwu], arg_xdvx:
        var_bacg[var_hqta], arg_dcmd: var_rgwu, arg_llti: var_rgwu):
        if arg_dcmd < arg_llti:
            var_yjch = arg_ihhe._partition(arg_rcsn, arg_xdvx, arg_dcmd,
                arg_llti)
            arg_ihhe._quick_sort(arg_rcsn, arg_xdvx, arg_dcmd, var_yjch - 1)
            arg_ihhe._quick_sort(arg_rcsn, arg_xdvx, var_yjch + 1, arg_llti)
