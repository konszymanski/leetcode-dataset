class ParkingSystem:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta):
        arg_ihhe.empty = [arg_xdvx, arg_rcsn, arg_bacg]

    def func_rgwu(arg_ihhe, arg_wrnh: var_hqta) ->var_osiz:
        if arg_ihhe.empty[arg_wrnh - 1] > 0:
            arg_ihhe.empty[arg_wrnh - 1] -= 1
            return True
        return False
