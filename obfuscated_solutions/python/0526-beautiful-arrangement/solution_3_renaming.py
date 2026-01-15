class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.count = 0

    def func_xdvx(arg_ihhe, arg_rcsn):
        var_bacg = [False] * (arg_rcsn + 1)
        arg_ihhe.calculate(arg_rcsn, 1, var_bacg)
        return arg_ihhe.count

    def func_hqta(arg_ihhe, arg_rcsn, arg_rgwu, var_bacg):
        if arg_rgwu > arg_rcsn:
            arg_ihhe.count += 1
            return
        for var_wrnh in var_osiz(1, arg_rcsn + 1):
            if not var_bacg[var_wrnh] and (arg_rgwu % var_wrnh == 0 or 
                var_wrnh % arg_rgwu == 0):
                var_bacg[var_wrnh] = True
                arg_ihhe.calculate(arg_rcsn, arg_rgwu + 1, var_bacg)
                var_bacg[var_wrnh] = False
