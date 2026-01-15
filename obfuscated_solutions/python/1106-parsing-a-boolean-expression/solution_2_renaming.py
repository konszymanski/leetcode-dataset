class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_hqta:
        var_bacg = [0]
        return arg_ihhe._evaluate(arg_xdvx, var_bacg)

    def func_rgwu(arg_ihhe, arg_wrnh: var_rcsn, var_bacg: var_osiz) ->var_hqta:
        var_ayzf = arg_wrnh[var_bacg[0]]
        var_bacg[0] += 1
        if var_ayzf == 't':
            return True
        if var_ayzf == 'f':
            return False
        if var_ayzf == '!':
            var_bacg[0] += 1
            var_wnki = not arg_ihhe._evaluate(arg_wrnh, var_bacg)
            var_bacg[0] += 1
            return var_wnki
        values = []
        var_bacg[0] += 1
        while arg_wrnh[var_bacg[0]] != ')':
            if arg_wrnh[var_bacg[0]] != ',':
                values.append(arg_ihhe._evaluate(arg_wrnh, var_bacg))
            else:
                var_bacg[0] += 1
        var_bacg[0] += 1
        if var_ayzf == '&':
            return var_egyk(values)
        if var_ayzf == '|':
            return var_dcmd(values)
        return False
