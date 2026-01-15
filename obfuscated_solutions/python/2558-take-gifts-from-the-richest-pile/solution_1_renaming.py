class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        for var_rgwu in var_wrnh(arg_rcsn):
            var_osiz = 0
            for var_ayzf in var_wrnh(var_bacg):
                if arg_xdvx[var_osiz] < arg_xdvx[var_ayzf]:
                    var_osiz = var_ayzf
            arg_xdvx[var_osiz] = var_wnki.floor(var_wnki.sqrt(arg_xdvx[
                var_osiz]))
        var_egyk = var_dcmd(arg_xdvx)
        return var_egyk
