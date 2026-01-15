class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """

        def func_hqta(arg_rgwu, arg_wrnh):
            var_osiz = 0
            while var_osiz < arg_wrnh / 2:
                arg_rgwu[var_osiz], arg_rgwu[arg_wrnh - var_osiz - 1
                    ] = arg_rgwu[arg_wrnh - var_osiz - 1], arg_rgwu[var_osiz]
                var_osiz += 1
        var_ayzf = []
        var_wnki = var_egyk(arg_xdvx)
        while var_wnki > 0:
            var_dcmd = arg_xdvx.index(var_wnki)
            if var_dcmd != var_wnki - 1:
                if var_dcmd != 0:
                    var_ayzf.append(var_dcmd + 1)
                    func_hqta(arg_xdvx, var_dcmd + 1)
                var_ayzf.append(var_wnki)
                func_hqta(arg_xdvx, var_wnki)
            var_wnki -= 1
        return var_ayzf
