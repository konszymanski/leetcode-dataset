class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if arg_xdvx.val > 4:
            arg_xdvx = var_rcsn(0, arg_xdvx)
        var_bacg = arg_xdvx
        while var_bacg:
            var_bacg.val = var_bacg.val * 2 % 10
            if var_bacg.next and var_bacg.next.val > 4:
                var_bacg.val += 1
            var_bacg = var_bacg.next
        return arg_xdvx
