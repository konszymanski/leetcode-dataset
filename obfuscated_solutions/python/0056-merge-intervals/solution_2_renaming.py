class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        arg_xdvx.sort(key=lambda x: var_hqta[0])
        var_rgwu = []
        for var_wrnh in arg_xdvx:
            if not var_rgwu or var_rgwu[-1][1] < var_wrnh[0]:
                var_rgwu.append(var_wrnh)
            else:
                var_rgwu[-1][1] = var_osiz(var_rgwu[-1][1], var_wrnh[1])
        return var_rgwu
