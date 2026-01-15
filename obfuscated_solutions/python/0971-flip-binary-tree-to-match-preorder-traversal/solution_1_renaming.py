class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        arg_xdvx.flipped = []
        arg_xdvx.i = 0

        def func_hqta(arg_rgwu):
            if arg_rgwu:
                if arg_rgwu.val != arg_bacg[arg_xdvx.i]:
                    arg_xdvx.flipped = [-1]
                    return
                arg_xdvx.i += 1
                if arg_xdvx.i < var_wrnh(arg_bacg
                    ) and arg_rgwu.left and arg_rgwu.left.val != arg_bacg[
                    arg_xdvx.i]:
                    arg_xdvx.flipped.append(arg_rgwu.val)
                    func_hqta(arg_rgwu.right)
                    func_hqta(arg_rgwu.left)
                else:
                    func_hqta(arg_rgwu.left)
                    func_hqta(arg_rgwu.right)
        func_hqta(arg_rcsn)
        if arg_xdvx.flipped and arg_xdvx.flipped[0] == -1:
            arg_xdvx.flipped = [-1]
        return arg_xdvx.flipped
