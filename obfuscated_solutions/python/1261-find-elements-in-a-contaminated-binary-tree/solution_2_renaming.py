class FindElements:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.seen = var_bacg()
        arg_ihhe.bfs(arg_xdvx)

    def func_hqta(arg_ihhe, arg_rgwu: var_wrnh) ->var_osiz:
        return arg_rgwu in arg_ihhe.seen

    def func_ayzf(arg_ihhe, arg_xdvx: var_rcsn) ->None:
        var_wnki = [arg_xdvx]
        arg_xdvx.val = 0
        while var_wnki:
            var_egyk = var_wnki.pop(0)
            arg_ihhe.seen.add(var_egyk.val)
            if var_egyk.left:
                var_egyk.left.val = var_egyk.val * 2 + 1
                var_wnki.append(var_egyk.left)
            if var_egyk.right:
                var_egyk.right.val = var_egyk.val * 2 + 2
                var_wnki.append(var_egyk.right)
