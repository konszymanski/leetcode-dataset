class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_llti:
        var_rgwu, var_wrnh, var_osiz = 0, 0, 0
        var_ayzf = arg_xdvx + arg_rcsn + arg_bacg
        var_wnki = []
        for var_egyk in var_dcmd(var_ayzf):
            if (arg_xdvx >= arg_rcsn and arg_xdvx >= arg_bacg and var_rgwu !=
                2 or arg_xdvx > 0 and (var_wrnh == 2 or var_osiz == 2)):
                var_wnki.append('a')
                arg_xdvx -= 1
                var_rgwu += 1
                var_wrnh = 0
                var_osiz = 0
            elif arg_rcsn >= arg_xdvx and arg_rcsn >= arg_bacg and var_wrnh != 2 or arg_rcsn > 0 and (
                var_osiz == 2 or var_rgwu == 2):
                var_wnki.append('b')
                arg_rcsn -= 1
                var_wrnh += 1
                var_rgwu = 0
                var_osiz = 0
            elif arg_bacg >= arg_xdvx and arg_bacg >= arg_rcsn and var_osiz != 2 or arg_bacg > 0 and (
                var_rgwu == 2 or var_wrnh == 2):
                var_wnki.append('c')
                arg_bacg -= 1
                var_osiz += 1
                var_rgwu = 0
                var_wrnh = 0
        return ''.join(var_wnki)
