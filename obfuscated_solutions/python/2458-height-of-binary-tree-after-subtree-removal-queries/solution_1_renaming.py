class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_wrnh]:
        var_osiz = [0] * 100001
        arg_ihhe.current_max_height = 0

        def func_ayzf(arg_wnki, arg_egyk):
            if not arg_wnki:
                return
            var_osiz[arg_wnki.val] = arg_ihhe.current_max_height
            arg_ihhe.current_max_height = var_dcmd(arg_ihhe.
                current_max_height, arg_egyk)
            func_ayzf(arg_wnki.left, arg_egyk + 1)
            func_ayzf(arg_wnki.right, arg_egyk + 1)

        def func_llti(arg_wnki, arg_egyk):
            if not arg_wnki:
                return
            var_osiz[arg_wnki.val] = var_dcmd(var_osiz[arg_wnki.val],
                arg_ihhe.current_max_height)
            arg_ihhe.current_max_height = var_dcmd(arg_egyk, arg_ihhe.
                current_max_height)
            func_llti(arg_wnki.right, arg_egyk + 1)
            func_llti(arg_wnki.left, arg_egyk + 1)
        func_ayzf(arg_xdvx, 0)
        arg_ihhe.current_max_height = 0
        func_llti(arg_xdvx, 0)
        return [var_osiz[var_zbxo] for var_zbxo in arg_rcsn]
