class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz([(1, 1)]), var_osiz([])
        var_ayzf, var_wnki = 1, 0
        for var_egyk in var_dcmd(2, arg_xdvx + 1):
            if var_rgwu and var_rgwu[0][0] == var_egyk - arg_rcsn:
                var_ayzf -= var_rgwu[0][1]
                var_wnki += var_rgwu[0][1]
                var_wrnh.append(var_rgwu[0])
                var_rgwu.popleft()
            if var_wrnh and var_wrnh[0][0] == var_egyk - arg_bacg:
                var_wnki -= var_wrnh[0][1]
                var_wrnh.popleft()
            if var_wrnh:
                var_ayzf += var_wnki
                var_rgwu.append((var_egyk, var_wnki))
        return (var_ayzf + var_wnki) % (10 ** 9 + 7)
