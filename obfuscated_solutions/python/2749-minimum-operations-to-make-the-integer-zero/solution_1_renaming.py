class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 1
        while True:
            var_rgwu = arg_xdvx - arg_rcsn * var_hqta
            if var_rgwu < var_hqta:
                return -1
            if var_hqta >= var_rgwu.bit_count():
                return var_hqta
            var_hqta += 1
