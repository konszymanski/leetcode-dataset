class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx) - 1
        while var_hqta < var_rgwu:
            var_osiz = (var_hqta + var_rgwu) // 2
            if arg_xdvx[var_osiz] < arg_xdvx[var_osiz + 1]:
                var_hqta = var_osiz + 1
            else:
                var_rgwu = var_osiz
        return var_hqta
