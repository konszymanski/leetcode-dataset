class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = var_wrnh = 0
        while var_wrnh < var_bacg:
            var_osiz = var_wrnh
            if var_osiz + 1 < var_bacg and arg_rcsn[var_osiz] < arg_rcsn[
                var_osiz + 1]:
                while var_osiz + 1 < var_bacg and arg_rcsn[var_osiz
                    ] < arg_rcsn[var_osiz + 1]:
                    var_osiz += 1
                if var_osiz + 1 < var_bacg and arg_rcsn[var_osiz] > arg_rcsn[
                    var_osiz + 1]:
                    while var_osiz + 1 < var_bacg and arg_rcsn[var_osiz
                        ] > arg_rcsn[var_osiz + 1]:
                        var_osiz += 1
                    var_rgwu = var_ayzf(var_rgwu, var_osiz - var_wrnh + 1)
            var_wrnh = var_ayzf(var_osiz, var_wrnh + 1)
        return var_rgwu
