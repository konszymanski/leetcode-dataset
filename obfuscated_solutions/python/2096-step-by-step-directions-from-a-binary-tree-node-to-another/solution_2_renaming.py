class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_dcmd:
        var_wrnh = arg_ihhe._find_lowest_common_ancestor(arg_xdvx, arg_rcsn,
            arg_bacg)
        var_osiz = []
        var_ayzf = []
        arg_ihhe._find_path(var_wrnh, arg_rcsn, var_osiz)
        arg_ihhe._find_path(var_wrnh, arg_bacg, var_ayzf)
        var_wnki = []
        var_wnki.extend('U' * var_egyk(var_osiz))
        var_wnki.extend(var_ayzf)
        return ''.join(var_wnki)

    def func_llti(arg_ihhe, arg_zbxo: var_hqta, arg_rdmc: var_rgwu,
        arg_rjut: var_rgwu) ->var_hqta:
        if arg_zbxo is None:
            return None
        if arg_zbxo.val == arg_rdmc or arg_zbxo.val == arg_rjut:
            return arg_zbxo
        var_lsgw = arg_ihhe._find_lowest_common_ancestor(arg_zbxo.left,
            arg_rdmc, arg_rjut)
        var_cbvh = arg_ihhe._find_lowest_common_ancestor(arg_zbxo.right,
            arg_rdmc, arg_rjut)
        if var_lsgw is None:
            return var_cbvh
        elif var_cbvh is None:
            return var_lsgw
        else:
            return arg_zbxo

    def func_yjch(arg_ihhe, arg_zbxo: var_hqta, arg_dmio: var_rgwu,
        arg_ulfl: var_lgvi[var_dcmd]) ->var_wvuc:
        if arg_zbxo is None:
            return False
        if arg_zbxo.val == arg_dmio:
            return True
        arg_ulfl.append('L')
        if arg_ihhe._find_path(arg_zbxo.left, arg_dmio, arg_ulfl):
            return True
        arg_ulfl.pop()
        arg_ulfl.append('R')
        if arg_ihhe._find_path(arg_zbxo.right, arg_dmio, arg_ulfl):
            return True
        arg_ulfl.pop()
        return False
