class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.array = arg_xdvx
        arg_ihhe.original = var_rcsn(arg_xdvx)

    def func_bacg(arg_ihhe):
        arg_ihhe.array = arg_ihhe.original
        arg_ihhe.original = var_rcsn(arg_ihhe.original)
        return arg_ihhe.array

    def func_hqta(arg_ihhe):
        for var_rgwu in var_wrnh(var_osiz(arg_ihhe.array)):
            var_ayzf = var_wnki.randrange(var_rgwu, var_osiz(arg_ihhe.array))
            arg_ihhe.array[var_rgwu], arg_ihhe.array[var_ayzf
                ] = arg_ihhe.array[var_ayzf], arg_ihhe.array[var_rgwu]
        return arg_ihhe.array
