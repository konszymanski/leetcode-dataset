class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_rcsn
        [var_bacg]]:
        var_hqta = [0] * (var_rgwu(arg_xdvx) + 1)
        var_wrnh = []
        for var_osiz in arg_xdvx:
            if var_hqta[var_osiz] >= var_rgwu(var_wrnh):
                var_wrnh.append([])
            var_wrnh[var_hqta[var_osiz]].append(var_osiz)
            var_hqta[var_osiz] += 1
        return var_wrnh
