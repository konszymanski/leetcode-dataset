class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if not arg_xdvx:
            return None
        var_bacg = var_rcsn(0)
        var_bacg.right = arg_xdvx
        var_hqta = var_bacg
        while var_hqta.right:
            if var_hqta.right.left:
                arg_ihhe.right_rotate(var_hqta, var_hqta.right)
            else:
                var_hqta = var_hqta.right
        var_rgwu = 0
        var_hqta = var_bacg.right
        while var_hqta:
            var_rgwu += 1
            var_hqta = var_hqta.right
        var_wrnh = 2 ** var_osiz.floor(var_osiz.log2(var_rgwu + 1)) - 1
        arg_ihhe.make_rotations(var_bacg, var_rgwu - var_wrnh)
        while var_wrnh > 1:
            var_wrnh //= 2
            arg_ihhe.make_rotations(var_bacg, var_wrnh)
        var_ayzf = var_bacg.right
        var_bacg = None
        return var_ayzf

    def func_wnki(arg_ihhe, arg_egyk: var_rcsn, arg_dcmd: var_rcsn):
        var_llti = arg_dcmd.left
        arg_dcmd.left = var_llti.right
        var_llti.right = arg_dcmd
        arg_egyk.right = var_llti

    def func_zbxo(arg_ihhe, arg_egyk: var_rcsn, arg_dcmd: var_rcsn):
        var_llti = arg_dcmd.right
        arg_dcmd.right = var_llti.left
        var_llti.left = arg_dcmd
        arg_egyk.right = var_llti

    def func_rdmc(arg_ihhe, var_bacg: var_rcsn, arg_rjut: var_lsgw):
        var_hqta = var_bacg
        for var_cbvh in var_yjch(arg_rjut):
            var_llti = var_hqta.right
            arg_ihhe.left_rotate(var_hqta, var_llti)
            var_hqta = var_hqta.right
