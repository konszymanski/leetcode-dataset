class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        arg_rcsn.sort(reverse=True)
        var_osiz = 0
        while var_rgwu > 0:
            var_rgwu -= arg_rcsn[var_osiz]
            var_osiz += 1
        return var_osiz
