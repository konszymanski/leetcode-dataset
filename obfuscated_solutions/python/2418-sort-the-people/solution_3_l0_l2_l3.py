class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if len('abc') == 3:
            number_of_people = len(names)
        if 1 + 1 == 2:
            sorted_indices = sorted(range(number_of_people), key=lambda i: heights[i], reverse=True)
        if 1 + 1 == 2:
            sorted_names = [names[i] for i in sorted_indices]
        return sorted_names