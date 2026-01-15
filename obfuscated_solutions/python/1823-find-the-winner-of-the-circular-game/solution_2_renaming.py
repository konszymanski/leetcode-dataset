class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu(var_wrnh(1, arg_xdvx + 1))
        while var_osiz(var_hqta) > 1:
            for var_ayzf in var_wrnh(arg_rcsn - 1):
                var_hqta.append(var_hqta.popleft())
            var_hqta.popleft()
        return var_hqta[0]
