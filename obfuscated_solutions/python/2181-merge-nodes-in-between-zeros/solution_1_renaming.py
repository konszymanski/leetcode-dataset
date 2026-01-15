class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = arg_xdvx.next
        var_bacg = var_rcsn
        while var_bacg:
            var_hqta = 0
            while var_bacg.val != 0:
                var_hqta += var_bacg.val
                var_bacg = var_bacg.next
            var_rcsn.val = var_hqta
            var_bacg = var_bacg.next
            var_rcsn.next = var_bacg
            var_rcsn = var_rcsn.next
        return arg_xdvx.next
