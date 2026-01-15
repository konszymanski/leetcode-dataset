class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti:
        var_hqta = var_rgwu()
        var_wrnh = arg_xdvx
        var_hqta.append(var_wrnh)
        var_osiz = True
        while var_hqta:
            var_ayzf = var_wnki(var_hqta)
            var_egyk = var_dcmd('inf')
            if var_osiz:
                var_egyk = -var_egyk
            while var_ayzf > 0:
                var_wrnh = var_hqta.popleft()
                if var_osiz and (var_wrnh.val % 2 == 0 or var_wrnh.val <=
                    var_egyk) or not var_osiz and (var_wrnh.val % 2 == 1 or
                    var_wrnh.val >= var_egyk):
                    return False
                var_egyk = var_wrnh.val
                if var_wrnh.left:
                    var_hqta.append(var_wrnh.left)
                if var_wrnh.right:
                    var_hqta.append(var_wrnh.right)
                var_ayzf -= 1
            var_osiz = not var_osiz
        return True
