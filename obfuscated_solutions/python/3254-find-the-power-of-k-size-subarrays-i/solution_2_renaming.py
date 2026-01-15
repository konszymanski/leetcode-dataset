class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [-1] * (var_rgwu - arg_rcsn + 1)
        var_ayzf = var_wnki.deque()
        for var_egyk in var_dcmd(var_rgwu):
            if var_ayzf and var_ayzf[0] < var_egyk - arg_rcsn + 1:
                var_ayzf.popleft()
            if var_ayzf and arg_xdvx[var_egyk] != arg_xdvx[var_egyk - 1] + 1:
                var_ayzf.clear()
            var_ayzf.append(var_egyk)
            if var_egyk >= arg_rcsn - 1:
                if var_wrnh(var_ayzf) == arg_rcsn:
                    var_osiz[var_egyk - arg_rcsn + 1] = arg_xdvx[var_ayzf[-1]]
                else:
                    var_osiz[var_egyk - arg_rcsn + 1] = -1
        return var_osiz
