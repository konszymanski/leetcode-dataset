class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_rdmc:
        var_hqta = 3 * (1 << arg_xdvx - 1)
        if arg_rcsn > var_hqta:
            return ''
        var_rgwu = ['a'] * arg_xdvx
        var_wrnh = {'a': 'b', 'b': 'a', 'c': 'a'}
        var_osiz = {'a': 'c', 'b': 'c', 'c': 'b'}
        var_ayzf = 1
        var_wnki = var_ayzf + (1 << arg_xdvx - 1)
        var_egyk = var_wnki + (1 << arg_xdvx - 1)
        if arg_rcsn < var_wnki:
            var_rgwu[0] = 'a'
            arg_rcsn -= var_ayzf
        elif arg_rcsn < var_egyk:
            var_rgwu[0] = 'b'
            arg_rcsn -= var_wnki
        else:
            var_rgwu[0] = 'c'
            arg_rcsn -= var_egyk
        for var_dcmd in var_llti(1, arg_xdvx):
            var_zbxo = 1 << arg_xdvx - var_dcmd - 1
            if arg_rcsn < var_zbxo:
                var_rgwu[var_dcmd] = var_wrnh[var_rgwu[var_dcmd - 1]]
            else:
                var_rgwu[var_dcmd] = var_osiz[var_rgwu[var_dcmd - 1]]
                arg_rcsn -= var_zbxo
        return ''.join(var_rgwu)
