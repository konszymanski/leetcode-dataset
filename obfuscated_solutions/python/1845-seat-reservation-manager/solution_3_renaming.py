from sortedcontainers import SortedSet


class SeatManager:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.marker = 1
        arg_ihhe.available_seats = var_rcsn()

    def func_bacg(arg_ihhe):
        if arg_ihhe.available_seats:
            var_hqta = arg_ihhe.available_seats.pop(0)
            return var_hqta
        var_hqta = arg_ihhe.marker
        arg_ihhe.marker += 1
        return var_hqta

    def func_rgwu(arg_ihhe, var_hqta):
        arg_ihhe.available_seats.add(var_hqta)
