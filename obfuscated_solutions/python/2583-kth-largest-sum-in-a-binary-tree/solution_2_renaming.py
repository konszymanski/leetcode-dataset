class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = var_rgwu()
        var_hqta.append(arg_xdvx)
        while var_hqta:
            var_wrnh = var_osiz(var_hqta)
            var_ayzf = 0
            for var_wnki in var_egyk(var_wrnh):
                var_dcmd = var_hqta.popleft()
                var_ayzf += var_dcmd.val
                if var_dcmd.left is not None:
                    var_hqta.append(var_dcmd.left)
                if var_dcmd.right is not None:
                    var_hqta.append(var_dcmd.right)
            var_llti.heappush(var_bacg, var_ayzf)
            if var_osiz(var_bacg) > arg_rcsn:
                var_llti.heappop(var_bacg)
        if var_osiz(var_bacg) < arg_rcsn:
            return -1
        return var_bacg[0]
