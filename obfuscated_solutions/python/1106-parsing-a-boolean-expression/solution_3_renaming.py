class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = var_hqta()
        for var_rgwu in arg_xdvx:
            if var_rgwu == ')':
                values = []
                while var_bacg[-1] != '(':
                    values.append(var_bacg.pop())
                var_bacg.pop()
                var_wrnh = var_bacg.pop()
                var_osiz = arg_ihhe._evaluate_sub_expr(var_wrnh, values)
                var_bacg.append(var_osiz)
            elif var_rgwu != ',':
                var_bacg.append(var_rgwu)
        return var_bacg[-1] == 't'

    def func_wnki(arg_ihhe, var_wrnh, arg_egyk):
        if var_wrnh == '!':
            return 'f' if values[0] == 't' else 't'
        if var_wrnh == '&':
            for var_dcmd in values:
                if var_dcmd == 'f':
                    return 'f'
            return 't'
        if var_wrnh == '|':
            for var_dcmd in values:
                if var_dcmd == 't':
                    return 't'
            return 'f'
        return 'f'
