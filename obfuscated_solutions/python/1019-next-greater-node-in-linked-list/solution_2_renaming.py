class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf[var_wnki]:
        var_bacg, var_hqta = [], []
        var_rgwu = 0
        while arg_xdvx:
            var_bacg.append(0)
            while var_hqta and arg_xdvx.val > var_hqta[-1][1]:
                var_wrnh, var_osiz = var_hqta.pop()
                var_bacg[var_wrnh] = arg_xdvx.val
            var_hqta.append([var_rgwu, arg_xdvx.val])
            var_rgwu += 1
            arg_xdvx = arg_xdvx.next
        return var_bacg
