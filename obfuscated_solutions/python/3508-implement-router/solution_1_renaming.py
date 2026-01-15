class Router:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.memLimit = arg_xdvx
        arg_ihhe.length = 0
        arg_ihhe.isExist = var_rcsn()
        arg_ihhe.sameDestQue = {}
        arg_ihhe.que = []

    def func_bacg(arg_ihhe, arg_hqta, arg_rgwu, arg_wrnh):
        var_osiz = arg_hqta, arg_rgwu, arg_wrnh
        if var_osiz in arg_ihhe.isExist:
            return False
        if arg_ihhe.length == arg_ihhe.memLimit:
            arg_ihhe.forwardPacket()
        arg_ihhe.length += 1
        arg_ihhe.que.append(var_osiz)
        if arg_rgwu not in arg_ihhe.sameDestQue:
            arg_ihhe.sameDestQue[arg_rgwu] = var_ayzf()
        arg_ihhe.sameDestQue[arg_rgwu].add(arg_wrnh)
        arg_ihhe.isExist.add(var_osiz)
        return True

    def func_wnki(arg_ihhe):
        var_egyk = []
        if arg_ihhe.que:
            var_osiz = arg_ihhe.que.pop(0)
            var_egyk = var_dcmd(var_osiz)
            arg_ihhe.isExist.remove(var_osiz)
            arg_ihhe.sameDestQue[var_egyk[1]].remove(var_egyk[2])
            arg_ihhe.length -= 1
        return var_egyk

    def func_llti(arg_ihhe, arg_rgwu, arg_zbxo, arg_rdmc):
        if arg_rgwu not in arg_ihhe.sameDestQue:
            return 0
        var_rjut = arg_ihhe.sameDestQue[arg_rgwu]
        var_lsgw = var_rjut.bisect_left(arg_zbxo)
        var_cbvh = var_rjut.bisect_right(arg_rdmc)
        return var_cbvh - var_lsgw
