class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_bacg[var_hqta]:
        if arg_xdvx is None:
            return None
        arg_xdvx.left = arg_ihhe.removeLeafNodes(arg_xdvx.left, arg_rcsn)
        arg_xdvx.right = arg_ihhe.removeLeafNodes(arg_xdvx.right, arg_rcsn)
        if (arg_xdvx.left is None and arg_xdvx.right is None and arg_xdvx.
            val == arg_rcsn):
            return None
        return arg_xdvx
