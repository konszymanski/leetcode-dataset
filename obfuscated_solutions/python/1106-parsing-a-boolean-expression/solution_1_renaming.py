class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        while var_bacg(arg_xdvx) > 1:
            var_hqta = var_rgwu(arg_xdvx.rfind('!'), arg_xdvx.rfind('&'),
                arg_xdvx.rfind('|'))
            var_wrnh = arg_xdvx.find(')', var_hqta)
            var_osiz = arg_xdvx[var_hqta:var_wrnh + 1]
            var_ayzf = arg_ihhe._evaluate_sub_expr(var_osiz)
            arg_xdvx = arg_xdvx[:var_hqta] + var_ayzf + arg_xdvx[var_wrnh + 1:]
        return arg_xdvx == 't'

    def func_egyk(arg_ihhe, var_osiz: var_rcsn) ->var_rcsn:
        var_dcmd = var_osiz[0]
        values = var_osiz[2:-1]
        if var_dcmd == '!':
            return 'f' if values == 't' else 't'
        if var_dcmd == '&':
            return 'f' if 'f' in values else 't'
        if var_dcmd == '|':
            return 't' if 't' in values else 'f'
        return 'f'
