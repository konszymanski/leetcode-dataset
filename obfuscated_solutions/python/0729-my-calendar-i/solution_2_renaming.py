from sortedcontainers import SortedList


class MyCalendar:

    def func_udax(arg_ihhe):
        arg_ihhe.calendar = var_xdvx()

    def func_rcsn(arg_ihhe, arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_ayzf:
        var_wrnh = arg_ihhe.calendar.bisect_right((arg_bacg, arg_hqta))
        if var_wrnh > 0 and arg_ihhe.calendar[var_wrnh - 1][1
            ] > arg_bacg or var_wrnh < var_osiz(arg_ihhe.calendar
            ) and arg_ihhe.calendar[var_wrnh][0] < arg_hqta:
            return False
        arg_ihhe.calendar.add((arg_bacg, arg_hqta))
        return True
