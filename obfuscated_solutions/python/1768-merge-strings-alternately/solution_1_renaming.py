class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = var_rgwu(arg_bacg)
        var_osiz = 0
        var_ayzf = 0
        var_wnki = []
        while var_osiz < var_hqta or var_ayzf < var_wrnh:
            if var_osiz < var_hqta:
                var_wnki += arg_rcsn[var_osiz]
                var_osiz += 1
            if var_ayzf < var_wrnh:
                var_wnki += arg_bacg[var_ayzf]
                var_ayzf += 1
        return ''.join(var_wnki)
