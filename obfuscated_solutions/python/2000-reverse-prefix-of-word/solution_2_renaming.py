class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = []
        var_rgwu = []
        var_wrnh = 0
        while var_wrnh < var_osiz(arg_xdvx):
            var_hqta.append(arg_xdvx[var_wrnh])
            if arg_xdvx[var_wrnh] == arg_rcsn:
                while var_hqta:
                    var_rgwu.append(var_hqta.pop())
                var_wrnh += 1
                while var_wrnh < var_osiz(arg_xdvx):
                    var_rgwu.append(arg_xdvx[var_wrnh])
                    var_wrnh += 1
                return ''.join(var_rgwu)
            var_wrnh += 1
        return arg_xdvx
