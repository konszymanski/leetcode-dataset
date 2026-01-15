class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.array = arg_xdvx
        arg_ihhe.original = var_rcsn(arg_xdvx)

    def func_bacg(arg_ihhe):
        arg_ihhe.array = arg_ihhe.original
        arg_ihhe.original = var_rcsn(arg_ihhe.original)
        return arg_ihhe.array

    def func_hqta(arg_ihhe):
        var_rgwu = var_rcsn(arg_ihhe.array)
        for var_wrnh in var_osiz(var_ayzf(arg_ihhe.array)):
            var_wnki = var_egyk.randrange(var_ayzf(var_rgwu))
            arg_ihhe.array[var_wrnh] = var_rgwu.pop(var_wnki)
        return arg_ihhe.array
