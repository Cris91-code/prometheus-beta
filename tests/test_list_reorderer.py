import pytest
from src.list_reorderer import reorder_list_with_adjacent_difference

def test_reorder_list_with_adjacent_difference():
    # Test normal cases
    assert reorder_list_with_adjacent_difference([1, 2, 3]) is not None
    assert reorder_list_with_adjacent_difference([3, 2, 1]) is not None
    
    # Test scenarios with allowed differences
    def validate_reordering(original, reordered):
        if reordered is None:
            return False
        
        # Check that reordered uses all original elements
        assert sorted(original) == sorted(reordered)
        
        # Check adjacent differences
        for i in range(1, len(reordered)):
            diff = abs(reordered[i] - reordered[i-1])
            assert diff in (0, 1), f"Invalid difference between {reordered[i-1]} and {reordered[i]}"
        
        return True

    test_cases = [
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [1, 3, 2, 4],
        [5, 4, 6, 3],
        [10, 9, 11, 8]
    ]

    for case in test_cases:
        result = reorder_list_with_adjacent_difference(case)
        assert validate_reordering(case, result)

def test_edge_cases():
    # Empty list
    assert reorder_list_with_adjacent_difference([]) == []
    
    # Single element
    assert reorder_list_with_adjacent_difference([5]) == [5]

def test_impossible_cases():
    # Impossible to reorder to meet conditions
    assert reorder_list_with_adjacent_difference([1, 4, 7, 10]) is None
    assert reorder_list_with_adjacent_difference([100, 200, 300]) is None