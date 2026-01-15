class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz, var_ayzf = 0, -1
        var_wnki = var_egyk()
        var_dcmd = 0
        for var_llti in var_zbxo(var_rgwu):
            while var_osiz < arg_rcsn and var_ayzf + 1 < var_rgwu:
                var_ayzf += 1
                var_osiz += var_wnki[arg_xdvx[var_ayzf]]
                var_wnki[arg_xdvx[var_ayzf]] += 1
            if var_osiz >= arg_rcsn:
                var_dcmd += var_rgwu - var_ayzf
            var_wnki[arg_xdvx[var_llti]] -= 1
            var_osiz -= var_wnki[arg_xdvx[var_llti]]
        return var_dcmd
