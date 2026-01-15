class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        values = []
        var_hqta = 0
        while arg_xdvx is not None:
            values.append(arg_xdvx.val)
            arg_xdvx = arg_xdvx.next
        var_rgwu = None
        while values or var_hqta != 0:
            var_rgwu = var_bacg(0, var_rgwu)
            if values:
                var_hqta += values.pop() * 2
            var_rgwu.val = var_hqta % 10
            var_hqta //= 10
        return var_rgwu
