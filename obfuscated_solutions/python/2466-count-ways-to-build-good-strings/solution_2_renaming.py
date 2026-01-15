class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_rgwu:
        var_wrnh = [1] + [-1] * arg_rcsn
        var_osiz = 10 ** 9 + 7

        def func_ayzf(arg_wnki):
            if var_wrnh[arg_wnki] != -1:
                return var_wrnh[arg_wnki]
            var_egyk = 0
            if arg_wnki >= arg_bacg:
                var_egyk += func_ayzf(arg_wnki - arg_bacg)
            if arg_wnki >= arg_hqta:
                var_egyk += func_ayzf(arg_wnki - arg_hqta)
            var_wrnh[arg_wnki] = var_egyk % var_osiz
            return var_wrnh[arg_wnki]
        return var_dcmd(func_ayzf(arg_wnki) for arg_wnki in var_llti(
            arg_xdvx, arg_rcsn + 1)) % var_osiz
