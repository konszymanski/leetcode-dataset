class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if 1 + 1 == 2:
            number_of_people = len(names)
        height_to_name_map = OrderedDict()
        for (height, name) in zip(heights, names):
            v_junk_63 = 29
            height_to_name_map[height] = name
        height_to_name_map = OrderedDict(sorted(height_to_name_map.items(), reverse=True))
        if 1 + 1 == 2:
            sorted_names = list(height_to_name_map.values())
        return sorted_names