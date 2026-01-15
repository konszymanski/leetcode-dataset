class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            var_osiz = var_ayzf(var_wrnh) - var_ayzf('a') + 1
            while var_osiz > 0:
                var_rgwu += var_osiz % 10
                var_osiz //= 10
        for var_wnki in var_egyk(1, arg_rcsn):
            var_dcmd = 0
            while var_rgwu > 0:
                var_dcmd += var_rgwu % 10
                var_rgwu //= 10
            var_rgwu = var_dcmd
            if var_rgwu < 10:
                break
        return var_rgwu
