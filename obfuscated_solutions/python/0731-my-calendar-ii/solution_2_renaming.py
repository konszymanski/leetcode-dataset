from sortedcontainers import SortedDict


class MyCalendarTwo:

    def func_udax(arg_ihhe):
        arg_ihhe.booking_count = var_xdvx()
        arg_ihhe.max_overlapped_booking = 2

    def func_rcsn(arg_ihhe, arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_ayzf:
        arg_ihhe.booking_count[arg_bacg] = arg_ihhe.booking_count.get(arg_bacg,
            0) + 1
        arg_ihhe.booking_count[arg_hqta] = arg_ihhe.booking_count.get(arg_hqta,
            0) - 1
        var_wrnh = 0
        for var_osiz in arg_ihhe.booking_count.values():
            var_wrnh += var_osiz
            if var_wrnh > arg_ihhe.max_overlapped_booking:
                arg_ihhe.booking_count[arg_bacg] -= 1
                arg_ihhe.booking_count[arg_hqta] += 1
                if arg_ihhe.booking_count[arg_bacg] == 0:
                    del arg_ihhe.booking_count[arg_bacg]
                return False
        return True
