class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_llti]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = arg_xdvx.copy()
        var_osiz = var_ayzf(var_bacg)
        for var_wnki in var_egyk(var_hqta):
            var_osiz[var_wrnh[var_wnki]] = var_wnki
        var_wrnh.sort(reverse=True)
        var_dcmd = [' '] * var_hqta
        for var_wnki in var_egyk(var_hqta):
            if var_wnki == 0:
                var_dcmd[var_osiz[var_wrnh[var_wnki]]] = 'Gold Medal'
            elif var_wnki == 1:
                var_dcmd[var_osiz[var_wrnh[var_wnki]]] = 'Silver Medal'
            elif var_wnki == 2:
                var_dcmd[var_osiz[var_wrnh[var_wnki]]] = 'Bronze Medal'
            else:
                var_dcmd[var_osiz[var_wrnh[var_wnki]]] = var_llti(var_wnki + 1)
        return var_dcmd
