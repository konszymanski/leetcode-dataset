class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rjut:
        var_hqta, var_rgwu, var_wrnh = var_osiz('-inf'), 0, 0
        var_ayzf = var_wnki.deque()
        var_ayzf.append(arg_xdvx)
        while var_ayzf:
            var_wrnh += 1
            var_egyk = 0
            for var_dcmd in var_llti(var_zbxo(var_ayzf)):
                var_rdmc = var_ayzf.popleft()
                var_egyk += var_rdmc.val
                if var_rdmc.left:
                    var_ayzf.append(var_rdmc.left)
                if var_rdmc.right:
                    var_ayzf.append(var_rdmc.right)
            if var_hqta < var_egyk:
                var_hqta, var_rgwu = var_egyk, var_wrnh
        return var_rgwu
