class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:

        def func_hqta(arg_rgwu):
            if var_wrnh(arg_rgwu) == var_osiz:
                if arg_rgwu not in arg_xdvx:
                    return arg_rgwu
                return ''
            var_ayzf = func_hqta(arg_rgwu + '0')
            if var_ayzf:
                return var_ayzf
            return func_hqta(arg_rgwu + '1')
        var_osiz = var_wrnh(arg_xdvx)
        arg_xdvx = var_wnki(arg_xdvx)
        return func_hqta('')
