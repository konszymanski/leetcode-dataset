class Solution:

    def func_udax(arg_ihhe, arg_xdvx: 'Node') ->var_bacg[var_hqta]:
        var_rcsn = []
        if not arg_xdvx:
            return var_rcsn
        arg_ihhe._traverse_postorder(arg_xdvx, var_rcsn)
        return var_rcsn

    def func_rgwu(arg_ihhe, arg_wrnh: 'Node', arg_osiz: var_bacg[var_hqta]
        ) ->None:
        if not arg_wrnh:
            return
        for var_ayzf in arg_wrnh.children:
            arg_ihhe._traverse_postorder(var_ayzf, arg_osiz)
        arg_osiz.append(arg_wrnh.val)
