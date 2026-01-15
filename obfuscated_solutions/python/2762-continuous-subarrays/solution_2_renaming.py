class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = []
        var_rgwu = []
        var_wrnh = var_osiz = 0
        var_ayzf = 0
        while var_osiz < var_wnki(arg_xdvx):
            var_egyk.heappush(var_hqta, (arg_xdvx[var_osiz], var_osiz))
            var_egyk.heappush(var_rgwu, (-arg_xdvx[var_osiz], var_osiz))
            while var_wrnh < var_osiz and -var_rgwu[0][0] - var_hqta[0][0] > 2:
                var_wrnh += 1
                while var_hqta and var_hqta[0][1] < var_wrnh:
                    var_egyk.heappop(var_hqta)
                while var_rgwu and var_rgwu[0][1] < var_wrnh:
                    var_egyk.heappop(var_rgwu)
            var_ayzf += var_osiz - var_wrnh + 1
            var_osiz += 1
        return var_ayzf
