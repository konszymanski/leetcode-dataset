class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_wrnh, arg_bacg: var_osiz[var_wrnh]) ->None:
        if arg_xdvx is None:
            return
        if var_ayzf(arg_bacg) == arg_rcsn:
            arg_bacg.append(arg_xdvx.val)
        else:
            arg_bacg[arg_rcsn] += arg_xdvx.val
        arg_ihhe.dfs(arg_xdvx.left, arg_rcsn + 1, arg_bacg)
        arg_ihhe.dfs(arg_xdvx.right, arg_rcsn + 1, arg_bacg)

    def func_wnki(arg_ihhe, arg_egyk: var_hqta[var_rgwu]) ->var_wrnh:
        arg_bacg = []
        arg_ihhe.dfs(arg_egyk, 0, arg_bacg)
        var_dcmd = var_llti('-inf')
        var_zbxo = 0
        for var_rdmc in var_rjut(var_ayzf(arg_bacg)):
            if var_dcmd < arg_bacg[var_rdmc]:
                var_dcmd = arg_bacg[var_rdmc]
                var_zbxo = var_rdmc + 1
        return var_zbxo
