class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = [var_hqta for var_hqta in arg_rcsn if var_hqta.isalpha()]
        var_rgwu = []
        for var_hqta in arg_rcsn:
            if var_hqta.isalpha():
                var_rgwu.append(var_bacg.pop())
            else:
                var_rgwu.append(var_hqta)
        return ''.join(var_rgwu)
