class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = var_rgwu(var_bacg) - 1
        for var_wrnh, var_osiz in var_ayzf(arg_rcsn):
            if var_osiz.isalpha():
                while not arg_rcsn[var_hqta].isalpha():
                    var_hqta -= 1
                var_bacg.append(arg_rcsn[var_hqta])
                var_hqta -= 1
            else:
                var_bacg.append(var_osiz)
        return ''.join(var_bacg)
