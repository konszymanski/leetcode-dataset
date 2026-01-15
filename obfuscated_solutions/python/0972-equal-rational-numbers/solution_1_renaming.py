from fractions import Fraction


class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):

        def func_hqta(arg_rcsn):
            if '.' not in arg_rcsn:
                return var_rgwu(var_wrnh(arg_rcsn), 1)
            var_osiz = arg_rcsn.index('.')
            var_ayzf = var_rgwu(var_wrnh(arg_rcsn[:var_osiz]), 1)
            arg_rcsn = arg_rcsn[var_osiz + 1:]
            if '(' not in arg_rcsn:
                if arg_rcsn:
                    var_ayzf += var_rgwu(var_wrnh(arg_rcsn), 10 ** var_wnki
                        (arg_rcsn))
                return var_ayzf
            var_osiz = arg_rcsn.index('(')
            if var_osiz:
                var_ayzf += var_rgwu(var_wrnh(arg_rcsn[:var_osiz]), 10 **
                    var_osiz)
            arg_rcsn = arg_rcsn[var_osiz + 1:-1]
            var_egyk = var_wnki(arg_rcsn)
            var_ayzf += var_rgwu(var_wrnh(arg_rcsn), 10 ** var_osiz * (10 **
                var_egyk - 1))
            return var_ayzf
        return func_hqta(arg_rcsn) == func_hqta(arg_bacg)
