class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_rcsn
        [var_bacg]]:
        var_hqta = []

        def func_rgwu(arg_wrnh, arg_osiz):
            if var_ayzf(arg_wrnh) == var_ayzf(arg_xdvx):
                var_hqta.append(var_wnki(arg_wrnh))
                return
            for var_egyk in arg_osiz:
                if arg_osiz[var_egyk] > 0:
                    arg_wrnh.append(var_egyk)
                    arg_osiz[var_egyk] -= 1
                    func_rgwu(arg_wrnh, arg_osiz)
                    arg_wrnh.pop()
                    arg_osiz[var_egyk] += 1
        func_rgwu([], var_dcmd(arg_xdvx))
        return var_hqta
