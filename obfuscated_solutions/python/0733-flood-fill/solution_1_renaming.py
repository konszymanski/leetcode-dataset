class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta, arg_rgwu):
        var_wrnh, var_osiz = var_ayzf(arg_rcsn), var_ayzf(arg_rcsn[0])
        var_wnki = arg_rcsn[arg_bacg][arg_hqta]
        if var_wnki == arg_rgwu:
            return arg_rcsn

        def func_egyk(arg_dcmd, arg_llti):
            if arg_rcsn[arg_dcmd][arg_llti] == var_wnki:
                arg_rcsn[arg_dcmd][arg_llti] = arg_rgwu
                if arg_dcmd >= 1:
                    func_egyk(arg_dcmd - 1, arg_llti)
                if arg_dcmd + 1 < var_wrnh:
                    func_egyk(arg_dcmd + 1, arg_llti)
                if arg_llti >= 1:
                    func_egyk(arg_dcmd, arg_llti - 1)
                if arg_llti + 1 < var_osiz:
                    func_egyk(arg_dcmd, arg_llti + 1)
        func_egyk(arg_bacg, arg_hqta)
        return arg_rcsn
