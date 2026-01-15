class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_zbxo:
        var_rgwu = []
        if arg_xdvx > 0:
            var_wrnh.heappush(var_rgwu, (-arg_xdvx, 'a'))
        if arg_rcsn > 0:
            var_wrnh.heappush(var_rgwu, (-arg_rcsn, 'b'))
        if arg_bacg > 0:
            var_wrnh.heappush(var_rgwu, (-arg_bacg, 'c'))
        var_osiz = []
        while var_rgwu:
            var_ayzf, var_wnki = var_wrnh.heappop(var_rgwu)
            var_ayzf = -var_ayzf
            if var_egyk(var_osiz) >= 2 and var_osiz[-1
                ] == var_wnki and var_osiz[-2] == var_wnki:
                if not var_rgwu:
                    break
                var_dcmd, var_llti = var_wrnh.heappop(var_rgwu)
                var_osiz.append(var_llti)
                if var_dcmd + 1 < 0:
                    var_wrnh.heappush(var_rgwu, (var_dcmd + 1, var_llti))
                var_wrnh.heappush(var_rgwu, (-var_ayzf, var_wnki))
            else:
                var_ayzf -= 1
                var_osiz.append(var_wnki)
                if var_ayzf > 0:
                    var_wrnh.heappush(var_rgwu, (-var_ayzf, var_wnki))
        return ''.join(var_osiz)
