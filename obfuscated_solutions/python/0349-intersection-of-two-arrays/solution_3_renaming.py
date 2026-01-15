class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        return [var_bacg for var_bacg in arg_xdvx if var_bacg in arg_rcsn]

    def func_hqta(arg_ihhe, arg_rgwu, arg_wrnh):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arg_xdvx = var_osiz(arg_rgwu)
        arg_rcsn = var_osiz(arg_wrnh)
        if var_ayzf(arg_xdvx) < var_ayzf(arg_rcsn):
            return arg_ihhe.set_intersection(arg_xdvx, arg_rcsn)
        else:
            return arg_ihhe.set_intersection(arg_rcsn, arg_xdvx)
