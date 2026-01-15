class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = [[] for var_hqta in var_rgwu(26)]
        var_wrnh = var_osiz(arg_xdvx)
        for var_ayzf, var_wnki in var_egyk(var_wrnh):
            if var_wnki != '*':
                var_bacg[var_dcmd(var_wnki) - var_dcmd('a')].append(var_ayzf)
            else:
                for var_llti in var_rgwu(26):
                    if var_bacg[var_llti]:
                        var_wrnh[var_bacg[var_llti].pop()] = '*'
                        break
        return ''.join(var_wnki for var_wnki in var_wrnh if var_wnki != '*')
