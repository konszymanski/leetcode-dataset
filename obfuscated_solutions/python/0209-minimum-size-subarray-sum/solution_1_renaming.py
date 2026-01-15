class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_bacg:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = var_wnki('inf')
        for var_wrnh in var_egyk(0, var_dcmd(arg_rcsn)):
            var_osiz += arg_rcsn[var_wrnh]
            while var_osiz >= arg_xdvx:
                var_ayzf = var_llti(var_ayzf, var_wrnh - var_rgwu + 1)
                var_osiz -= arg_rcsn[var_rgwu]
                var_rgwu += 1
        return var_ayzf if var_ayzf != var_wnki('inf') else 0
