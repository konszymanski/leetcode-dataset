class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.output = []
        arg_ihhe.n = var_rcsn(arg_xdvx)
        arg_ihhe.backtrack(0, [], arg_xdvx)
        return arg_ihhe.output

    def func_bacg(arg_ihhe, arg_hqta, arg_rgwu, arg_xdvx):
        arg_ihhe.output.append(arg_rgwu[:])
        for var_wrnh in var_osiz(arg_hqta, arg_ihhe.n):
            arg_rgwu.append(arg_xdvx[var_wrnh])
            arg_ihhe.backtrack(var_wrnh + 1, arg_rgwu, arg_xdvx)
            arg_rgwu.pop()
