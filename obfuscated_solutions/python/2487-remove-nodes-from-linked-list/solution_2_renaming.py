class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        if arg_xdvx is None or arg_xdvx.next is None:
            return arg_xdvx
        var_hqta = arg_ihhe.removeNodes(arg_xdvx.next)
        if arg_xdvx.val < var_hqta.val:
            return var_hqta
        arg_xdvx.next = var_hqta
        return arg_xdvx
