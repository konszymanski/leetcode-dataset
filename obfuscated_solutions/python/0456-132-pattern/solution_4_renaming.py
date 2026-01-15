class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_dcmd:
        if var_hqta(arg_xdvx) < 3:
            return False
        var_rgwu = []
        var_wrnh = [-1] * var_hqta(arg_xdvx)
        var_wrnh[0] = arg_xdvx[0]
        for var_osiz in var_ayzf(1, var_hqta(arg_xdvx)):
            var_wrnh[var_osiz] = var_wnki(var_wrnh[var_osiz - 1], arg_xdvx[
                var_osiz])
        for var_egyk in var_ayzf(var_hqta(arg_xdvx) - 1, -1, -1):
            if arg_xdvx[var_egyk] <= var_wrnh[var_egyk]:
                continue
            while var_rgwu and var_rgwu[-1] <= var_wrnh[var_egyk]:
                var_rgwu.pop()
            if var_rgwu and var_rgwu[-1] < arg_xdvx[var_egyk]:
                return True
            var_rgwu.append(arg_xdvx[var_egyk])
        return False
