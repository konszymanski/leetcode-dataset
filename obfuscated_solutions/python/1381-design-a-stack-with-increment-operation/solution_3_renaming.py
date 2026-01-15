class CustomStack:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe._stack = [0] * arg_xdvx
        arg_ihhe._inc = [0] * arg_xdvx
        arg_ihhe._top = -1

    def func_bacg(arg_ihhe, arg_hqta: var_rcsn) ->None:
        if arg_ihhe._top < var_rgwu(arg_ihhe._stack) - 1:
            arg_ihhe._top += 1
            arg_ihhe._stack[arg_ihhe._top] = arg_hqta

    def func_wrnh(arg_ihhe) ->var_rcsn:
        if arg_ihhe._top < 0:
            return -1
        var_osiz = arg_ihhe._stack[arg_ihhe._top] + arg_ihhe._inc[arg_ihhe._top
            ]
        if arg_ihhe._top > 0:
            arg_ihhe._inc[arg_ihhe._top - 1] += arg_ihhe._inc[arg_ihhe._top]
        arg_ihhe._inc[arg_ihhe._top] = 0
        arg_ihhe._top -= 1
        return var_osiz

    def func_ayzf(arg_ihhe, arg_wnki: var_rcsn, arg_egyk: var_rcsn) ->None:
        if arg_ihhe._top >= 0:
            var_dcmd = var_llti(arg_ihhe._top, arg_wnki - 1)
            arg_ihhe._inc[var_dcmd] += arg_egyk
