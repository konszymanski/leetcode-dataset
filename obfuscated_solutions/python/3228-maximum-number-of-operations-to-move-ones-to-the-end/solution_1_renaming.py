class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = 0
        while var_rgwu < var_wrnh(arg_xdvx):
            if arg_xdvx[var_rgwu] == '0':
                while var_rgwu + 1 < var_wrnh(arg_xdvx) and arg_xdvx[
                    var_rgwu + 1] == '0':
                    var_rgwu += 1
                var_hqta += var_bacg
            else:
                var_bacg += 1
            var_rgwu += 1
        return var_hqta
