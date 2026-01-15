class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [[] for var_hqta in var_rgwu(arg_xdvx)]
        var_wrnh = [[] for var_hqta in var_rgwu(arg_xdvx)]
        for var_osiz, var_ayzf in arg_rcsn:
            var_bacg[var_osiz].append(var_ayzf)
        for var_wnki in var_rgwu(arg_xdvx):
            arg_ihhe.find_ancestors_DFS(var_wnki, var_bacg, var_wnki, var_wrnh)
        return var_wrnh

    def func_egyk(arg_ihhe, arg_dcmd, var_bacg, arg_llti, var_wrnh):
        for var_zbxo in var_bacg[arg_llti]:
            if not var_wrnh[var_zbxo] or var_wrnh[var_zbxo][-1] != arg_dcmd:
                var_wrnh[var_zbxo].append(arg_dcmd)
                arg_ihhe.find_ancestors_DFS(arg_dcmd, var_bacg, var_zbxo,
                    var_wrnh)
