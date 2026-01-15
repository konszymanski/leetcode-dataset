class NumberContainers:

    def func_udax(arg_ihhe):
        arg_ihhe.number_to_indices = var_xdvx.defaultdict(var_rcsn)
        arg_ihhe.index_to_number = {}

    def func_bacg(arg_ihhe, arg_hqta: var_wrnh, arg_rgwu: var_wrnh) ->None:
        if arg_hqta in arg_ihhe.index_to_number:
            var_osiz = arg_ihhe.index_to_number[arg_hqta]
            arg_ihhe.number_to_indices[var_osiz].remove(arg_hqta)
            if not arg_ihhe.number_to_indices[var_osiz]:
                del arg_ihhe.number_to_indices[var_osiz]
        arg_ihhe.index_to_number[arg_hqta] = arg_rgwu
        arg_ihhe.number_to_indices[arg_rgwu].add(arg_hqta)

    def func_ayzf(arg_ihhe, arg_rgwu: var_wrnh) ->var_wrnh:
        if (arg_rgwu in arg_ihhe.number_to_indices and arg_ihhe.
            number_to_indices[arg_rgwu]):
            return arg_ihhe.number_to_indices[arg_rgwu][0]
        return -1
