class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = []
        for var_hqta in arg_rcsn:
            if var_hqta == '+':
                var_bacg.append(var_bacg[-1] + var_bacg[-2])
            elif var_hqta == 'C':
                var_bacg.pop()
            elif var_hqta == 'D':
                var_bacg.append(2 * var_bacg[-1])
            else:
                var_bacg.append(var_rgwu(var_hqta))
        return var_wrnh(var_bacg)
