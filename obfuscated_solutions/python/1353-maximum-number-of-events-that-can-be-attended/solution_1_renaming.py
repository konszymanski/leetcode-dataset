class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(var_ayzf[1] for var_ayzf in arg_xdvx)
        arg_xdvx.sort()
        var_wnki = []
        var_egyk, var_dcmd = 0, 0
        for var_llti in var_zbxo(1, var_wrnh + 1):
            while var_dcmd < var_hqta and arg_xdvx[var_dcmd][0] <= var_llti:
                var_rdmc.heappush(var_wnki, arg_xdvx[var_dcmd][1])
                var_dcmd += 1
            while var_wnki and var_wnki[0] < var_llti:
                var_rdmc.heappop(var_wnki)
            if var_wnki:
                var_rdmc.heappop(var_wnki)
                var_egyk += 1
        return var_egyk
