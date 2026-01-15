class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        if arg_xdvx == 1:
            return arg_bacg
        var_rgwu = 2 ** (arg_xdvx - 1)
        if arg_rcsn > var_rgwu / 2:
            var_wrnh = 1 if arg_bacg == 0 else 0
            return arg_ihhe.depthFirstSearch(arg_xdvx - 1, arg_rcsn - 
                var_rgwu / 2, var_wrnh)
        else:
            var_wrnh = 0 if arg_bacg == 0 else 1
            return arg_ihhe.depthFirstSearch(arg_xdvx - 1, arg_rcsn, var_wrnh)

    def func_osiz(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta) ->var_hqta:
        return arg_ihhe.depthFirstSearch(arg_xdvx, arg_rcsn, 0)
