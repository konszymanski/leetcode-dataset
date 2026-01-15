class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_egyk:
        var_hqta = []
        var_rgwu = 1
        var_wrnh = 0
        for var_rgwu in var_osiz(var_ayzf(arg_xdvx)):
            if arg_xdvx[var_rgwu] < arg_xdvx[var_rgwu - 1]:
                if var_wrnh < var_rgwu - 1:
                    var_hqta.append((arg_xdvx[var_wrnh], arg_xdvx[var_rgwu -
                        1]))
                var_wrnh = var_rgwu
            for var_wnki in var_hqta:
                if var_wnki[0] < arg_xdvx[var_rgwu] < var_wnki[1]:
                    return True
        return False
