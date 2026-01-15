class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = {var_rgwu(var_wrnh) for var_wrnh in arg_bacg}
        var_osiz = 0
        for var_ayzf in var_wnki(arg_rcsn):
            for var_egyk in var_wnki(arg_rcsn):
                var_dcmd = 0
                while (var_dcmd <= var_ayzf < arg_rcsn - var_dcmd and 
                    var_dcmd <= var_egyk < arg_rcsn - var_dcmd and (
                    var_ayzf - var_dcmd, var_egyk) not in var_hqta and (
                    var_ayzf + var_dcmd, var_egyk) not in var_hqta and (
                    var_ayzf, var_egyk - var_dcmd) not in var_hqta and (
                    var_ayzf, var_egyk + var_dcmd) not in var_hqta):
                    var_dcmd += 1
                var_osiz = var_llti(var_osiz, var_dcmd)
        return var_osiz
