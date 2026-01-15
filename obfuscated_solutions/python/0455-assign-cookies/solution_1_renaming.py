class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        arg_xdvx.sort()
        arg_rcsn.sort()
        var_rgwu = 0
        var_wrnh = 0
        while var_wrnh < var_osiz(arg_rcsn) and var_rgwu < var_osiz(arg_xdvx):
            if arg_rcsn[var_wrnh] >= arg_xdvx[var_rgwu]:
                var_rgwu += 1
            var_wrnh += 1
        return var_rgwu
