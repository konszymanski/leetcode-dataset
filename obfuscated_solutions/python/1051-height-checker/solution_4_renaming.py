class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = {}
        var_bacg, var_hqta = var_rgwu(arg_xdvx), var_wrnh(arg_xdvx)
        for var_osiz in arg_xdvx:
            if var_osiz in var_rcsn:
                var_rcsn[var_osiz] += 1
            else:
                var_rcsn[var_osiz] = 1
        var_ayzf = 0
        for var_osiz in var_wnki(var_bacg, var_hqta + 1):
            while var_rcsn.get(var_osiz, 0) > 0:
                arg_xdvx[var_ayzf] = var_osiz
                var_ayzf += 1
                var_rcsn[var_osiz] -= 1

    def func_egyk(arg_ihhe, arg_dcmd: var_llti[var_zbxo]) ->var_zbxo:
        var_rdmc = arg_dcmd[:]
        arg_ihhe.counting_sort(var_rdmc)
        var_rjut = 0
        for var_lsgw in var_wnki(var_cbvh(var_rdmc)):
            if arg_dcmd[var_lsgw] != var_rdmc[var_lsgw]:
                var_rjut += 1
        return var_rjut
