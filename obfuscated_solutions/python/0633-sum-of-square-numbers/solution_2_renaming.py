class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = 0
        while var_bacg * var_bacg <= arg_xdvx:
            var_hqta = arg_xdvx - var_bacg * var_bacg
            var_rgwu = 1
            var_wrnh = 0
            while var_wrnh < var_hqta:
                var_wrnh += var_rgwu
                var_rgwu += 2
            if var_wrnh == var_hqta:
                return True
            var_bacg += 1
        return False
