class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = 10 ** 9 + 7
        var_hqta = var_rgwu(arg_rcsn)
        arg_rcsn.sort()
        var_wrnh = [1]
        for var_osiz in var_ayzf(1, var_hqta):
            var_wrnh.append(var_wrnh[-1] * 2 % var_bacg)
        var_wnki = 0
        for var_osiz, var_egyk in var_dcmd(arg_rcsn):
            var_wnki = (var_wnki + (var_wrnh[var_osiz] - var_wrnh[var_hqta -
                1 - var_osiz]) * var_egyk) % var_bacg
        return var_wnki
