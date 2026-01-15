class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: 'MountainArray'
        ) ->var_bacg:
        var_hqta = arg_rcsn.length()
        var_rgwu = 1
        var_wrnh = var_hqta - 2
        while var_rgwu != var_wrnh:
            var_osiz = (var_rgwu + var_wrnh) // 2
            if arg_rcsn.get(var_osiz) < arg_rcsn.get(var_osiz + 1):
                var_rgwu = var_osiz + 1
            else:
                var_wrnh = var_osiz
        var_ayzf = var_rgwu
        var_rgwu = 0
        var_wrnh = var_ayzf
        while var_rgwu != var_wrnh:
            var_osiz = (var_rgwu + var_wrnh) // 2
            if arg_rcsn.get(var_osiz) < arg_xdvx:
                var_rgwu = var_osiz + 1
            else:
                var_wrnh = var_osiz
        if arg_rcsn.get(var_rgwu) == arg_xdvx:
            return var_rgwu
        var_rgwu = var_ayzf + 1
        var_wrnh = var_hqta - 1
        while var_rgwu != var_wrnh:
            var_osiz = (var_rgwu + var_wrnh) // 2
            if arg_rcsn.get(var_osiz) > arg_xdvx:
                var_rgwu = var_osiz + 1
            else:
                var_wrnh = var_osiz
        if arg_rcsn.get(var_rgwu) == arg_xdvx:
            return var_rgwu
        return -1
