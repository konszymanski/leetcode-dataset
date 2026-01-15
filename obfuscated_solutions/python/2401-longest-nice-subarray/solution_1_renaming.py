class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 1
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx) - var_hqta):
            var_ayzf = 1
            var_wnki = arg_xdvx[var_rgwu]
            for var_egyk in var_wrnh(var_rgwu + 1, var_osiz(arg_xdvx)):
                if var_wnki & arg_xdvx[var_egyk] == 0:
                    var_wnki |= arg_xdvx[var_egyk]
                    var_ayzf += 1
                else:
                    break
            var_hqta = var_dcmd(var_hqta, var_ayzf)
        return var_hqta
