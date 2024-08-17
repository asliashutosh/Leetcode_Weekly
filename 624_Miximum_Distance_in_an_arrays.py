class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:


        # Initialize with the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        # Iterate over the arrays starting from the second one
        for i in range(1, len(arrays)):
            # Get the first and last elements of the current array
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Calculate possible maximum distances
            max_distance = max(max_distance, abs(current_max - min_val), abs(current_min - max_val))
            
            # Update the global min and max for future comparisons
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
        
        return max_distance

