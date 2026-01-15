class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_zbxo[var_ayzf]:

        def func_hqta(arg_rgwu, arg_wrnh):
            if not arg_rgwu:
                return
            arg_wrnh[arg_rgwu.val] += 1
            func_hqta(arg_rgwu.left, arg_wrnh)
            func_hqta(arg_rgwu.right, arg_wrnh)
        arg_wrnh = var_osiz(var_ayzf)
        func_hqta(arg_xdvx, arg_wrnh)
        var_wnki = var_egyk(arg_wrnh.values())
        var_dcmd = []
        for var_llti in arg_wrnh:
            if arg_wrnh[var_llti] == var_wnki:
                var_dcmd.append(var_llti)
        return var_dcmd
