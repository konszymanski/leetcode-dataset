class CustomStack:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.stack = var_bacg()
        arg_ihhe.max_size = arg_xdvx

    def func_hqta(arg_ihhe, arg_rgwu: var_rcsn) ->None:
        if var_wrnh(arg_ihhe.stack) < arg_ihhe.max_size:
            arg_ihhe.stack.append(arg_rgwu)

    def func_osiz(arg_ihhe) ->var_rcsn:
        return arg_ihhe.stack.pop() if arg_ihhe.stack else -1

    def func_ayzf(arg_ihhe, arg_wnki: var_rcsn, arg_egyk: var_rcsn) ->None:
        for var_dcmd, var_llti in var_zbxo(var_rdmc(arg_wnki), arg_ihhe.stack):
            arg_ihhe.stack[var_dcmd] += arg_egyk
