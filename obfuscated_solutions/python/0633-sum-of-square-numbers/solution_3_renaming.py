class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        while var_rcsn * var_rcsn <= arg_xdvx:
            var_bacg = (arg_xdvx - var_rcsn * var_rcsn) ** 0.5
            if var_bacg == var_hqta(var_bacg):
                return True
            var_rcsn += 1
        return False
