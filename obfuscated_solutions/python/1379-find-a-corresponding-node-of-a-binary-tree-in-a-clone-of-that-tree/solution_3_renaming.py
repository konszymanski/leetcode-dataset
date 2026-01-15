class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:

        def func_rgwu(arg_wrnh: var_hqta, arg_osiz: var_hqta):
            if arg_wrnh:
                func_rgwu(arg_wrnh.left, arg_osiz.left)
                if arg_wrnh is arg_bacg:
                    arg_ihhe.ans = arg_osiz
                func_rgwu(arg_wrnh.right, arg_osiz.right)
        func_rgwu(arg_xdvx, arg_rcsn)
        return arg_ihhe.ans
