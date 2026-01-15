class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = var_ayzf('-inf')
        for var_wnki in var_egyk(var_hqta):
            var_dcmd = var_llti(arg_xdvx[var_wnki])
            var_osiz = var_zbxo(var_osiz, var_dcmd)
        var_rdmc = var_ayzf('inf')
        for var_wnki in var_egyk(var_rgwu):
            var_rjut = var_zbxo(arg_xdvx[var_lsgw][var_wnki] for var_lsgw in
                var_egyk(var_hqta))
            var_rdmc = var_llti(var_rdmc, var_rjut)
        if var_osiz == var_rdmc:
            return [var_osiz]
        else:
            return []
