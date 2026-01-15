class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = []
        var_hqta = 0
        while var_hqta < var_rgwu(arg_xdvx):
            var_wrnh = 0
            var_osiz = arg_xdvx[var_hqta]
            while var_hqta < var_rgwu(arg_xdvx) and var_wrnh < 9 and arg_xdvx[
                var_hqta] == var_osiz:
                var_wrnh += 1
                var_hqta += 1
            var_bacg.append(var_rcsn(var_wrnh))
            var_bacg.append(var_osiz)
        return ''.join(var_bacg)
