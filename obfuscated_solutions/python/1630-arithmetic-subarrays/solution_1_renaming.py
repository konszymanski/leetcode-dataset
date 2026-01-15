class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_hqta[var_rgwu]) ->var_hqta[var_zbxo]:

        def func_wrnh(arg_osiz):
            arg_osiz.sort()
            var_ayzf = arg_osiz[1] - arg_osiz[0]
            for var_wnki in var_egyk(2, var_dcmd(arg_osiz)):
                if arg_osiz[var_wnki] - arg_osiz[var_wnki - 1] != var_ayzf:
                    return False
            return True
        var_llti = []
        for var_wnki in var_egyk(var_dcmd(arg_rcsn)):
            arg_osiz = arg_xdvx[arg_rcsn[var_wnki]:arg_bacg[var_wnki] + 1]
            var_llti.append(func_wrnh(arg_osiz))
        return var_llti
