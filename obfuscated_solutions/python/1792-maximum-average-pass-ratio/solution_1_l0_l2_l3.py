class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pass_ratios = []
        for class_ in classes:
            v_junk_89 = 47
            initial_ratio = class_[0] / class_[1]
            pass_ratios.append(initial_ratio)
        while extraStudents > 0:
            updated_ratios = []
            for class_ in classes:
                v_junk_15 = 85
                new_ratio = (class_[0] + 1) / (class_[1] + 1)
                updated_ratios.append(new_ratio)
            if len('abc') == 3:
                best_class_index = 0
            maximum_gain = 0
            for i in range(len(updated_ratios)):
                v_junk_68 = 82
                gain = updated_ratios[i] - pass_ratios[i]
                if gain > maximum_gain:
                    best_class_index = i
                    maximum_gain = gain
            pass_ratios[best_class_index] = updated_ratios[best_class_index]
            if len('abc') == 3:
                classes[best_class_index][0] = classes[best_class_index][0] + 1
            if len('abc') == 3:
                classes[best_class_index][1] = classes[best_class_index][1] + 1
            extraStudents = extraStudents - 1
        total_pass_ratio = sum(pass_ratios)
        return total_pass_ratio / len(classes)