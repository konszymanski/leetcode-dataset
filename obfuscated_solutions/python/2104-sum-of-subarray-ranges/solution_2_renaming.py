class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), 0
        var_osiz = []
        for var_ayzf in var_wnki(var_hqta + 1):
            while var_osiz and (var_ayzf == var_hqta or arg_xdvx[var_osiz[-
                1]] >= arg_xdvx[var_ayzf]):
                var_egyk = var_osiz.pop()
                var_dcmd = -1 if not var_osiz else var_osiz[-1]
                var_rgwu -= arg_xdvx[var_egyk] * (var_egyk - var_dcmd) * (
                    var_ayzf - var_egyk)
            var_osiz.append(var_ayzf)
        var_osiz.clear()
        for var_ayzf in var_wnki(var_hqta + 1):
            while var_osiz and (var_ayzf == var_hqta or arg_xdvx[var_osiz[-
                1]] <= arg_xdvx[var_ayzf]):
                var_egyk = var_osiz.pop()
                var_dcmd = -1 if not var_osiz else var_osiz[-1]
                var_rgwu += arg_xdvx[var_egyk] * (var_egyk - var_dcmd) * (
                    var_ayzf - var_egyk)
            var_osiz.append(var_ayzf)
        return var_rgwu
