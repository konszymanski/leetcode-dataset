class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [0] * arg_rcsn
        var_bacg[arg_rcsn - 1] = 0
        for var_hqta in var_rgwu(arg_rcsn - 2, -1, -1):
            var_wrnh = arg_rcsn
            for var_osiz in arg_xdvx[var_hqta]:
                var_wrnh = var_ayzf(var_wrnh, var_bacg[var_osiz] + 1)
            var_bacg[var_hqta] = var_wrnh
        return var_bacg[0]

    def func_wnki(arg_ihhe, arg_rcsn, arg_egyk):
        var_dcmd = []
        arg_xdvx = [[] for var_llti in var_rgwu(arg_rcsn)]
        for var_zbxo in var_rgwu(arg_rcsn - 1):
            arg_xdvx[var_zbxo].append(var_zbxo + 1)
        for var_rdmc in arg_egyk:
            var_rjut, var_lsgw = var_rdmc[0], var_rdmc[1]
            arg_xdvx[var_rjut].append(var_lsgw)
            var_dcmd.append(arg_ihhe.find_min_distance(arg_xdvx, arg_rcsn))
        return var_dcmd
