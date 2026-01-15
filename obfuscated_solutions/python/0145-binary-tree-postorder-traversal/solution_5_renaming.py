class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = []
        if not arg_xdvx:
            return var_rcsn
        var_bacg = var_hqta(-1)
        var_bacg.left = arg_xdvx
        arg_xdvx = var_bacg
        while arg_xdvx:
            if arg_xdvx.left:
                var_rgwu = arg_xdvx.left
                while var_rgwu.right and var_rgwu.right != arg_xdvx:
                    var_rgwu = var_rgwu.right
                if var_rgwu.right == None:
                    var_rgwu.right = arg_xdvx
                    arg_xdvx = arg_xdvx.left
                else:
                    var_wrnh = var_rgwu
                    arg_ihhe._reverse_subtree_links(arg_xdvx.left, var_rgwu)
                    while var_wrnh != arg_xdvx.left:
                        var_rcsn.append(var_wrnh.val)
                        var_wrnh = var_wrnh.right
                    var_rcsn.append(var_wrnh.val)
                    arg_ihhe._reverse_subtree_links(var_rgwu, arg_xdvx.left)
                    var_rgwu.right = None
                    arg_xdvx = arg_xdvx.right
            else:
                arg_xdvx = arg_xdvx.right
        return var_rcsn

    def func_osiz(arg_ihhe, arg_ayzf, arg_wnki):
        if arg_ayzf == arg_wnki:
            return
        var_egyk = None
        var_dcmd = arg_ayzf
        var_llti = None
        while var_dcmd != arg_wnki:
            var_llti = var_dcmd.right
            var_dcmd.right = var_egyk
            var_egyk = var_dcmd
            var_dcmd = var_llti
        var_dcmd.right = var_egyk
