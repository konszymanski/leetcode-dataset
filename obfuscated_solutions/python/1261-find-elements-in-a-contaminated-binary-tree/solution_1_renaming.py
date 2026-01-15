class FindElements:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.seen = var_bacg()
        arg_ihhe.dfs(arg_xdvx, 0)

    def func_hqta(arg_ihhe, arg_rgwu: var_wrnh) ->var_osiz:
        return arg_rgwu in arg_ihhe.seen

    def func_ayzf(arg_ihhe, arg_wnki, arg_egyk):
        if arg_wnki is None:
            return
        arg_ihhe.seen.add(arg_egyk)
        arg_ihhe.dfs(arg_wnki.left, arg_egyk * 2 + 1)
        arg_ihhe.dfs(arg_wnki.right, arg_egyk * 2 + 2)
