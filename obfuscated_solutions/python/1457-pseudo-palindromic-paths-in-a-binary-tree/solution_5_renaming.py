class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:

        def func_bacg(arg_hqta, arg_rgwu):
            nonlocal count
            if arg_hqta:
                arg_rgwu = arg_rgwu ^ 1 << arg_hqta.val
                if arg_hqta.left is None and arg_hqta.right is None:
                    if arg_rgwu & arg_rgwu - 1 == 0:
                        var_wrnh += 1
                else:
                    func_bacg(arg_hqta.left, arg_rgwu)
                    func_bacg(arg_hqta.right, arg_rgwu)
        var_wrnh = 0
        func_bacg(arg_xdvx, 0)
        return var_wrnh
