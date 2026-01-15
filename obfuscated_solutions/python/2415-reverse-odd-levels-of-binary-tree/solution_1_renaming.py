class Solution:

    def func_udax(arg_ihhe, arg_xdvx) ->var_rcsn:
        arg_ihhe.__traverse_DFS(arg_xdvx.left, arg_xdvx.right, 0)
        return arg_xdvx

    def func_bacg(arg_ihhe, arg_hqta, arg_rgwu, arg_wrnh):
        if arg_hqta is None or arg_rgwu is None:
            return
        if arg_wrnh % 2 == 0:
            var_osiz = arg_hqta.val
            arg_hqta.val = arg_rgwu.val
            arg_rgwu.val = var_osiz
        arg_ihhe.__traverse_DFS(arg_hqta.left, arg_rgwu.right, arg_wrnh + 1)
        arg_ihhe.__traverse_DFS(arg_hqta.right, arg_rgwu.left, arg_wrnh + 1)
