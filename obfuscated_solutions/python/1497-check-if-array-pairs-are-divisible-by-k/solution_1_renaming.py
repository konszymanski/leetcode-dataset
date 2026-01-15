class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = {}
        for var_hqta in arg_xdvx:
            var_bacg[(var_hqta % arg_rcsn + arg_rcsn) % arg_rcsn
                ] = var_bacg.get((var_hqta % arg_rcsn + arg_rcsn) % arg_rcsn, 0
                ) + 1
        for var_hqta in arg_xdvx:
            var_rgwu = (var_hqta % arg_rcsn + arg_rcsn) % arg_rcsn
            if var_rgwu == 0:
                if var_bacg[var_rgwu] % 2 == 1:
                    return False
            elif var_bacg[var_rgwu] != var_bacg.get(arg_rcsn - var_rgwu, 0):
                return False
        return True
