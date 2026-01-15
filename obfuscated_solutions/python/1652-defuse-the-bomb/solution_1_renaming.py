class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = [0] * var_wrnh(arg_xdvx)
        if arg_rcsn == 0:
            return var_rgwu
        for var_osiz in var_ayzf(var_wrnh(var_rgwu)):
            if arg_rcsn > 0:
                for var_wnki in var_ayzf(var_osiz + 1, var_osiz + arg_rcsn + 1
                    ):
                    var_rgwu[var_osiz] += arg_xdvx[var_wnki % var_wrnh(
                        arg_xdvx)]
            else:
                for var_wnki in var_ayzf(var_osiz - var_egyk(arg_rcsn),
                    var_osiz):
                    var_rgwu[var_osiz] += arg_xdvx[(var_wnki + var_wrnh(
                        arg_xdvx)) % var_wrnh(arg_xdvx)]
        return var_rgwu
