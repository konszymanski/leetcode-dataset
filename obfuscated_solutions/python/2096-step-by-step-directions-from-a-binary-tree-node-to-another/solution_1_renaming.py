class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_rjut:
        var_wrnh = {}
        var_osiz = arg_ihhe._find_start_node(arg_xdvx, arg_rcsn)
        arg_ihhe._populate_parent_map(arg_xdvx, var_wrnh)
        var_ayzf = var_wnki([var_osiz])
        var_egyk = var_dcmd()
        var_llti = {}
        var_egyk.add(var_osiz)
        while var_ayzf:
            var_zbxo = var_ayzf.popleft()
            if var_zbxo.val == arg_bacg:
                return arg_ihhe._backtrack_path(var_zbxo, var_llti)
            if var_zbxo.val in var_wrnh:
                var_rdmc = var_wrnh[var_zbxo.val]
                if var_rdmc not in var_egyk:
                    var_ayzf.append(var_rdmc)
                    var_llti[var_rdmc] = var_zbxo, 'U'
                    var_egyk.add(var_rdmc)
            if var_zbxo.left and var_zbxo.left not in var_egyk:
                var_ayzf.append(var_zbxo.left)
                var_llti[var_zbxo.left] = var_zbxo, 'L'
                var_egyk.add(var_zbxo.left)
            if var_zbxo.right and var_zbxo.right not in var_egyk:
                var_ayzf.append(var_zbxo.right)
                var_llti[var_zbxo.right] = var_zbxo, 'R'
                var_egyk.add(var_zbxo.right)
        return ''

    def func_lsgw(arg_ihhe, arg_cbvh, var_llti):
        var_yjch = []
        while arg_cbvh in var_llti:
            var_yjch.append(var_llti[arg_cbvh][1])
            arg_cbvh = var_llti[arg_cbvh][0]
        var_yjch.reverse()
        return ''.join(var_yjch)

    def func_dmio(arg_ihhe, arg_cbvh, var_wrnh):
        if not arg_cbvh:
            return
        if arg_cbvh.left:
            var_wrnh[arg_cbvh.left.val] = arg_cbvh
            arg_ihhe._populate_parent_map(arg_cbvh.left, var_wrnh)
        if arg_cbvh.right:
            var_wrnh[arg_cbvh.right.val] = arg_cbvh
            arg_ihhe._populate_parent_map(arg_cbvh.right, var_wrnh)

    def func_ulfl(arg_ihhe, arg_cbvh, arg_lgvi):
        if not arg_cbvh:
            return None
        if arg_cbvh.val == arg_lgvi:
            return arg_cbvh
        var_wvuc = arg_ihhe._find_start_node(arg_cbvh.left, arg_lgvi)
        if var_wvuc:
            return var_wvuc
        return arg_ihhe._find_start_node(arg_cbvh.right, arg_lgvi)
