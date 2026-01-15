class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_rcsn()
        var_hqta = arg_xdvx
        while var_hqta:
            var_rgwu = var_bacg
            while var_rgwu.next and var_rgwu.next.val <= var_hqta.val:
                var_rgwu = var_rgwu.next
            var_wrnh = var_hqta.next
            var_hqta.next = var_rgwu.next
            var_rgwu.next = var_hqta
            var_hqta = var_wrnh
        return var_bacg.next
