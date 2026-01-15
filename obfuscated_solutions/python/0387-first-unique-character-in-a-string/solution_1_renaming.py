class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        """
        :type s: str
        :rtype: int
        """
        var_bacg = var_hqta.Counter(arg_xdvx)
        for var_rgwu, var_wrnh in var_osiz(arg_xdvx):
            if var_bacg[var_wrnh] == 1:
                return var_rgwu
        return -1
