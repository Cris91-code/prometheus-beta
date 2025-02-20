def reorder_list_with_adjacent_difference(nums):
    """
    Reorder a list of integers so that the difference between consecutive elements 
    is always 1, -1, or 0. If impossible, return None.
    
    Args:
        nums (list): A list of integers to be reordered
    
    Returns:
        list or None: Reordered list or None if reordering is impossible
    """
    if not nums:
        return []
    
    def backtrack(current_list, remaining):
        # Base case: all numbers have been used
        if not remaining:
            return current_list
        
        # Try each remaining number
        for i in range(len(remaining)):
            num = remaining[i]
            
            # Check if the number can be added (valid adjacent difference)
            if not current_list or abs(current_list[-1] - num) <= 1:
                # Make a copy to track remaining numbers
                new_remaining = remaining[:i] + remaining[i+1:]
                
                # Recursively try this arrangement
                result = backtrack(current_list + [num], new_remaining)
                if result is not None:
                    return result
        
        # No valid arrangement found
        return None
    
    # Try all possible starting points
    for start_index in range(len(nums)):
        start_num = nums[start_index]
        remaining = nums[:start_index] + nums[start_index+1:]
        
        result = backtrack([start_num], remaining)
        if result is not None:
            return result
    
    return None