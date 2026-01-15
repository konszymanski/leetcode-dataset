class Solution:

    def func_udax(arg_ihhe, arg_xdvx):

        def func_rcsn(arg_xdvx, arg_bacg, arg_hqta, arg_rgwu):
            if arg_bacg == var_wrnh(arg_xdvx):
                arg_rgwu.append(arg_hqta[:])
                return
            arg_hqta.append(arg_xdvx[arg_bacg])
            func_rcsn(arg_xdvx, arg_bacg + 1, arg_hqta, arg_rgwu)
            arg_hqta.pop()
            func_rcsn(arg_xdvx, arg_bacg + 1, arg_hqta, arg_rgwu)
        arg_rgwu = []
        func_rcsn(arg_xdvx, 0, [], arg_rgwu)
        var_osiz = 0
        for arg_hqta in arg_rgwu:
            var_ayzf = 0
            for var_wnki in arg_hqta:
                var_ayzf ^= var_wnki
            var_osiz += var_ayzf
        return var_osiz
