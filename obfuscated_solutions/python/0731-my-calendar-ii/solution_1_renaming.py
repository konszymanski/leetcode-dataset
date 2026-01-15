class MyCalendarTwo:

    def func_udax(arg_ihhe):
        arg_ihhe.bookings = []
        arg_ihhe.overlap_bookings = []

    def func_xdvx(arg_ihhe, arg_rcsn: var_hqta, arg_bacg: var_hqta) ->var_wrnh:
        for var_rgwu in arg_ihhe.overlap_bookings:
            if arg_ihhe.does_overlap(var_rgwu[0], var_rgwu[1], arg_rcsn,
                arg_bacg):
                return False
        for var_rgwu in arg_ihhe.bookings:
            if arg_ihhe.does_overlap(var_rgwu[0], var_rgwu[1], arg_rcsn,
                arg_bacg):
                arg_ihhe.overlap_bookings.append(arg_ihhe.get_overlapped(
                    var_rgwu[0], var_rgwu[1], arg_rcsn, arg_bacg))
        arg_ihhe.bookings.append((arg_rcsn, arg_bacg))
        return True

    def func_osiz(arg_ihhe, arg_ayzf: var_hqta, arg_wnki: var_hqta,
        arg_egyk: var_hqta, arg_dcmd: var_hqta) ->var_wrnh:
        return var_llti(arg_ayzf, arg_egyk) < var_zbxo(arg_wnki, arg_dcmd)

    def func_rdmc(arg_ihhe, arg_ayzf: var_hqta, arg_wnki: var_hqta,
        arg_egyk: var_hqta, arg_dcmd: var_hqta) ->var_rjut:
        return var_llti(arg_ayzf, arg_egyk), var_zbxo(arg_wnki, arg_dcmd)
