class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = [0] * var_bacg
        var_wrnh = 0
        for var_osiz in var_ayzf(var_bacg):
            if arg_rcsn[var_osiz] == 'R':
                var_wrnh = var_bacg
            elif arg_rcsn[var_osiz] == 'L':
                var_wrnh = 0
            else:
                var_wrnh = var_wnki(var_wrnh - 1, 0)
            var_rgwu[var_osiz] += var_wrnh
        var_wrnh = 0
        for var_osiz in var_ayzf(var_bacg - 1, -1, -1):
            if arg_rcsn[var_osiz] == 'L':
                var_wrnh = var_bacg
            elif arg_rcsn[var_osiz] == 'R':
                var_wrnh = 0
            else:
                var_wrnh = var_wnki(var_wrnh - 1, 0)
            var_rgwu[var_osiz] -= var_wrnh
        return ''.join('.' if var_wrnh == 0 else 'R' if var_wrnh > 0 else
            'L' for var_wrnh in var_rgwu)
