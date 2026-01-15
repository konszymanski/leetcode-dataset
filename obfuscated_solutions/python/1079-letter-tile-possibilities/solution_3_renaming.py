class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = var_hqta()
        var_rgwu = ''.join(var_wrnh(arg_xdvx))
        return arg_ihhe._generate_sequences(var_rgwu, '', 0, var_bacg) - 1

    def func_ayzf(arg_ihhe, arg_wnki: var_osiz) ->var_osiz:
        if arg_wnki <= 1:
            return 1
        var_egyk = 1
        for var_dcmd in var_llti(2, arg_wnki + 1):
            var_egyk *= var_dcmd
        return var_egyk

    def func_zbxo(arg_ihhe, arg_rdmc: var_rcsn) ->var_osiz:
        var_rjut = arg_ihhe._factorial(var_lsgw(arg_rdmc))
        for var_cbvh in var_yjch(arg_rdmc).values():
            var_rjut //= arg_ihhe._factorial(var_cbvh)
        return var_rjut

    def func_dmio(arg_ihhe, arg_xdvx: var_rcsn, arg_ulfl: var_rcsn,
        arg_lgvi: var_osiz, var_bacg: var_hqta) ->var_osiz:
        if arg_lgvi >= var_lsgw(arg_xdvx):
            if arg_ulfl not in var_bacg:
                var_bacg.add(arg_ulfl)
                return arg_ihhe._count_permutations(arg_ulfl)
            return 0
        return arg_ihhe._generate_sequences(arg_xdvx, arg_ulfl, arg_lgvi + 
            1, var_bacg) + arg_ihhe._generate_sequences(arg_xdvx, arg_ulfl +
            arg_xdvx[arg_lgvi], arg_lgvi + 1, var_bacg)
