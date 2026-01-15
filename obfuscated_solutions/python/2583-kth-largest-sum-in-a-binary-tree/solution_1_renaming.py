class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = []
        var_wrnh = var_osiz()
        var_wrnh.append(arg_xdvx)
        while var_wrnh:
            var_ayzf = var_wnki(var_wrnh)
            var_egyk = 0
            for var_dcmd in var_llti(var_ayzf):
                var_zbxo = var_wrnh.popleft()
                var_egyk += var_zbxo.val
                if var_zbxo.left:
                    var_wrnh.append(var_zbxo.left)
                if var_zbxo.right:
                    var_wrnh.append(var_zbxo.right)
            var_rdmc.heappush(var_rgwu, -var_egyk)
        if var_wnki(var_rgwu) < arg_rcsn:
            return -1
        for var_dcmd in var_llti(arg_rcsn - 1):
            var_rdmc.heappop(var_rgwu)
        return -var_rdmc.heappop(var_rgwu)
