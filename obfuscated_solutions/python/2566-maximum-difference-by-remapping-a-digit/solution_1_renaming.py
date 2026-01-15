class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_bacg
        var_wrnh = 0
        while var_wrnh < var_osiz(var_bacg) and var_bacg[var_wrnh] == '9':
            var_wrnh += 1
        if var_wrnh < var_osiz(var_bacg):
            var_bacg = var_bacg.replace(var_bacg[var_wrnh], '9')
        var_rgwu = var_rgwu.replace(var_rgwu[0], '0')
        return var_rcsn(var_bacg) - var_rcsn(var_rgwu)
