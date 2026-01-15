class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf(arg_xdvx[1:])
        var_wnki = arg_xdvx[0]
        var_egyk = 0
        while var_osiz:
            var_dcmd = var_osiz.popleft()
            if var_wnki > var_dcmd:
                var_osiz.append(var_dcmd)
                var_egyk += 1
            else:
                var_osiz.append(var_wnki)
                var_wnki = var_dcmd
                var_egyk = 1
            if var_egyk == arg_rcsn or var_wnki == var_rgwu:
                return var_wnki
