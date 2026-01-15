class Solution:
    var_udax = 20
    var_ihhe = 1048575

    def func_xdvx(arg_rcsn, arg_bacg: var_hqta['TreeNode']) ->var_rjut:
        var_rgwu = var_wrnh([arg_bacg])
        var_osiz = 0
        while var_rgwu:
            var_ayzf = var_wnki(var_rgwu)
            var_egyk = []
            for var_dcmd in var_llti(var_ayzf):
                var_zbxo = var_rgwu.popleft()
                var_egyk.append((var_zbxo.val << arg_rcsn._SHIFT) + var_dcmd)
                if var_zbxo.left:
                    var_rgwu.append(var_zbxo.left)
                if var_zbxo.right:
                    var_rgwu.append(var_zbxo.right)
            var_egyk.sort()
            var_dcmd = 0
            while var_dcmd < var_ayzf:
                var_rdmc = var_egyk[var_dcmd] & arg_rcsn._MASK
                if var_rdmc != var_dcmd:
                    var_egyk[var_dcmd], var_egyk[var_rdmc] = var_egyk[var_rdmc
                        ], var_egyk[var_dcmd]
                    var_osiz += 1
                    var_dcmd -= 1
                var_dcmd += 1
        return var_osiz
