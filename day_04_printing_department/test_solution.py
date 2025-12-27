import os
from solution import count_adjacent_rolls, count_accessible, count_accessible_with_iter_remove


def read_example():
    """Read example.txt and return as grid."""
    file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]


def test_count_accessible_example():
    """Test that count_accessible returns 13 for example.txt"""
    grid = read_example()
    result = count_accessible(grid)
    assert result == 13, f"Expected 13, got {result}"
    print("test_count_accessible_example PASSED")


def test_count_adjacent_rolls_corner():
    """Test count_adjacent_rolls at corner (0,0) - should only check 3 neighbors"""
    grid = read_example()
    # At (0,0), neighbors are positions 6, 8, 9 only
    # Grid row 0: ..@@.@@@@.
    # Grid row 1: @@@.@.@.@@
    # Position (0,0) = '.', neighbors: (0,1)='.', (1,0)='@', (1,1)='@'
    result = count_adjacent_rolls(grid, 0, 0)
    assert result == 2, f"Expected 2 adjacent rolls at (0,0), got {result}"
    print("test_count_adjacent_rolls_corner PASSED")


def test_count_adjacent_rolls_middle():
    """Test count_adjacent_rolls in middle of grid"""
    grid = read_example()
    # Pick a cell in the middle and manually verify
    # Let's check (5, 5) which should have 8 neighbors
    result = count_adjacent_rolls(grid, 5, 5)
    # Grid around (5,5):
    # Row 4: @@.@@@@.@@  -> (4,4)=@, (4,5)=@, (4,6)=@
    # Row 5: .@@@@@@@.@  -> (5,4)=@, (5,5)=@, (5,6)=@
    # Row 6: .@.@.@.@@@  -> (6,4)=., (6,5)=@, (6,6)=.
    # Adjacent to (5,5): @,@,@,@,@,.,@,. = 6 rolls
    assert result == 6, f"Expected 6 adjacent rolls at (5,5), got {result}"
    print("test_count_adjacent_rolls_middle PASSED")


def test_count_accessible_with_iter_remove_example():
    """Test that count_accessible_with_iter_remove returns 43 for example.txt (Part 2)"""
    grid = read_example()
    result = count_accessible_with_iter_remove(grid)
    assert result == 43, f"Expected 43, got {result}"
    print("test_count_accessible_with_iter_remove_example PASSED")


if __name__ == "__main__":
    test_count_accessible_example()
    test_count_adjacent_rolls_corner()
    test_count_adjacent_rolls_middle()
    test_count_accessible_with_iter_remove_example()
    print("\nAll tests PASSED!")

