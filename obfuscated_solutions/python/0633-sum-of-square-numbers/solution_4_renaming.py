class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):

        def func_bacg(arg_hqta, arg_rgwu, arg_wrnh):
            if arg_hqta > arg_rgwu:
                return False
            var_osiz = arg_hqta + (arg_rgwu - arg_hqta) // 2
            if var_osiz * var_osiz == arg_wrnh:
                return True
            elif var_osiz * var_osiz > arg_wrnh:
                return func_bacg(arg_hqta, var_osiz - 1, arg_wrnh)
            else:
                return func_bacg(var_osiz + 1, arg_rgwu, arg_wrnh)
        for var_ayzf in var_wnki(var_egyk(arg_rcsn ** 0.5) + 1):
            var_dcmd = arg_rcsn - var_ayzf * var_ayzf
            if func_bacg(0, var_dcmd, var_dcmd):
                return True
        return False
