class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):

        def func_bacg(arg_hqta):
            if arg_hqta:
                if not arg_hqta.left and not arg_hqta.right:
                    yield arg_hqta.val
                yield from func_bacg(arg_hqta.left)
                yield from func_bacg(arg_hqta.right)
        return var_rgwu(func_bacg(arg_xdvx)) == var_rgwu(func_bacg(arg_rcsn))
