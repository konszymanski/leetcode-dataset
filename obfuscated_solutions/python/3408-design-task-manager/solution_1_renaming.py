class TaskManager:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]):
        arg_ihhe.taskInfo = {}
        arg_ihhe.heap = []
        for var_hqta, var_rgwu, var_wrnh in arg_xdvx:
            arg_ihhe.taskInfo[var_rgwu] = [var_wrnh, var_hqta]
            var_osiz(arg_ihhe.heap, [-var_wrnh, -var_rgwu])

    def func_ayzf(arg_ihhe, var_hqta: var_bacg, var_rgwu: var_bacg,
        var_wrnh: var_bacg) ->None:
        arg_ihhe.taskInfo[var_rgwu] = [var_wrnh, var_hqta]
        var_osiz(arg_ihhe.heap, [-var_wrnh, -var_rgwu])

    def func_wnki(arg_ihhe, var_rgwu: var_bacg, arg_egyk: var_bacg) ->None:
        arg_ihhe.taskInfo[var_rgwu][0] = arg_egyk
        var_osiz(arg_ihhe.heap, [-arg_egyk, -var_rgwu])

    def func_dcmd(arg_ihhe, var_rgwu: var_bacg) ->None:
        arg_ihhe.taskInfo.pop(var_rgwu)

    def func_llti(arg_ihhe) ->var_bacg:
        while arg_ihhe.heap:
            var_wrnh, var_rgwu = var_zbxo(arg_ihhe.heap)
            var_wrnh, var_rgwu = -var_wrnh, -var_rgwu
            if var_wrnh == arg_ihhe.taskInfo.get(var_rgwu, [-1, -1])[0]:
                return arg_ihhe.taskInfo.pop(var_rgwu)[1]
        return -1
