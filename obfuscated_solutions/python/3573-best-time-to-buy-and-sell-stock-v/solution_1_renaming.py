class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)

        @var_rdmc
        def func_osiz(arg_ayzf, arg_wnki, arg_egyk):
            if arg_wnki == 0:
                return 0
            if arg_ayzf == 0:
                return 0 if arg_egyk == 0 else -arg_xdvx[0
                    ] if arg_egyk == 1 else arg_xdvx[0]
            var_dcmd = arg_xdvx[arg_ayzf]
            if arg_egyk == 0:
                var_llti = var_zbxo(func_osiz(arg_ayzf - 1, arg_wnki, 0), 
                    func_osiz(arg_ayzf - 1, arg_wnki, 1) + var_dcmd, 
                    func_osiz(arg_ayzf - 1, arg_wnki, 2) - var_dcmd)
            elif arg_egyk == 1:
                var_llti = var_zbxo(func_osiz(arg_ayzf - 1, arg_wnki, 1), 
                    func_osiz(arg_ayzf - 1, arg_wnki - 1, 0) - var_dcmd)
            else:
                var_llti = var_zbxo(func_osiz(arg_ayzf - 1, arg_wnki, 2), 
                    func_osiz(arg_ayzf - 1, arg_wnki - 1, 0) + var_dcmd)
            return var_llti
        var_rjut = func_osiz(var_rgwu - 1, arg_rcsn, 0)
        func_osiz.cache_clear()
        return var_rjut
