class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_xdvx = arg_xdvx.next
        if not arg_xdvx:
            return arg_xdvx
        var_rcsn = arg_xdvx
        var_bacg = 0
        while var_rcsn.val != 0:
            var_bacg += var_rcsn.val
            var_rcsn = var_rcsn.next
        arg_xdvx.val = var_bacg
        arg_xdvx.next = arg_ihhe.mergeNodes(var_rcsn)
        return arg_xdvx
