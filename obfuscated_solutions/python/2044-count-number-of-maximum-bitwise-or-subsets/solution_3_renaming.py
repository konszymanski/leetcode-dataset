class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_hqta |= var_rgwu
        var_wrnh = 1 << var_osiz(arg_xdvx)
        var_ayzf = 0
        for var_wnki in var_egyk(var_wrnh):
            var_dcmd = 0
            for var_llti in var_egyk(var_osiz(arg_xdvx)):
                if var_wnki >> var_llti & 1:
                    var_dcmd |= arg_xdvx[var_llti]
            if var_dcmd == var_hqta:
                var_ayzf += 1
        return var_ayzf
