class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta, arg_rgwu):
        if arg_xdvx == var_wrnh(arg_bacg):
            return 0 if arg_rcsn == 1 else -var_osiz('inf')
        if arg_rgwu[arg_xdvx][arg_rcsn] != -1:
            return arg_rgwu[arg_xdvx][arg_rcsn]
        var_ayzf = arg_bacg[arg_xdvx] + arg_ihhe.maxSumOfNodes(arg_xdvx + 1,
            arg_rcsn, arg_bacg, arg_hqta, arg_rgwu)
        var_wnki = (arg_bacg[arg_xdvx] ^ arg_hqta) + arg_ihhe.maxSumOfNodes(
            arg_xdvx + 1, arg_rcsn ^ 1, arg_bacg, arg_hqta, arg_rgwu)
        arg_rgwu[arg_xdvx][arg_rcsn] = var_egyk(var_wnki, var_ayzf)
        return arg_rgwu[arg_xdvx][arg_rcsn]

    def func_dcmd(arg_ihhe, arg_bacg: var_zbxo[var_rdmc], arg_hqta:
        var_rdmc, arg_llti: var_zbxo[var_zbxo[var_rdmc]]) ->var_rdmc:
        arg_rgwu = [([-1] * 2) for var_rjut in var_lsgw(var_wrnh(arg_bacg))]
        return arg_ihhe.maxSumOfNodes(0, 1, arg_bacg, arg_hqta, arg_rgwu)
