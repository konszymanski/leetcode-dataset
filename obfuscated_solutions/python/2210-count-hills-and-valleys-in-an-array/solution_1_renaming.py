class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in var_ayzf(1, var_rgwu - 1):
            if arg_xdvx[var_osiz] == arg_xdvx[var_osiz - 1]:
                continue
            var_wnki = 0
            for var_egyk in var_ayzf(var_osiz - 1, -1, -1):
                if arg_xdvx[var_egyk] > arg_xdvx[var_osiz]:
                    var_wnki = 1
                    break
                elif arg_xdvx[var_egyk] < arg_xdvx[var_osiz]:
                    var_wnki = -1
                    break
            var_dcmd = 0
            for var_egyk in var_ayzf(var_osiz + 1, var_rgwu):
                if arg_xdvx[var_egyk] > arg_xdvx[var_osiz]:
                    var_dcmd = 1
                    break
                elif arg_xdvx[var_egyk] < arg_xdvx[var_osiz]:
                    var_dcmd = -1
                    break
            if var_wnki == var_dcmd and var_wnki != 0:
                var_hqta += 1
        return var_hqta
