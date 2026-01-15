class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = var_hqta()
        for var_rgwu in arg_xdvx:
            if var_rgwu == ',' or var_rgwu == '(':
                var_rgwu
            if var_rgwu in ['t', 'f', '!', '&', '|']:
                var_bacg.append(var_rgwu)
            elif var_rgwu == ')':
                var_wrnh = False
                var_osiz = False
                while var_bacg[-1] not in ['!', '&', '|']:
                    var_ayzf = var_bacg.pop()
                    if var_ayzf == 't':
                        var_wrnh = True
                    elif var_ayzf == 'f':
                        var_osiz = True
                var_wnki = var_bacg.pop()
                if var_wnki == '!':
                    var_bacg.append('t' if not var_wrnh else 'f')
                elif var_wnki == '&':
                    var_bacg.append('f' if var_osiz else 't')
                else:
                    var_bacg.append('t' if var_wrnh else 'f')
        return var_bacg[-1] == 't'
