class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        if arg_hqta[arg_xdvx]:
            return True
        if arg_bacg[arg_xdvx]:
            return False
        arg_bacg[arg_xdvx] = True
        arg_hqta[arg_xdvx] = True
        for var_rgwu in arg_rcsn[arg_xdvx]:
            if arg_ihhe.dfs(var_rgwu, arg_rcsn, arg_bacg, arg_hqta):
                return True
        arg_hqta[arg_xdvx] = False
        return False

    def func_wrnh(arg_ihhe, arg_osiz: var_ayzf[var_ayzf[var_wnki]]) ->var_ayzf[
        var_wnki]:
        var_egyk = var_dcmd(arg_osiz)
        arg_bacg = [False] * var_egyk
        arg_hqta = [False] * var_egyk
        for var_llti in var_zbxo(var_egyk):
            arg_ihhe.dfs(var_llti, arg_osiz, arg_bacg, arg_hqta)
        var_rdmc = []
        for var_llti in var_zbxo(var_egyk):
            if not arg_hqta[var_llti]:
                var_rdmc.append(var_llti)
        return var_rdmc
