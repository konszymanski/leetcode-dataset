class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_xdvx.pop()

    def func_rcsn(arg_ihhe, arg_xdvx):
        var_bacg = var_hqta(arg_xdvx) - 1
        while var_bacg >= 0 and arg_xdvx[var_bacg] != '0':
            arg_xdvx[var_bacg] = '0'
            var_bacg -= 1
        if var_bacg < 0:
            arg_xdvx.insert(0, '1')
        else:
            arg_xdvx[var_bacg] = '1'

    def func_rgwu(arg_ihhe, arg_xdvx: var_wrnh) ->var_egyk:
        arg_xdvx = var_osiz(arg_xdvx)
        var_ayzf = 0
        while var_hqta(arg_xdvx) > 1:
            var_wnki = var_hqta(arg_xdvx)
            if arg_xdvx[var_wnki - 1] == '0':
                arg_ihhe.divide_by_two(arg_xdvx)
            else:
                arg_ihhe.add_one(arg_xdvx)
            var_ayzf += 1
        return var_ayzf
