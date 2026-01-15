class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.index = 0

    def func_xdvx(arg_ihhe, arg_rcsn: var_bacg) ->var_hqta:
        return arg_ihhe.helper(arg_rcsn, 0)

    def func_rgwu(arg_ihhe, arg_rcsn, arg_wrnh):
        if arg_ihhe.index >= var_osiz(arg_rcsn):
            return None
        var_ayzf = 0
        while arg_ihhe.index + var_ayzf < var_osiz(arg_rcsn) and arg_rcsn[
            arg_ihhe.index + var_ayzf] == '-':
            var_ayzf += 1
        if var_ayzf != arg_wrnh:
            return None
        arg_ihhe.index += var_ayzf
        var_wnki = 0
        while arg_ihhe.index < var_osiz(arg_rcsn) and arg_rcsn[arg_ihhe.index
            ].isdigit():
            var_wnki = var_wnki * 10 + var_egyk(arg_rcsn[arg_ihhe.index])
            arg_ihhe.index += 1
        var_dcmd = var_hqta(var_wnki)
        var_dcmd.left = arg_ihhe.helper(arg_rcsn, arg_wrnh + 1)
        var_dcmd.right = arg_ihhe.helper(arg_rcsn, arg_wrnh + 1)
        return var_dcmd
