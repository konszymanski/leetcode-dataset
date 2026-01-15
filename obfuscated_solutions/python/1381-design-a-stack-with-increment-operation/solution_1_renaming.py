class CustomStack:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe._stack = []
        arg_ihhe._max_size = arg_xdvx

    def func_bacg(arg_ihhe, arg_hqta: var_rcsn) ->None:
        if var_rgwu(arg_ihhe._stack) < arg_ihhe._max_size:
            arg_ihhe._stack.append(arg_hqta)

    def func_wrnh(arg_ihhe) ->var_rcsn:
        return arg_ihhe._stack.pop() if arg_ihhe._stack else -1

    def func_osiz(arg_ihhe, arg_ayzf: var_rcsn, arg_wnki: var_rcsn) ->None:
        for var_egyk in var_dcmd(var_llti(arg_ayzf, var_rgwu(arg_ihhe._stack))
            ):
            arg_ihhe._stack[var_egyk] += arg_wnki
