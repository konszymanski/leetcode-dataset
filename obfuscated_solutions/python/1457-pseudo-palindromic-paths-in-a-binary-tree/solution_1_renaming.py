def func_udax(arg_ihhe):
    var_xdvx = 0
    for var_rcsn in var_bacg(1, 10):
        if arg_ihhe.count(var_rcsn) % 2 == 1:
            var_xdvx += 1
            if var_xdvx > 1:
                return False
    return True
