class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_hqta:
        arg_ihhe.smallest_string = ''
        arg_ihhe.dfs(arg_xdvx, '')
        return arg_ihhe.smallest_string

    def func_rgwu(arg_ihhe, arg_xdvx, arg_wrnh):
        if not arg_xdvx:
            return
        arg_wrnh = var_osiz(arg_xdvx.val + var_ayzf('a')) + arg_wrnh
        if not arg_xdvx.left and not arg_xdvx.right:
            if (not arg_ihhe.smallest_string or arg_ihhe.smallest_string >
                arg_wrnh):
                arg_ihhe.smallest_string = arg_wrnh
        if arg_xdvx.left:
            arg_ihhe.dfs(arg_xdvx.left, arg_wrnh)
        if arg_xdvx.right:
            arg_ihhe.dfs(arg_xdvx.right, arg_wrnh)
