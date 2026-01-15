class CBTInserter(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        arg_xdvx.deque = var_bacg.deque()
        arg_xdvx.root = arg_rcsn
        var_hqta = var_bacg.deque([arg_rcsn])
        while var_hqta:
            var_rgwu = var_hqta.popleft()
            if not var_rgwu.left or not var_rgwu.right:
                arg_xdvx.deque.append(var_rgwu)
            if var_rgwu.left:
                var_hqta.append(var_rgwu.left)
            if var_rgwu.right:
                var_hqta.append(var_rgwu.right)

    def func_wrnh(arg_xdvx, arg_osiz):
        var_rgwu = arg_xdvx.deque[0]
        arg_xdvx.deque.append(var_ayzf(arg_osiz))
        if not var_rgwu.left:
            var_rgwu.left = arg_xdvx.deque[-1]
        else:
            var_rgwu.right = arg_xdvx.deque[-1]
            arg_xdvx.deque.popleft()
        return var_rgwu.val

    def func_wnki(arg_xdvx):
        return arg_xdvx.root
