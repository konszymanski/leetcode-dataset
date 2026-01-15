class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_dcmd[var_egyk]:
        var_bacg = []
        var_hqta = 0
        while var_hqta < var_rgwu(arg_xdvx):
            var_wrnh = 0
            while var_hqta < var_rgwu(arg_xdvx) and arg_xdvx[var_hqta] == '-':
                var_wrnh += 1
                var_hqta += 1
            var_osiz = 0
            while var_hqta < var_rgwu(arg_xdvx) and arg_xdvx[var_hqta].isdigit(
                ):
                var_osiz = var_osiz * 10 + var_ayzf(arg_xdvx[var_hqta])
                var_hqta += 1
            var_wnki = var_egyk(var_osiz)
            while var_rgwu(var_bacg) > var_wrnh:
                var_bacg.pop()
            if var_bacg:
                if var_bacg[-1].left is None:
                    var_bacg[-1].left = var_wnki
                else:
                    var_bacg[-1].right = var_wnki
            var_bacg.append(var_wnki)
        return var_bacg[0]
