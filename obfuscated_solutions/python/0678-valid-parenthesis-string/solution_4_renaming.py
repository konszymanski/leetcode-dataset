class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx) - 1
        for var_osiz in var_ayzf(var_rgwu + 1):
            if arg_xdvx[var_osiz] == '(' or arg_xdvx[var_osiz] == '*':
                var_bacg += 1
            else:
                var_bacg -= 1
            if arg_xdvx[var_rgwu - var_osiz] == ')' or arg_xdvx[var_rgwu -
                var_osiz] == '*':
                var_hqta += 1
            else:
                var_hqta -= 1
            if var_bacg < 0 or var_hqta < 0:
                return False
        return True
