class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = 0
        var_hqta = {(0): -1}
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            var_bacg = (var_bacg + arg_xdvx[var_rgwu]) % arg_rcsn
            if var_bacg in var_hqta:
                if var_rgwu - var_hqta[var_bacg] > 1:
                    return True
            else:
                var_hqta[var_bacg] = var_rgwu
        return False
