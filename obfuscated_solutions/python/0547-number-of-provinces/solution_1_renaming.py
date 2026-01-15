class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        arg_bacg[arg_xdvx] = True
        for var_hqta in var_rgwu(var_wrnh(arg_rcsn)):
            if arg_rcsn[arg_xdvx][var_hqta] and not arg_bacg[var_hqta]:
                arg_ihhe.dfs(var_hqta, arg_rcsn, arg_bacg)

    def func_osiz(arg_ihhe, arg_rcsn):
        var_ayzf = var_wrnh(arg_rcsn)
        var_wnki = 0
        arg_bacg = [False] * var_ayzf
        for var_hqta in var_rgwu(var_ayzf):
            if not arg_bacg[var_hqta]:
                var_wnki += 1
                arg_ihhe.dfs(var_hqta, arg_rcsn, arg_bacg)
        return var_wnki
