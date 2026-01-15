class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = False
        for var_osiz in var_ayzf(var_hqta):
            if arg_xdvx[var_osiz] == 1:
                var_wrnh = True
            if arg_xdvx[var_osiz] <= 0 or arg_xdvx[var_osiz] > var_hqta:
                arg_xdvx[var_osiz] = 1
        if not var_wrnh:
            return 1
        for var_osiz in var_ayzf(var_hqta):
            var_wnki = var_egyk(arg_xdvx[var_osiz])
            if var_wnki == var_hqta:
                arg_xdvx[0] = -var_egyk(arg_xdvx[0])
            else:
                arg_xdvx[var_wnki] = -var_egyk(arg_xdvx[var_wnki])
        for var_osiz in var_ayzf(1, var_hqta):
            if arg_xdvx[var_osiz] > 0:
                return var_osiz
        if arg_xdvx[0] > 0:
            return var_hqta
        return var_hqta + 1
