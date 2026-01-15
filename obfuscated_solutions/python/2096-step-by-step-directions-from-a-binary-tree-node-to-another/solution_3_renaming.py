class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_dcmd:
        var_wrnh = []
        var_osiz = []
        arg_ihhe._find_path(arg_xdvx, arg_rcsn, var_wrnh)
        arg_ihhe._find_path(arg_xdvx, arg_bacg, var_osiz)
        var_ayzf = []
        var_wnki = 0
        while var_wnki < var_egyk(var_wrnh) and var_wnki < var_egyk(var_osiz
            ) and var_wrnh[var_wnki] == var_osiz[var_wnki]:
            var_wnki += 1
        var_ayzf.extend('U' * (var_egyk(var_wrnh) - var_wnki))
        var_ayzf.extend(var_osiz[var_wnki:])
        return ''.join(var_ayzf)

    def func_llti(arg_ihhe, arg_zbxo: var_hqta, arg_rdmc: var_rgwu,
        arg_rjut: var_lsgw[var_dcmd]) ->var_cbvh:
        if arg_zbxo is None:
            return False
        if arg_zbxo.val == arg_rdmc:
            return True
        arg_rjut.append('L')
        if arg_ihhe._find_path(arg_zbxo.left, arg_rdmc, arg_rjut):
            return True
        arg_rjut.pop()
        arg_rjut.append('R')
        if arg_ihhe._find_path(arg_zbxo.right, arg_rdmc, arg_rjut):
            return True
        arg_rjut.pop()
        return False
