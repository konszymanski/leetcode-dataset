class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx[0]).count('1')
        var_hqta = arg_xdvx[0]
        var_rgwu = arg_xdvx[0]
        var_wrnh = var_osiz('-inf')
        for var_ayzf in var_wnki(1, var_egyk(arg_xdvx)):
            if var_bacg(arg_xdvx[var_ayzf]).count('1') == var_rcsn:
                var_hqta = var_dcmd(var_hqta, arg_xdvx[var_ayzf])
                var_rgwu = var_llti(var_rgwu, arg_xdvx[var_ayzf])
            else:
                if var_rgwu < var_wrnh:
                    return False
                var_wrnh = var_hqta
                var_hqta = arg_xdvx[var_ayzf]
                var_rgwu = arg_xdvx[var_ayzf]
                var_rcsn = var_bacg(arg_xdvx[var_ayzf]).count('1')
        if var_rgwu < var_wrnh:
            return False
        return True
