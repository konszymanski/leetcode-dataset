class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = []
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            while var_hqta and var_hqta[-1] > var_wrnh:
                var_hqta.pop()
            if var_wrnh == 0:
                continue
            if not var_hqta or var_hqta[-1] < var_wrnh:
                var_rgwu += 1
                var_hqta.append(var_wrnh)
        return var_rgwu
