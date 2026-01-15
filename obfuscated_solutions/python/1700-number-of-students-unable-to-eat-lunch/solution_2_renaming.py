class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            if var_osiz == 0:
                var_rgwu += 1
            else:
                var_wrnh += 1
        for var_ayzf in arg_rcsn:
            if var_ayzf == 0 and var_rgwu == 0:
                return var_wrnh
            if var_ayzf == 1 and var_wrnh == 0:
                return var_rgwu
            if var_ayzf == 0:
                var_rgwu -= 1
            else:
                var_wrnh -= 1
        return 0
