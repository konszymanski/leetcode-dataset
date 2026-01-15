class NumberContainers:

    def func_udax(arg_ihhe):
        arg_ihhe.number_to_indices = var_xdvx(var_rcsn)
        arg_ihhe.index_to_numbers = {}

    def func_bacg(arg_ihhe, arg_hqta: var_wrnh, arg_rgwu: var_wrnh) ->None:
        arg_ihhe.index_to_numbers[arg_hqta] = arg_rgwu
        var_osiz.heappush(arg_ihhe.number_to_indices[arg_rgwu], arg_hqta)

    def func_ayzf(arg_ihhe, arg_rgwu: var_wrnh) ->var_wrnh:
        if not arg_ihhe.number_to_indices[arg_rgwu]:
            return -1
        while arg_ihhe.number_to_indices[arg_rgwu]:
            arg_hqta = arg_ihhe.number_to_indices[arg_rgwu][0]
            if arg_ihhe.index_to_numbers.get(arg_hqta) == arg_rgwu:
                return arg_hqta
            var_osiz.heappop(arg_ihhe.number_to_indices[arg_rgwu])
        return -1
