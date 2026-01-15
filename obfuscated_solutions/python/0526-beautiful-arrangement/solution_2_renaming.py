class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        """
        :type N: int
        :rtype: int
        """
        arg_xdvx.count = 0
        var_bacg = [(var_hqta + 1) for var_hqta in var_rgwu(arg_rcsn)]
        arg_xdvx.permute(var_bacg, 0)
        return arg_xdvx.count

    def func_wrnh(arg_xdvx, var_bacg, arg_osiz):
        if arg_osiz == var_ayzf(var_bacg):
            arg_xdvx.count += 1
        for var_hqta in var_rgwu(arg_osiz, var_ayzf(var_bacg)):
            var_bacg[var_hqta], var_bacg[arg_osiz] = var_bacg[arg_osiz
                ], var_bacg[var_hqta]
            if var_bacg[arg_osiz] % (arg_osiz + 1) == 0 or (arg_osiz + 1
                ) % var_bacg[arg_osiz] == 0:
                arg_xdvx.permute(var_bacg, arg_osiz + 1)
            var_bacg[var_hqta], var_bacg[arg_osiz] = var_bacg[arg_osiz
                ], var_bacg[var_hqta]
