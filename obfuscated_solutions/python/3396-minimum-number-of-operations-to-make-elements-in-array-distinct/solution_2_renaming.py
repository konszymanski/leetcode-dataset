class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = [False] * 128
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx) - 1, -1, -1):
            if var_hqta[arg_xdvx[var_rgwu]]:
                return var_rgwu // 3 + 1
            var_hqta[arg_xdvx[var_rgwu]] = True
        return 0
