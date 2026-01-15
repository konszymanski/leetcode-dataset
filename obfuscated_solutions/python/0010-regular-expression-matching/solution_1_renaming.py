def func_udax(arg_ihhe, arg_xdvx):
    if not arg_xdvx:
        return not arg_ihhe
    var_rcsn = var_bacg(arg_ihhe) and arg_xdvx[0] in {arg_ihhe[0], '.'}
    return var_rcsn and func_udax(arg_ihhe[1:], arg_xdvx[1:])
