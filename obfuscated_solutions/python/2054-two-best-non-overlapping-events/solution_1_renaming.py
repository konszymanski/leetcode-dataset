class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_xdvx.sort()
        var_rcsn = [([-1] * 3) for var_bacg in var_hqta(var_rgwu(arg_xdvx))]
        return arg_ihhe.find_events(arg_xdvx, 0, 0, var_rcsn)

    def func_wrnh(arg_ihhe, arg_xdvx, arg_osiz, arg_ayzf, var_rcsn):
        if arg_ayzf == 2 or arg_osiz >= var_rgwu(arg_xdvx):
            return 0
        if var_rcsn[arg_osiz][arg_ayzf] == -1:
            var_wnki = arg_xdvx[arg_osiz][1]
            var_egyk, var_dcmd = arg_osiz + 1, var_rgwu(arg_xdvx) - 1
            while var_egyk < var_dcmd:
                var_llti = var_egyk + (var_dcmd - var_egyk >> 1)
                if arg_xdvx[var_llti][0] > var_wnki:
                    var_dcmd = var_llti
                else:
                    var_egyk = var_llti + 1
            var_zbxo = arg_xdvx[arg_osiz][2] + (arg_ihhe.find_events(
                arg_xdvx, var_egyk, arg_ayzf + 1, var_rcsn) if var_egyk <
                var_rgwu(arg_xdvx) and arg_xdvx[var_egyk][0] > var_wnki else 0)
            var_rdmc = arg_ihhe.find_events(arg_xdvx, arg_osiz + 1,
                arg_ayzf, var_rcsn)
            var_rcsn[arg_osiz][arg_ayzf] = var_rjut(var_zbxo, var_rdmc)
        return var_rcsn[arg_osiz][arg_ayzf]
