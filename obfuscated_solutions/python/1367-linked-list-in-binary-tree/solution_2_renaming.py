class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_ayzf:
        if not arg_rcsn:
            return False
        var_wrnh = [arg_rcsn]
        while var_wrnh:
            var_osiz = var_wrnh.pop()
            if arg_ihhe._is_match(var_osiz, arg_xdvx):
                return True
            if var_osiz.left:
                var_wrnh.append(var_osiz.left)
            if var_osiz.right:
                var_wrnh.append(var_osiz.right)
        return False

    def func_wnki(arg_ihhe, var_osiz: var_bacg[var_rgwu], arg_egyk:
        var_bacg[var_hqta]) ->var_ayzf:
        var_wrnh = [(var_osiz, arg_egyk)]
        while var_wrnh:
            var_dcmd, var_llti = var_wrnh.pop()
            while var_dcmd and var_llti:
                if var_dcmd.val != var_llti.val:
                    break
                var_llti = var_llti.next
                if var_llti:
                    if var_dcmd.left:
                        var_wrnh.append((var_dcmd.left, var_llti))
                    if var_dcmd.right:
                        var_wrnh.append((var_dcmd.right, var_llti))
                    break
            if not var_llti:
                return True
        return False
