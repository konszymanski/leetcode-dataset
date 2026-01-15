class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = 0
        for var_rgwu in var_wrnh(var_rcsn):
            var_osiz = 0
            var_ayzf = 0
            for var_wnki in var_wrnh(var_rcsn):
                if arg_xdvx[var_rgwu][var_wnki]:
                    var_hqta += 1
                var_osiz = var_egyk(var_osiz, arg_xdvx[var_rgwu][var_wnki])
                var_ayzf = var_egyk(var_ayzf, arg_xdvx[var_wnki][var_rgwu])
            var_hqta += var_osiz + var_ayzf
        return var_hqta
        """ Alternative solution:
        ans = sum(map(max, grid))
        ans += sum(map(max, zip(*grid)))
        ans += sum(v > 0 for row in grid for v in row)
        """
