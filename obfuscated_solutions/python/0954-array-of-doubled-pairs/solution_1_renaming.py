class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta.Counter(arg_rcsn)
        for var_rgwu in var_wrnh(arg_rcsn, key=var_osiz):
            if var_bacg[var_rgwu] == 0:
                continue
            if var_bacg[2 * var_rgwu] == 0:
                return False
            var_bacg[var_rgwu] -= 1
            var_bacg[2 * var_rgwu] -= 1
        return True
