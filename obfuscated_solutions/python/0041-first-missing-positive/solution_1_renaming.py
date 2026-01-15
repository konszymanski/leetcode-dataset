class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = [False] * (var_rcsn + 1)
        for var_rgwu in arg_xdvx:
            if 0 < var_rgwu <= var_rcsn:
                var_hqta[var_rgwu] = True
        for var_wrnh in var_osiz(1, var_rcsn + 1):
            if not var_hqta[var_wrnh]:
                return var_wrnh
        return var_rcsn + 1
