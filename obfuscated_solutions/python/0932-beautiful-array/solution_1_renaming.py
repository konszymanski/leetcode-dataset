class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = {(1): [1]}

        def func_bacg(arg_xdvx):
            if arg_xdvx not in var_rcsn:
                var_hqta = func_bacg((arg_xdvx + 1) / 2)
                var_rgwu = func_bacg(arg_xdvx / 2)
                var_rcsn[arg_xdvx] = [(2 * var_wrnh - 1) for var_wrnh in
                    var_hqta] + [(2 * var_wrnh) for var_wrnh in var_rgwu]
            return var_rcsn[arg_xdvx]
        return func_bacg(arg_xdvx)
