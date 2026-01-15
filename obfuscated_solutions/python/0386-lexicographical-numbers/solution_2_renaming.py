class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz[var_rcsn]:
        var_bacg = []
        var_hqta = 1
        for var_rgwu in var_wrnh(arg_xdvx):
            var_bacg.append(var_hqta)
            if var_hqta * 10 <= arg_xdvx:
                var_hqta *= 10
            else:
                while var_hqta % 10 == 9 or var_hqta >= arg_xdvx:
                    var_hqta //= 10
                var_hqta += 1
        return var_bacg
