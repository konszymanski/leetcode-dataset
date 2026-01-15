class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->None:
        """
        Do not return anything, modify arr in-place instead.
        """
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx) - 1
        for var_osiz in var_ayzf(var_rgwu + 1):
            if var_osiz > var_rgwu - var_hqta:
                break
            if arg_xdvx[var_osiz] == 0:
                if var_osiz == var_rgwu - var_hqta:
                    arg_xdvx[var_rgwu] = 0
                    var_rgwu -= 1
                    break
                var_hqta += 1
        var_wnki = var_rgwu - var_hqta
        for var_egyk in var_ayzf(var_wnki, -1, -1):
            if arg_xdvx[var_egyk] == 0:
                arg_xdvx[var_egyk + var_hqta] = 0
                var_hqta -= 1
                arg_xdvx[var_egyk + var_hqta] = 0
            else:
                arg_xdvx[var_egyk + var_hqta] = arg_xdvx[var_egyk]
