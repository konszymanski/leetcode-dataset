class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta()
        var_rgwu = var_hqta()
        for var_wrnh in arg_xdvx:
            if var_wrnh in var_rgwu:
                continue
            if var_wrnh in var_bacg:
                var_bacg.remove(var_wrnh)
                var_rgwu.add(var_wrnh)
            else:
                var_bacg.add(var_wrnh)
        for var_wrnh in arg_xdvx:
            if var_wrnh not in var_rgwu:
                arg_rcsn -= 1
            if arg_rcsn == 0:
                return var_wrnh
        return ''
