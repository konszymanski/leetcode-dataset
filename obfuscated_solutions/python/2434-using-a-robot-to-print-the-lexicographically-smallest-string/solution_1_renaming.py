class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = []
        var_wrnh = []
        var_osiz = 'a'
        for var_ayzf in arg_xdvx:
            var_rgwu.append(var_ayzf)
            var_bacg[var_ayzf] -= 1
            while var_osiz != 'z' and var_bacg[var_osiz] == 0:
                var_osiz = var_wnki(var_egyk(var_osiz) + 1)
            while var_rgwu and var_rgwu[-1] <= var_osiz:
                var_wrnh.append(var_rgwu.pop())
        return ''.join(var_wrnh)
