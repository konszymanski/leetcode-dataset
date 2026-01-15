class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = []
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            var_egyk.heappush(var_bacg, (-arg_xdvx[var_osiz], var_osiz))
            var_egyk.heappush(var_hqta, (arg_xdvx[var_osiz], var_osiz))
            while -var_bacg[0][0] - var_hqta[0][0] > arg_rcsn:
                var_rgwu = var_dcmd(var_bacg[0][1], var_hqta[0][1]) + 1
                while var_bacg[0][1] < var_rgwu:
                    var_egyk.heappop(var_bacg)
                while var_hqta[0][1] < var_rgwu:
                    var_egyk.heappop(var_hqta)
            var_wrnh = var_llti(var_wrnh, var_osiz - var_rgwu + 1)
        return var_wrnh
