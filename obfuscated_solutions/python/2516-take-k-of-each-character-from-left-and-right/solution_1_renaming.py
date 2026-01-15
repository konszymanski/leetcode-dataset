class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.min_minutes = var_xdvx('inf')

    def func_rcsn(arg_ihhe, arg_bacg: var_rgwu, arg_hqta: var_wrnh) ->var_wrnh:
        if arg_hqta == 0:
            return 0
        var_osiz = [0, 0, 0]
        arg_ihhe._solve(arg_bacg, arg_hqta, 0, var_ayzf(arg_bacg) - 1,
            var_osiz, 0)
        return -1 if arg_ihhe.min_minutes == var_xdvx('inf'
            ) else arg_ihhe.min_minutes

    def func_wnki(arg_ihhe, arg_bacg, arg_hqta, arg_egyk, arg_dcmd,
        var_osiz, arg_llti):
        if var_osiz[0] >= arg_hqta and var_osiz[1] >= arg_hqta and var_osiz[2
            ] >= arg_hqta:
            arg_ihhe.min_minutes = var_zbxo(arg_ihhe.min_minutes, arg_llti)
            return
        if arg_egyk > arg_dcmd:
            return
        var_rdmc = var_osiz.copy()
        var_rdmc[var_rjut(arg_bacg[arg_egyk]) - var_rjut('a')] += 1
        arg_ihhe._solve(arg_bacg, arg_hqta, arg_egyk + 1, arg_dcmd,
            var_rdmc, arg_llti + 1)
        var_lsgw = var_osiz.copy()
        var_lsgw[var_rjut(arg_bacg[arg_dcmd]) - var_rjut('a')] += 1
        arg_ihhe._solve(arg_bacg, arg_hqta, arg_egyk, arg_dcmd - 1,
            var_lsgw, arg_llti + 1)
