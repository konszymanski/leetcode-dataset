class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        values = arg_xdvx.copy()
        for var_hqta in var_rgwu(var_rcsn):
            for var_wrnh in var_rgwu(var_rcsn - var_hqta - 1):
                if values[var_wrnh] <= values[var_wrnh + 1]:
                    continue
                elif var_osiz(values[var_wrnh]).count('1') == var_osiz(values
                    [var_wrnh + 1]).count('1'):
                    values[var_wrnh], values[var_wrnh + 1] = values[
                        var_wrnh + 1], values[var_wrnh]
                else:
                    return False
        return True
