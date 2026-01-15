class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):

        def func_hqta(arg_rcsn):
            var_rgwu = 0
            for var_wrnh in var_osiz(arg_rcsn):
                if var_wrnh == '#':
                    var_rgwu += 1
                elif var_rgwu:
                    var_rgwu -= 1
                else:
                    yield var_wrnh
        return var_ayzf(var_wrnh == var_wnki for var_wrnh, var_wnki in
            var_egyk.izip_longest(func_hqta(arg_rcsn), func_hqta(arg_bacg)))
