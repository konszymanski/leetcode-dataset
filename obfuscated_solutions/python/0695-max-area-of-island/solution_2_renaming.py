class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta()
        var_rgwu = 0
        for var_wrnh, var_osiz in var_ayzf(arg_rcsn):
            for var_wnki, var_egyk in var_ayzf(var_osiz):
                if var_egyk and (var_wrnh, var_wnki) not in var_bacg:
                    var_dcmd = 0
                    var_llti = [(var_wrnh, var_wnki)]
                    var_bacg.add((var_wrnh, var_wnki))
                    while var_llti:
                        var_zbxo, var_rdmc = var_llti.pop()
                        var_dcmd += 1
                        for var_rjut, var_lsgw in ((var_zbxo - 1, var_rdmc),
                            (var_zbxo + 1, var_rdmc), (var_zbxo, var_rdmc -
                            1), (var_zbxo, var_rdmc + 1)):
                            if 0 <= var_rjut < var_cbvh(arg_rcsn
                                ) and 0 <= var_lsgw < var_cbvh(arg_rcsn[0]
                                ) and arg_rcsn[var_rjut][var_lsgw] and (
                                var_rjut, var_lsgw) not in var_bacg:
                                var_llti.append((var_rjut, var_lsgw))
                                var_bacg.add((var_rjut, var_lsgw))
                    var_rgwu = var_yjch(var_rgwu, var_dcmd)
        return var_rgwu
