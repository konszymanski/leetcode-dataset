class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx) - 1
        while var_hqta > 0 and arg_xdvx[var_hqta] >= arg_xdvx[var_hqta - 1]:
            var_hqta -= 1
        var_wrnh = var_hqta
        var_osiz = 0
        while var_osiz < var_hqta and (var_osiz == 0 or arg_xdvx[var_osiz -
            1] <= arg_xdvx[var_osiz]):
            while var_hqta < var_rgwu(arg_xdvx) and arg_xdvx[var_osiz
                ] > arg_xdvx[var_hqta]:
                var_hqta += 1
            var_wrnh = var_ayzf(var_wrnh, var_hqta - var_osiz - 1)
            var_osiz += 1
        return var_wrnh
