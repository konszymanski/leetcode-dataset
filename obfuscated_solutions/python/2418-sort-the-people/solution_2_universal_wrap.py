class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) ->List[str]:
        if True:
            number_of_people = len(names)
        height_to_name_map = OrderedDict()
        if True:
            for height, name in zip(heights, names):
                height_to_name_map[height] = name
        height_to_name_map = OrderedDict(sorted(height_to_name_map.items(),
            reverse=True))
        sorted_names = list(height_to_name_map.values())
        if True:
            return sorted_names
