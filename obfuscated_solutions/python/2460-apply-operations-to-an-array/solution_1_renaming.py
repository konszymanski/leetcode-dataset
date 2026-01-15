class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = []
        for var_osiz in var_ayzf(0, var_hqta - 1):
            if arg_xdvx[var_osiz] == arg_xdvx[var_osiz + 1] and arg_xdvx[
                var_osiz] != 0:
                arg_xdvx[var_osiz] *= 2
                arg_xdvx[var_osiz + 1] = 0
        for var_wnki in arg_xdvx:
            if var_wnki != 0:
                var_wrnh.append(var_wnki)
        while var_rgwu(var_wrnh) < var_hqta:
            var_wrnh.append(0)
        return var_wrnh
