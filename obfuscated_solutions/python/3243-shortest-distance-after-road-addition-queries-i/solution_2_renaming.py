class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        if arg_bacg == arg_rcsn - 1:
            return 0
        if arg_hqta[arg_bacg] != -1:
            return arg_hqta[arg_bacg]
        var_rgwu = arg_rcsn
        for var_wrnh in arg_xdvx[arg_bacg]:
            var_rgwu = var_osiz(var_rgwu, arg_ihhe.find_min_distance(
                arg_xdvx, arg_rcsn, var_wrnh, arg_hqta) + 1)
        arg_hqta[arg_bacg] = var_rgwu
        return var_rgwu

    def func_ayzf(arg_ihhe, arg_rcsn, arg_wnki):
        arg_hqta = [-1] * arg_rcsn
        arg_xdvx = [[] for var_egyk in var_dcmd(arg_rcsn)]
        for var_llti in var_dcmd(arg_rcsn - 1):
            arg_xdvx[var_llti].append(var_llti + 1)
        var_zbxo = []
        for var_rdmc in arg_wnki:
            var_rjut = var_rdmc[0]
            var_lsgw = var_rdmc[1]
            arg_xdvx[var_rjut].append(var_lsgw)
            var_zbxo.append(arg_ihhe.find_min_distance(arg_xdvx, arg_rcsn, 
                0, arg_hqta))
            arg_hqta = [-1] * arg_rcsn
        return var_zbxo
