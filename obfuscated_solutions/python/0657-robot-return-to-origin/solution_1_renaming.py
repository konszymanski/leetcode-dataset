class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta = 0
        for var_rgwu in arg_rcsn:
            if var_rgwu == 'U':
                var_hqta -= 1
            elif var_rgwu == 'D':
                var_hqta += 1
            elif var_rgwu == 'L':
                var_bacg -= 1
            elif var_rgwu == 'R':
                var_bacg += 1
        return var_bacg == var_hqta == 0
