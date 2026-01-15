class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = arg_xdvx ^ arg_rcsn
        var_rgwu = 0
        while var_hqta:
            var_hqta &= var_hqta - 1
            var_rgwu += 1
        return var_rgwu
