class TrieNode(var_udax):
    var_ihhe = 'children', 'score'

    def func_xdvx(arg_rcsn):
        arg_rcsn.children = {}
        arg_rcsn.score = 0


class MapSum(var_udax):

    def func_xdvx(arg_rcsn):
        arg_rcsn.map = {}
        arg_rcsn.root = var_bacg()

    def func_hqta(arg_rcsn, arg_rgwu, arg_wrnh):
        var_osiz = arg_wrnh - arg_rcsn.map.get(arg_rgwu, 0)
        arg_rcsn.map[arg_rgwu] = arg_wrnh
        var_ayzf = arg_rcsn.root
        var_ayzf.score += var_osiz
        for var_wnki in arg_rgwu:
            var_ayzf = var_ayzf.children.setdefault(var_wnki, var_bacg())
            var_ayzf.score += var_osiz

    def func_egyk(arg_rcsn, arg_dcmd):
        var_ayzf = arg_rcsn.root
        for var_wnki in arg_dcmd:
            if var_wnki not in var_ayzf.children:
                return 0
            var_ayzf = var_ayzf.children[var_wnki]
        return var_ayzf.score
