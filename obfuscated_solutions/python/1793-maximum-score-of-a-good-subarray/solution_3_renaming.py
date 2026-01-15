class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = arg_rcsn
        var_ayzf = arg_rcsn
        var_wnki = arg_xdvx[arg_rcsn]
        var_egyk = arg_xdvx[arg_rcsn]
        while var_osiz > 0 or var_ayzf < var_rgwu - 1:
            if (arg_xdvx[var_osiz - 1] if var_osiz else 0) < (arg_xdvx[
                var_ayzf + 1] if var_ayzf < var_rgwu - 1 else 0):
                var_ayzf += 1
                var_egyk = var_dcmd(var_egyk, arg_xdvx[var_ayzf])
            else:
                var_osiz -= 1
                var_egyk = var_dcmd(var_egyk, arg_xdvx[var_osiz])
            var_wnki = var_llti(var_wnki, var_egyk * (var_ayzf - var_osiz + 1))
        return var_wnki
