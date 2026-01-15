class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_bacg:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = ['']
        for var_wnki in var_egyk(var_dcmd(var_rgwu)):
            if arg_xdvx[var_wnki] != '-':
                var_ayzf += arg_xdvx[var_wnki].upper()
                var_osiz = var_osiz + 1
                if var_osiz == arg_rcsn:
                    var_osiz = 0
                    var_ayzf += '-'
        if var_wrnh(var_ayzf) > 0 and var_ayzf[var_wrnh(var_ayzf) - 1] == '-':
            var_ayzf = var_ayzf[:-1]
        var_ayzf = var_ayzf[::-1]
        var_llti = ''.join(var_ayzf)
        return var_llti
