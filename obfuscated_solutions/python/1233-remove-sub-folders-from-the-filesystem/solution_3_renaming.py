class Solution:


    class TrieNode:

        def func_udax(arg_ihhe):
            arg_ihhe.is_end_of_folder = False
            arg_ihhe.children = {}

    def func_udax(arg_ihhe):
        arg_ihhe.root = arg_ihhe.TrieNode()

    def func_xdvx(arg_ihhe, arg_rcsn):
        for var_bacg in arg_rcsn:
            var_hqta = arg_ihhe.root
            var_rgwu = var_bacg.split('/')
            for var_wrnh in var_rgwu:
                if var_wrnh == '':
                    continue
                if var_wrnh not in var_hqta.children:
                    var_hqta.children[var_wrnh] = arg_ihhe.TrieNode()
                var_hqta = var_hqta.children[var_wrnh]
            var_hqta.is_end_of_folder = True
        var_osiz = []
        for var_bacg in arg_rcsn:
            var_hqta = arg_ihhe.root
            var_rgwu = var_bacg.split('/')
            var_ayzf = False
            for var_wnki, var_wrnh in var_egyk(var_rgwu):
                if var_wrnh == '':
                    continue
                var_dcmd = var_hqta.children[var_wrnh]
                if var_dcmd.is_end_of_folder and var_wnki != var_llti(var_rgwu
                    ) - 1:
                    var_ayzf = True
                    break
                var_hqta = var_dcmd
            if not var_ayzf:
                var_osiz.append(var_bacg)
        return var_osiz
