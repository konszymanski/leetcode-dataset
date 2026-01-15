class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_rgwu:
        var_wrnh = [0] * 26
        for var_osiz in arg_xdvx:
            var_wrnh[var_ayzf(var_osiz) - var_ayzf('A')] += 1
        var_wnki = [(-var_egyk) for var_egyk in var_wrnh if var_egyk > 0]
        var_dcmd.heapify(var_wnki)
        var_llti = 0
        while var_wnki:
            var_zbxo = arg_rcsn + 1
            var_rdmc = []
            var_rjut = 0
            while var_zbxo > 0 and var_wnki:
                var_lsgw = -var_dcmd.heappop(var_wnki)
                if var_lsgw > 1:
                    var_rdmc.append(-(var_lsgw - 1))
                var_rjut += 1
                var_zbxo -= 1
            for var_cbvh in var_rdmc:
                var_dcmd.heappush(var_wnki, var_cbvh)
            var_llti += var_rjut if not var_wnki else arg_rcsn + 1
        return var_llti
