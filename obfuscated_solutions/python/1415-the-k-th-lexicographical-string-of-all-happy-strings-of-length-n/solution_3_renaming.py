class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_egyk:
        var_hqta = []
        var_rgwu = 0
        var_hqta.append('')
        while var_hqta:
            var_wrnh = var_hqta.pop()
            if var_osiz(var_wrnh) == arg_xdvx:
                var_rgwu += 1
                if var_rgwu == arg_rcsn:
                    return var_wrnh
                continue
            for var_ayzf in var_wnki(['a', 'b', 'c']):
                if var_osiz(var_wrnh) == 0 or var_wrnh[-1] != var_ayzf:
                    var_hqta.append(var_wrnh + var_ayzf)
        return ''
