class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int
        ) ->float:
        pass_ratios = []
        for class_ in classes:
            initial_ratio = class_[0] / class_[1]
            pass_ratios.append(initial_ratio)
        while extraStudents > 0:
            updated_ratios = []
            for class_ in classes:
                new_ratio = (class_[0] + 1) / (class_[1] + 1)
                updated_ratios.append(new_ratio)
            best_class_index = 0
            maximum_gain = 0
            i = 0
            while i < len(updated_ratios):
                gain = updated_ratios[i] - pass_ratios[i]
                if gain > maximum_gain:
                    best_class_index = i
                    maximum_gain = gain
                i += 1
            pass_ratios[best_class_index] = updated_ratios[best_class_index]
            classes[best_class_index][0] += 1
            classes[best_class_index][1] += 1
            extraStudents -= 1
        total_pass_ratio = sum(pass_ratios)
        return total_pass_ratio / len(classes)
