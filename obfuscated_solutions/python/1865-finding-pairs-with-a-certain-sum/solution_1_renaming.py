class FindSumPairs:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]):
        arg_ihhe.nums1 = arg_xdvx
        arg_ihhe.nums2 = arg_rcsn
        arg_ihhe.cnt = var_rgwu(arg_rcsn)

    def func_wrnh(arg_ihhe, arg_osiz: var_hqta, arg_ayzf: var_hqta) ->None:
        var_wnki, var_egyk = arg_ihhe.nums2, arg_ihhe.cnt
        var_egyk[var_wnki[arg_osiz]] -= 1
        var_wnki[arg_osiz] += arg_ayzf
        var_egyk[var_wnki[arg_osiz]] += 1

    def func_dcmd(arg_ihhe, arg_llti: var_hqta) ->var_hqta:
        var_zbxo, var_egyk = arg_ihhe.nums1, arg_ihhe.cnt
        var_rdmc = 0
        for var_rjut in var_zbxo:
            if (var_lsgw := arg_llti - var_rjut) in var_egyk:
                var_rdmc += var_egyk[var_lsgw]
        return var_rdmc
