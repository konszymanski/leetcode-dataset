class MapSum(var_udax):

    def func_ihhe(arg_xdvx):
        arg_xdvx.map = {}
        arg_xdvx.score = var_rcsn.Counter()

    def func_bacg(arg_xdvx, arg_hqta, arg_rgwu):
        var_wrnh = arg_rgwu - arg_xdvx.map.get(arg_hqta, 0)
        arg_xdvx.map[arg_hqta] = arg_rgwu
        for var_osiz in var_ayzf(var_wnki(arg_hqta) + 1):
            var_egyk = arg_hqta[:var_osiz]
            arg_xdvx.score[var_egyk] += var_wrnh

    def func_dcmd(arg_xdvx, var_egyk):
        return arg_xdvx.score[var_egyk]
