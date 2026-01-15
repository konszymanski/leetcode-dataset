class SeatManager:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.marker = 1
        arg_ihhe.available_seats = []

    def func_rcsn(arg_ihhe):
        if arg_ihhe.available_seats:
            var_bacg = var_hqta.heappop(arg_ihhe.available_seats)
            return var_bacg
        var_bacg = arg_ihhe.marker
        arg_ihhe.marker += 1
        return var_bacg

    def func_rgwu(arg_ihhe, var_bacg):
        var_hqta.heappush(arg_ihhe.available_seats, var_bacg)
