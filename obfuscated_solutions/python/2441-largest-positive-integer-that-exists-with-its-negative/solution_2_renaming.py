class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        arg_xdvx.sort()
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx) - 1
        while var_hqta < var_rgwu:
            if -arg_xdvx[var_hqta] == arg_xdvx[var_rgwu]:
                return arg_xdvx[var_rgwu]
            elif -arg_xdvx[var_hqta] > arg_xdvx[var_rgwu]:
                var_hqta += 1
            else:
                var_rgwu -= 1
        return -1
