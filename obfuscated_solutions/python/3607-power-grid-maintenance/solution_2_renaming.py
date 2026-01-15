class Vertex:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn=None):
        arg_ihhe.vertex_id = arg_xdvx
        arg_ihhe.offline = False
        arg_ihhe.power_grid_id = -1
        if arg_xdvx is not None:
            arg_ihhe.vertex_id = arg_xdvx


class Graph:

    def func_udax(arg_ihhe):
        arg_ihhe.adj: var_bacg[var_rcsn, var_hqta[var_rcsn]] = {}
        arg_ihhe.vertices: var_bacg[var_rcsn, var_rgwu] = {}

    def func_wrnh(arg_ihhe, arg_osiz: var_rcsn, arg_ayzf: var_rgwu):
        arg_ihhe.vertices[arg_osiz] = arg_ayzf
        arg_ihhe.adj[arg_osiz] = []

    def func_wnki(arg_ihhe, arg_egyk: var_rcsn, arg_dcmd: var_rcsn):
        arg_ihhe.adj[arg_egyk].append(arg_dcmd)
        arg_ihhe.adj[arg_dcmd].append(arg_egyk)

    def func_llti(arg_ihhe, arg_osiz: var_rcsn) ->var_rgwu:
        return arg_ihhe.vertices[arg_osiz]

    def func_zbxo(arg_ihhe, arg_osiz: var_rcsn) ->var_hqta[var_rcsn]:
        return arg_ihhe.adj[arg_osiz]


class Solution:

    def func_rdmc(arg_ihhe, arg_egyk: var_rgwu, arg_rjut: var_rcsn,
        arg_lsgw: var_hqta[var_rcsn], arg_cbvh: var_yjch):
        arg_egyk.power_grid_id = arg_rjut
        var_dmio.heappush(arg_lsgw, arg_egyk.vertex_id)
        for var_ulfl in arg_cbvh.get_connected_vertices(arg_egyk.vertex_id):
            arg_dcmd = arg_cbvh.get_vertex_value(var_ulfl)
            if arg_dcmd.power_grid_id == -1:
                arg_ihhe.traverse(arg_dcmd, arg_rjut, arg_lsgw, arg_cbvh)

    def func_lgvi(arg_ihhe, arg_wvuc: var_rcsn, arg_tufr: var_hqta[var_hqta
        [var_rcsn]], arg_xhfo: var_hqta[var_hqta[var_rcsn]]) ->var_hqta[
        var_rcsn]:
        arg_cbvh = var_yjch()
        for var_miuw in var_rhvk(arg_wvuc):
            arg_dcmd = var_rgwu(var_miuw + 1)
            arg_cbvh.add_vertex(var_miuw + 1, arg_dcmd)
        for var_yybh in arg_tufr:
            arg_cbvh.add_edge(var_yybh[0], var_yybh[1])
        var_bzkm = []
        arg_rjut = 0
        for var_miuw in var_rhvk(1, arg_wvuc + 1):
            arg_dcmd = arg_cbvh.get_vertex_value(var_miuw)
            if arg_dcmd.power_grid_id == -1:
                arg_lsgw = []
                arg_ihhe.traverse(arg_dcmd, arg_rjut, arg_lsgw, arg_cbvh)
                var_bzkm.append(arg_lsgw)
                arg_rjut += 1
        var_icgs = []
        for var_wkgu in arg_xhfo:
            var_pmuo, var_eieh = var_wkgu[0], var_wkgu[1]
            if var_pmuo == 1:
                var_xrri = arg_cbvh.get_vertex_value(var_eieh)
                if not var_xrri.offline:
                    var_icgs.append(var_eieh)
                else:
                    arg_lsgw = var_bzkm[var_xrri.power_grid_id]
                    while arg_lsgw and arg_cbvh.get_vertex_value(arg_lsgw[0]
                        ).offline:
                        var_dmio.heappop(arg_lsgw)
                    var_icgs.append(arg_lsgw[0] if arg_lsgw else -1)
            elif var_pmuo == 2:
                arg_cbvh.get_vertex_value(var_eieh).offline = True
        return var_icgs
