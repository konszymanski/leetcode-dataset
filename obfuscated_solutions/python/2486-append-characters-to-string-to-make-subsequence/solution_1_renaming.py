class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_osiz:
        var_hqta = 0
        var_rgwu = 0
        while var_hqta < var_wrnh(arg_xdvx) and var_rgwu < var_wrnh(arg_rcsn):
            if arg_xdvx[var_hqta] == arg_rcsn[var_rgwu]:
                var_rgwu += 1
            var_hqta += 1
        return var_wrnh(arg_rcsn) - var_rgwu
