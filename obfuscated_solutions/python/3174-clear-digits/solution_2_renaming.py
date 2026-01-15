class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = []
        for var_hqta in arg_xdvx:
            if var_hqta.isdigit():
                var_bacg.pop()
            else:
                var_bacg.append(var_hqta)
        return ''.join(var_bacg)
