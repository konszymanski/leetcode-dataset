class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        var_rcsn = var_bacg(arg_xdvx) - 2
        while var_rcsn >= 0 and arg_xdvx[var_rcsn + 1] <= arg_xdvx[var_rcsn]:
            var_rcsn -= 1
        if var_rcsn >= 0:
            var_hqta = var_bacg(arg_xdvx) - 1
            while arg_xdvx[var_hqta] <= arg_xdvx[var_rcsn]:
                var_hqta -= 1
            arg_ihhe.swap(arg_xdvx, var_rcsn, var_hqta)
        arg_ihhe.reverse(arg_xdvx, var_rcsn + 1)

    def func_rgwu(arg_ihhe, arg_xdvx, arg_wrnh):
        var_rcsn, var_hqta = arg_wrnh, var_bacg(arg_xdvx) - 1
        while var_rcsn < var_hqta:
            arg_ihhe.swap(arg_xdvx, var_rcsn, var_hqta)
            var_rcsn += 1
            var_hqta -= 1

    def func_osiz(arg_ihhe, arg_xdvx, var_rcsn, var_hqta):
        var_ayzf = arg_xdvx[var_rcsn]
        arg_xdvx[var_rcsn] = arg_xdvx[var_hqta]
        arg_xdvx[var_hqta] = var_ayzf
