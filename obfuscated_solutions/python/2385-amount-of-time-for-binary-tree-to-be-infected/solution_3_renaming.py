class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.max_distance = 0

    def func_xdvx(arg_ihhe, arg_rcsn, arg_bacg):
        arg_ihhe.traverse(arg_rcsn, arg_bacg)
        return arg_ihhe.max_distance

    def func_hqta(arg_ihhe, arg_rcsn, arg_bacg):
        var_rgwu = 0
        if arg_rcsn is None:
            return var_rgwu
        var_wrnh = arg_ihhe.traverse(arg_rcsn.left, arg_bacg)
        var_osiz = arg_ihhe.traverse(arg_rcsn.right, arg_bacg)
        if arg_rcsn.val == arg_bacg:
            arg_ihhe.max_distance = var_ayzf(var_wrnh, var_osiz)
            var_rgwu = -1
        elif var_wrnh >= 0 and var_osiz >= 0:
            var_rgwu = var_ayzf(var_wrnh, var_osiz) + 1
        else:
            var_wnki = var_egyk(var_wrnh) + var_egyk(var_osiz)
            arg_ihhe.max_distance = var_ayzf(arg_ihhe.max_distance, var_wnki)
            var_rgwu = var_dcmd(var_wrnh, var_osiz) - 1
        return var_rgwu
