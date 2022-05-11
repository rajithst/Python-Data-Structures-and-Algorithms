class Solution:
    def solve(self, weights, values, capacity):

        N = len(weights)

        def knaspack(index, remaining_weight):
            if index == 0 or remaining_weight == 0:
                return 0

            include = 0
            exclude = 0
            value, weight = values[index - 1], weights[index - 1],
            if weight <= remaining_weight:
                include = value + knaspack(index - 1, remaining_weight - weight)
            exclude = knaspack(index - 1, remaining_weight)
            return max(include, exclude)

        return knaspack(N, capacity)
