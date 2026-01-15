class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = []
        arg_hqta.append((arg_rcsn, var_wrnh('inf')))
        var_osiz = var_ayzf = 0
        for var_wnki, var_egyk in arg_hqta:
            arg_bacg -= var_wnki - var_ayzf
            while var_rgwu and arg_bacg < 0:
                arg_bacg += -var_dcmd.heappop(var_rgwu)
                var_osiz += 1
            if arg_bacg < 0:
                return -1
            var_dcmd.heappush(var_rgwu, -var_egyk)
            var_ayzf = var_wnki
        return var_osiz
