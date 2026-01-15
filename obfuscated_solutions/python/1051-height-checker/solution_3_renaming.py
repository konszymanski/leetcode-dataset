class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta, var_rgwu, var_wrnh = (arg_bacg, 2 * arg_bacg + 1, 2 *
            arg_bacg + 2)
        if var_rgwu < arg_rcsn and arg_xdvx[var_rgwu] > arg_xdvx[var_hqta]:
            var_hqta = var_rgwu
        if var_wrnh < arg_rcsn and arg_xdvx[var_wrnh] > arg_xdvx[var_hqta]:
            var_hqta = var_wrnh
        if var_hqta != arg_bacg:
            arg_xdvx[arg_bacg], arg_xdvx[var_hqta] = arg_xdvx[var_hqta
                ], arg_xdvx[arg_bacg]
            arg_ihhe.heapify(arg_xdvx, arg_rcsn, var_hqta)

    def func_osiz(arg_ihhe, arg_xdvx):
        arg_rcsn = var_ayzf(arg_xdvx)
        for arg_bacg in var_wnki(arg_rcsn // 2 - 1, -1, -1):
            arg_ihhe.heapify(arg_xdvx, arg_rcsn, arg_bacg)
        for arg_bacg in var_wnki(arg_rcsn - 1, 0, -1):
            arg_xdvx[0], arg_xdvx[arg_bacg] = arg_xdvx[arg_bacg], arg_xdvx[0]
            arg_ihhe.heapify(arg_xdvx, arg_bacg, 0)

    def func_egyk(arg_ihhe, arg_dcmd: var_llti[var_zbxo]) ->var_zbxo:
        var_rdmc = arg_dcmd[:]
        arg_ihhe.heap_sort(var_rdmc)
        var_rjut = 0
        for arg_bacg in var_wnki(var_ayzf(var_rdmc)):
            if arg_dcmd[arg_bacg] != var_rdmc[arg_bacg]:
                var_rjut += 1
        return var_rjut
