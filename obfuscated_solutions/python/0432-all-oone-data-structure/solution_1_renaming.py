class Node:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.freq = arg_xdvx
        arg_ihhe.prev = None
        arg_ihhe.next = None
        arg_ihhe.keys = var_rcsn()


class AllOne:

    def func_udax(arg_ihhe):
        arg_ihhe.head = var_bacg(0)
        arg_ihhe.tail = var_bacg(0)
        arg_ihhe.head.next = arg_ihhe.tail
        arg_ihhe.tail.prev = arg_ihhe.head
        arg_ihhe.map = {}

    def func_hqta(arg_ihhe, arg_rgwu: var_wrnh) ->None:
        if arg_rgwu in arg_ihhe.map:
            var_osiz = arg_ihhe.map[arg_rgwu]
            arg_xdvx = var_osiz.freq
            var_osiz.keys.remove(arg_rgwu)
            var_ayzf = var_osiz.next
            if var_ayzf == arg_ihhe.tail or var_ayzf.freq != arg_xdvx + 1:
                var_wnki = var_bacg(arg_xdvx + 1)
                var_wnki.keys.add(arg_rgwu)
                var_wnki.prev = var_osiz
                var_wnki.next = var_ayzf
                var_osiz.next = var_wnki
                var_ayzf.prev = var_wnki
                arg_ihhe.map[arg_rgwu] = var_wnki
            else:
                var_ayzf.keys.add(arg_rgwu)
                arg_ihhe.map[arg_rgwu] = var_ayzf
            if not var_osiz.keys:
                arg_ihhe.removeNode(var_osiz)
        else:
            var_egyk = arg_ihhe.head.next
            if var_egyk == arg_ihhe.tail or var_egyk.freq > 1:
                var_wnki = var_bacg(1)
                var_wnki.keys.add(arg_rgwu)
                var_wnki.prev = arg_ihhe.head
                var_wnki.next = var_egyk
                arg_ihhe.head.next = var_wnki
                var_egyk.prev = var_wnki
                arg_ihhe.map[arg_rgwu] = var_wnki
            else:
                var_egyk.keys.add(arg_rgwu)
                arg_ihhe.map[arg_rgwu] = var_egyk

    def func_dcmd(arg_ihhe, arg_rgwu: var_wrnh) ->None:
        if arg_rgwu not in arg_ihhe.map:
            return
        var_osiz = arg_ihhe.map[arg_rgwu]
        var_osiz.keys.remove(arg_rgwu)
        arg_xdvx = var_osiz.freq
        if arg_xdvx == 1:
            del arg_ihhe.map[arg_rgwu]
        else:
            var_llti = var_osiz.prev
            if var_llti == arg_ihhe.head or var_llti.freq != arg_xdvx - 1:
                var_wnki = var_bacg(arg_xdvx - 1)
                var_wnki.keys.add(arg_rgwu)
                var_wnki.prev = var_llti
                var_wnki.next = var_osiz
                var_llti.next = var_wnki
                var_osiz.prev = var_wnki
                arg_ihhe.map[arg_rgwu] = var_wnki
            else:
                var_llti.keys.add(arg_rgwu)
                arg_ihhe.map[arg_rgwu] = var_llti
        if not var_osiz.keys:
            arg_ihhe.removeNode(var_osiz)

    def func_zbxo(arg_ihhe) ->var_wrnh:
        if arg_ihhe.tail.prev == arg_ihhe.head:
            return ''
        return var_rdmc(var_rjut(arg_ihhe.tail.prev.keys))

    def func_lsgw(arg_ihhe) ->var_wrnh:
        if arg_ihhe.head.next == arg_ihhe.tail:
            return ''
        return var_rdmc(var_rjut(arg_ihhe.head.next.keys))

    def func_cbvh(arg_ihhe, var_osiz):
        var_llti = var_osiz.prev
        var_ayzf = var_osiz.next
        var_llti.next = var_ayzf
        var_ayzf.prev = var_llti
