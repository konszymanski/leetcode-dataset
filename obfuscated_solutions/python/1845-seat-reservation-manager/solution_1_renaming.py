class SeatManager:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.available_seats = [var_rcsn for var_rcsn in var_bacg(1, 
            arg_xdvx + 1)]

    def func_hqta(arg_ihhe):
        var_rgwu = var_wrnh.heappop(arg_ihhe.available_seats)
        return var_rgwu

    def func_osiz(arg_ihhe, var_rgwu):
        var_wrnh.heappush(arg_ihhe.available_seats, var_rgwu)
