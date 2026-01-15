def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu, arg_bacg:
    var_wrnh[var_rgwu, var_osiz[var_rgwu]]):
    if arg_xdvx is None:
        return
    if arg_xdvx.val not in arg_bacg:
        arg_bacg[arg_xdvx.val] = var_ayzf()
    var_wnki = arg_bacg[arg_xdvx.val]
    if arg_rcsn != 0:
        var_wnki.add(arg_rcsn)
    if arg_xdvx.left:
        var_wnki.add(arg_xdvx.left.val)
    if arg_xdvx.right:
        var_wnki.add(arg_xdvx.right.val)
    arg_ihhe.convert(arg_xdvx.left, arg_xdvx.val, arg_bacg)
    arg_ihhe.convert(arg_xdvx.right, arg_xdvx.val, arg_bacg)
