class Solution:
    var_udax = 10 ** 9 + 7

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = [0] * var_hqta
        for var_osiz in var_ayzf(var_hqta):
            var_wnki = arg_rcsn[var_osiz]
            for var_egyk in var_ayzf(2, var_dcmd(var_llti.sqrt(var_wnki)) + 1):
                if var_wnki % var_egyk == 0:
                    var_wrnh[var_osiz] += 1
                    while var_wnki % var_egyk == 0:
                        var_wnki //= var_egyk
            if var_wnki >= 2:
                var_wrnh[var_osiz] += 1
        var_zbxo = [var_hqta] * var_hqta
        var_rdmc = [-1] * var_hqta
        var_rjut = []
        for var_osiz in var_ayzf(var_hqta):
            while var_rjut and var_wrnh[var_rjut[-1]] < var_wrnh[var_osiz]:
                var_lsgw = var_rjut.pop()
                var_zbxo[var_lsgw] = var_osiz
            if var_rjut:
                var_rdmc[var_osiz] = var_rjut[-1]
            var_rjut.append(var_osiz)
        var_cbvh = [0] * var_hqta
        for var_osiz in var_ayzf(var_hqta):
            var_cbvh[var_osiz] = (var_zbxo[var_osiz] - var_osiz) * (var_osiz -
                var_rdmc[var_osiz])
        var_yjch = []
        for var_osiz in var_ayzf(var_hqta):
            var_dmio.heappush(var_yjch, (-arg_rcsn[var_osiz], var_osiz))
        var_ulfl = 1

        def func_lgvi(arg_wvuc, arg_tufr):
            var_xhfo = 1
            while arg_tufr > 0:
                if arg_tufr % 2 == 1:
                    var_xhfo = var_xhfo * arg_wvuc % arg_xdvx.MOD
                arg_wvuc = arg_wvuc * arg_wvuc % arg_xdvx.MOD
                arg_tufr //= 2
            return var_xhfo
        while arg_bacg > 0:
            var_wnki, var_osiz = var_dmio.heappop(var_yjch)
            var_wnki = -var_wnki
            var_miuw = var_rhvk(arg_bacg, var_cbvh[var_osiz])
            var_ulfl = var_ulfl * func_lgvi(var_wnki, var_miuw) % arg_xdvx.MOD
            arg_bacg -= var_miuw
        return var_ulfl
