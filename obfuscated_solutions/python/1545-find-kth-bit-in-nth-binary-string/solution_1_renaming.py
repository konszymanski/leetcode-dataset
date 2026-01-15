class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_egyk:
        var_hqta = '0'
        for var_rgwu in var_wrnh(1, arg_xdvx):
            if arg_rcsn <= var_osiz(var_hqta):
                break
            var_hqta += '1'
            var_ayzf = ''.join('1' if var_wnki == '0' else '0' for var_wnki in
                var_hqta[:-1])
            var_hqta += var_ayzf[::-1]
        return var_hqta[arg_rcsn - 1]
