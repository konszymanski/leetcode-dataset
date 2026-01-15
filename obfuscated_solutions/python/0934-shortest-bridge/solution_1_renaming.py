class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh, var_osiz = -1, -1
        for var_ayzf in var_wnki(var_hqta):
            for var_egyk in var_wnki(var_hqta):
                if arg_xdvx[var_ayzf][var_egyk] == 1:
                    var_wrnh, var_osiz = var_ayzf, var_egyk
                    break

        def func_dcmd(arg_llti, arg_zbxo):
            arg_xdvx[arg_llti][arg_zbxo] = 2
            var_rdmc.append((arg_llti, arg_zbxo))
            for var_rjut, var_lsgw in [(arg_llti + 1, arg_zbxo), (arg_llti -
                1, arg_zbxo), (arg_llti, arg_zbxo + 1), (arg_llti, arg_zbxo -
                1)]:
                if (0 <= var_rjut < var_hqta and 0 <= var_lsgw < var_hqta and
                    arg_xdvx[var_rjut][var_lsgw] == 1):
                    func_dcmd(var_rjut, var_lsgw)
        var_rdmc = []
        func_dcmd(var_wrnh, var_osiz)
        var_cbvh = 0
        while var_rdmc:
            var_yjch = []
            for arg_llti, arg_zbxo in var_rdmc:
                for var_rjut, var_lsgw in [(arg_llti + 1, arg_zbxo), (
                    arg_llti - 1, arg_zbxo), (arg_llti, arg_zbxo + 1), (
                    arg_llti, arg_zbxo - 1)]:
                    if 0 <= var_rjut < var_hqta and 0 <= var_lsgw < var_hqta:
                        if arg_xdvx[var_rjut][var_lsgw] == 1:
                            return var_cbvh
                        elif arg_xdvx[var_rjut][var_lsgw] == 0:
                            var_yjch.append((var_rjut, var_lsgw))
                            arg_xdvx[var_rjut][var_lsgw] = -1
            var_rdmc = var_yjch
            var_cbvh += 1
        return var_cbvh
