def func_udax(arg_ihhe, arg_xdvx, arg_rcsn) ->var_wnki:
    var_bacg = var_hqta[var_rgwu[arg_rcsn]]
    var_rgwu[arg_rcsn], var_rgwu[arg_xdvx] = var_rgwu[arg_xdvx], var_rgwu[
        arg_rcsn]
    var_wrnh = arg_ihhe
    for var_osiz in var_ayzf(arg_ihhe, arg_xdvx):
        if var_hqta[var_rgwu[var_osiz]] < var_bacg:
            var_rgwu[var_wrnh], var_rgwu[var_osiz] = var_rgwu[var_osiz
                ], var_rgwu[var_wrnh]
            var_wrnh += 1
    var_rgwu[arg_xdvx], var_rgwu[var_wrnh] = var_rgwu[var_wrnh], var_rgwu[
        arg_xdvx]
    return var_wrnh
