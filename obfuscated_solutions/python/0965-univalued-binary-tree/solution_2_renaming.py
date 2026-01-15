class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = (not arg_rcsn.left or arg_rcsn.val == arg_rcsn.left.val and
            arg_xdvx.isUnivalTree(arg_rcsn.left))
        var_hqta = (not arg_rcsn.right or arg_rcsn.val == arg_rcsn.right.
            val and arg_xdvx.isUnivalTree(arg_rcsn.right))
        return var_bacg and var_hqta
