class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        arg_xdvx.ans = 0
        var_bacg = {None}

        def func_hqta(arg_rgwu, arg_wrnh=None):
            if arg_rgwu:
                func_hqta(arg_rgwu.left, arg_rgwu)
                func_hqta(arg_rgwu.right, arg_rgwu)
                if (arg_wrnh is None and arg_rgwu not in var_bacg or 
                    arg_rgwu.left not in var_bacg or arg_rgwu.right not in
                    var_bacg):
                    arg_xdvx.ans += 1
                    var_bacg.update({arg_rgwu, arg_wrnh, arg_rgwu.left,
                        arg_rgwu.right})
        func_hqta(arg_rcsn)
        return arg_xdvx.ans
