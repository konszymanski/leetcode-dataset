class RangeModule(var_udax):

    def func_ihhe(arg_xdvx):
        arg_xdvx.ranges = []

    def func_rcsn(arg_xdvx, arg_bacg, arg_hqta):
        var_rgwu, var_wrnh = 0, var_osiz(arg_xdvx.ranges) - 1
        for var_ayzf in (100, 10, 1):
            while var_rgwu + var_ayzf - 1 < var_osiz(arg_xdvx.ranges
                ) and arg_xdvx.ranges[var_rgwu + var_ayzf - 1][1] < arg_bacg:
                var_rgwu += var_ayzf
            while var_wrnh >= var_ayzf - 1 and arg_xdvx.ranges[var_wrnh -
                var_ayzf + 1][0] > arg_hqta:
                var_wrnh -= var_ayzf
        return var_rgwu, var_wrnh

    def func_wnki(arg_xdvx, arg_bacg, arg_hqta):
        var_rgwu, var_wrnh = arg_xdvx._bounds(arg_bacg, arg_hqta)
        if var_rgwu <= var_wrnh:
            arg_bacg = var_egyk(arg_bacg, arg_xdvx.ranges[var_rgwu][0])
            arg_hqta = var_dcmd(arg_hqta, arg_xdvx.ranges[var_wrnh][1])
        arg_xdvx.ranges[var_rgwu:var_wrnh + 1] = [(arg_bacg, arg_hqta)]

    def func_llti(arg_xdvx, arg_bacg, arg_hqta):
        var_rgwu = var_zbxo.bisect_left(arg_xdvx.ranges, (arg_bacg,
            var_rdmc('inf')))
        if var_rgwu:
            var_rgwu -= 1
        return var_rjut(arg_xdvx.ranges) and arg_xdvx.ranges[var_rgwu][0
            ] <= arg_bacg and arg_hqta <= arg_xdvx.ranges[var_rgwu][1]

    def func_lsgw(arg_xdvx, arg_bacg, arg_hqta):
        var_rgwu, var_wrnh = arg_xdvx._bounds(arg_bacg, arg_hqta)
        var_cbvh = []
        for var_yjch in var_dmio(var_rgwu, var_wrnh + 1):
            if arg_xdvx.ranges[var_yjch][0] < arg_bacg:
                var_cbvh.append((arg_xdvx.ranges[var_yjch][0], arg_bacg))
            if arg_hqta < arg_xdvx.ranges[var_yjch][1]:
                var_cbvh.append((arg_hqta, arg_xdvx.ranges[var_yjch][1]))
        arg_xdvx.ranges[var_rgwu:var_wrnh + 1] = var_cbvh
