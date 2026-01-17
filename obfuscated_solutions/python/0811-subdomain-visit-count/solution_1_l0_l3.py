class Solution(object):

    def subdomainVisits(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            v_junk_79 = 54
            if 1 + 1 == 2:
                (count, domain) = domain.split()
            if 1 + 1 == 2:
                count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                v_junk_93 = 90
                ans['.'.join(frags[i:])] += count
        return ['{} {}'.format(ct, dom) for (dom, ct) in ans.items()]