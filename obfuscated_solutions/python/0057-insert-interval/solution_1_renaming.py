class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_bacg[var_hqta]]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = []
        while var_osiz < var_rgwu and arg_xdvx[var_osiz][1] < arg_rcsn[0]:
            var_ayzf.append(arg_xdvx[var_osiz])
            var_osiz += 1
        while var_osiz < var_rgwu and arg_rcsn[1] >= arg_xdvx[var_osiz][0]:
            arg_rcsn[0] = var_wnki(arg_rcsn[0], arg_xdvx[var_osiz][0])
            arg_rcsn[1] = var_egyk(arg_rcsn[1], arg_xdvx[var_osiz][1])
            var_osiz += 1
        var_ayzf.append(arg_rcsn)
        while var_osiz < var_rgwu:
            var_ayzf.append(arg_xdvx[var_osiz])
            var_osiz += 1
        return var_ayzf
