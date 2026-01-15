class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        from collections import deque
        var_hqta = var_rgwu([arg_xdvx])
        arg_bacg[arg_xdvx] = True
        while var_hqta:
            arg_xdvx = var_hqta.popleft()
            for var_wrnh in var_osiz(var_ayzf(arg_rcsn)):
                if arg_rcsn[arg_xdvx][var_wrnh] == 1 and not arg_bacg[var_wrnh
                    ]:
                    var_hqta.append(var_wrnh)
                    arg_bacg[var_wrnh] = True

    def func_wnki(arg_ihhe, arg_rcsn):
        var_egyk = var_ayzf(arg_rcsn)
        var_dcmd = 0
        arg_bacg = [False] * var_egyk
        for var_wrnh in var_osiz(var_egyk):
            if not arg_bacg[var_wrnh]:
                var_dcmd += 1
                arg_ihhe.bfs(var_wrnh, arg_rcsn, arg_bacg)
        return var_dcmd
