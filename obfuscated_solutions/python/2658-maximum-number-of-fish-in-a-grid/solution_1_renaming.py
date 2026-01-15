class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        if arg_bacg < 0 or arg_bacg >= var_rgwu(arg_xdvx
            ) or arg_hqta < 0 or arg_hqta >= var_rgwu(arg_xdvx[0]) or arg_xdvx[
            arg_bacg][arg_hqta] == 0 or arg_rcsn[arg_bacg][arg_hqta]:
            return 0
        arg_rcsn[arg_bacg][arg_hqta] = True
        return arg_xdvx[arg_bacg][arg_hqta] + arg_ihhe.calculate_fishes(
            arg_xdvx, arg_rcsn, arg_bacg, arg_hqta + 1
            ) + arg_ihhe.calculate_fishes(arg_xdvx, arg_rcsn, arg_bacg, 
            arg_hqta - 1) + arg_ihhe.calculate_fishes(arg_xdvx, arg_rcsn, 
            arg_bacg + 1, arg_hqta) + arg_ihhe.calculate_fishes(arg_xdvx,
            arg_rcsn, arg_bacg - 1, arg_hqta)

    def func_wrnh(arg_ihhe, arg_xdvx):
        var_osiz, var_ayzf = var_rgwu(arg_xdvx), var_rgwu(arg_xdvx[0])
        var_wnki = 0
        arg_rcsn = [([False] * var_ayzf) for var_egyk in var_dcmd(var_osiz)]
        for arg_bacg in var_dcmd(var_osiz):
            for arg_hqta in var_dcmd(var_ayzf):
                if arg_xdvx[arg_bacg][arg_hqta] > 0 and not arg_rcsn[arg_bacg][
                    arg_hqta]:
                    var_wnki = var_llti(var_wnki, arg_ihhe.calculate_fishes
                        (arg_xdvx, arg_rcsn, arg_bacg, arg_hqta))
        return var_wnki
