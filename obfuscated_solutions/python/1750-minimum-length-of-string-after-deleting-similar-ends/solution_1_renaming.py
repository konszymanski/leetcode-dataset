class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = 0
        var_hqta = var_rgwu(arg_xdvx) - 1
        while var_bacg < var_hqta and arg_xdvx[var_bacg] == arg_xdvx[var_hqta]:
            var_wrnh = arg_xdvx[var_bacg]
            while var_bacg <= var_hqta and arg_xdvx[var_bacg] == var_wrnh:
                var_bacg += 1
            while var_hqta > var_bacg and arg_xdvx[var_hqta] == var_wrnh:
                var_hqta -= 1
        return var_hqta - var_bacg + 1
