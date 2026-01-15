class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rgwu:
        if not arg_xdvx:
            return 0
        var_hqta = arg_xdvx.val * 2 + arg_ihhe.twice_of_val(arg_xdvx.next)
        arg_xdvx.val = var_hqta % 10
        return var_hqta // 10

    def func_wrnh(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_osiz = arg_ihhe.twice_of_val(arg_xdvx)
        if var_osiz:
            arg_xdvx = var_bacg(var_osiz, arg_xdvx)
        return arg_xdvx
