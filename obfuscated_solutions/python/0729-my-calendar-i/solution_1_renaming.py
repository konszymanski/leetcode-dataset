class MyCalendar:

    def func_udax(arg_ihhe):
        arg_ihhe.calendar = []

    def func_xdvx(arg_ihhe, arg_rcsn, arg_bacg):
        for var_hqta, var_rgwu in arg_ihhe.calendar:
            if var_hqta < arg_bacg and arg_rcsn < var_rgwu:
                return False
        arg_ihhe.calendar.append((arg_rcsn, arg_bacg))
        return True
