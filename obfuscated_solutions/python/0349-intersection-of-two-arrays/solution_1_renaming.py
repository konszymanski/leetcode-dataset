class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arg_rcsn.sort()
        arg_bacg.sort()
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = var_rgwu(arg_bacg)
        var_osiz = 0
        var_ayzf = 0
        func_ihhe = var_wnki()
        while var_osiz < var_hqta and var_ayzf < var_wrnh:
            if arg_rcsn[var_osiz] == arg_bacg[var_ayzf]:
                func_ihhe.add(arg_rcsn[var_osiz])
                var_osiz += 1
                var_ayzf += 1
            elif arg_rcsn[var_osiz] < arg_bacg[var_ayzf]:
                var_osiz += 1
            else:
                var_ayzf += 1
        var_egyk = []
        for var_dcmd in func_ihhe:
            var_egyk.append(var_dcmd)
        return var_egyk
