class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = [False] * var_hqta(arg_rcsn)
        var_bacg[0] = True
        var_rgwu = [0]
        while var_rgwu:
            var_wrnh = var_rgwu.pop()
            for var_osiz in arg_rcsn[var_wrnh]:
                if not var_bacg[var_osiz]:
                    var_bacg[var_osiz] = True
                    var_rgwu.append(var_osiz)
        return var_ayzf(var_bacg)
