__author__ = 'Brian Rieder'

# Difficulty: Easy with Easy/Intermediate Extension

# (Easy): Flood-Fill
# Challenge Input:
#
# You will accept two numbers, w and h, separated by a space. These are to be the width and height of the image in
# characters, with the top-left being (0, 0). You will then accept a grid of ASCII characters of size w*h. Finally
# you will accept two more numbers, x and y, and a character c. x and y are the co-ordinates on the image where the
# flood fill should be done, and c is the character that will be filled.
# Pixels are defined as contigious (touching) when they share at least one edge (pixels that only touch at corners
# aren't contigious).
# For example:
# 37 22
# .....................................
# ...#######################...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#######.....
# ...###.................##......#.....
# ...#..##.............##........#.....
# ...#....##.........##..........#.....
# ...#......##.....##............#.....
# ...#........#####..............#.....
# ...#........#..................#.....
# ...#.......##..................#.....
# ...#.....##....................#.....
# ...#...##......................#.....
# ...#############################.....
# .....................................
# .....................................
# .....................................
# .....................................
# 8 12 @
#
# Challenge Output
# Output the image given, after the specified flood-fill has taken place.
# .....................................
# ...#######################...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#...........
# ...#.....................#######.....
# ...###.................##......#.....
# ...#@@##.............##........#.....
# ...#@@@@##.........##..........#.....
# ...#@@@@@@##.....##............#.....
# ...#@@@@@@@@#####..............#.....
# ...#@@@@@@@@#..................#.....
# ...#@@@@@@@##..................#.....
# ...#@@@@@##....................#.....
# ...#@@@##......................#.....
# ...#############################.....
# .....................................
# .....................................
# .....................................
# .....................................
#
# Extension (Easy/Intermediate)
#
# Extend your program so that the image 'wraps' around from the bottom to the top, and from the left to the right
# (and vice versa). This makes it so that the top and bottom, and left and right edges of the image are touching
# (like the surface map of a torus).


def recursive_fill_without_wrap(current_x, current_y):
    # Note: fill_char and char_to_change are defined in global scope
    if grid[current_y][current_x] is not char_to_change:
        return
    else:
        grid[current_y][current_x] = fill_char
    recursive_fill_without_wrap(current_x - 1, current_y)
    recursive_fill_without_wrap(current_x + 1, current_y)
    recursive_fill_without_wrap(current_x, current_y - 1)
    recursive_fill_without_wrap(current_x, current_y + 1)


def iterative_fill_without_wrap(x_coord, y_coord):
    stack = [(x_coord, y_coord)]
    while True:
        check_x, check_y = stack.pop()
        if grid[check_y][check_x] is char_to_change:
            grid[check_y][check_x] = fill_char
            stack.append((check_x - 1, check_y))
            stack.append((check_x + 1, check_y))
            stack.append((check_x, check_y - 1))
            stack.append((check_x, check_y + 1))
        if not stack:  # Check for empty stack
            break


def iterative_fill_with_wrap(x_coord, y_coord):
    stack = [(x_coord, y_coord)]
    while True:
        check_x, check_y = stack.pop()
        if grid[check_y][check_x] is char_to_change:
            grid[check_y][check_x] = fill_char
            if check_x > 0:
                stack.append((check_x - 1, check_y))
            else:
                stack.append((width - 1, check_y))
            stack.append(((check_x + 1) % width, check_y))
            if check_y > 0:
                stack.append((check_x, check_y - 1))
            else:
                stack.append((check_x, height - 1))
            stack.append((check_x, (check_y + 1) % height))
        if not stack:  # Check for empty stack
            break


def recursive_fill_with_wrap(current_x, current_y):
    # Note: fill_char and char_to_change are defined in global scope
    if grid[current_y][current_x] is not char_to_change:
        return
    else:
        grid[current_y][current_x] = fill_char
    # X backward
    if current_x > 0:
        recursive_fill_with_wrap(current_x - 1, current_y)
    else:
        recursive_fill_with_wrap(width - 1, current_y)
    # X forward
    recursive_fill_with_wrap((current_x + 1) % width, current_y)
    # Y backward
    if current_y > 0:
        recursive_fill_with_wrap(current_x, current_y - 1)
    else:
        recursive_fill_with_wrap(current_x, height - 1)
    # Y forward
    recursive_fill_with_wrap(current_x, (current_y + 1) % height)


def print_grid():
    for sub_grid in grid:
        print("".join(sub_grid), end="")
    print("\n\n")


if __name__ == "__main__":
    wrap_flag = input("Wrap text or no? (Default: N) Y/N: ")
    wrap_flag = (wrap_flag == "Y")
    print("Wrap Mode = " + str(wrap_flag))
    recur_flag = input("Iterative or Recursive? (Default: I) I/R: ")
    recur_flag = (recur_flag == "R")
    print("Recursive Mode = " + str(recur_flag))
    width, height = [int(x) for x in input("Enter width and height of graph (space separated): ").split(" ")]
    filename = input("Enter the grid input file (e.g., grid16x15_22@.txt): ")
    if filename == "":
        print("Defaulting to grid16x15_22@.txt...")
        filename = "grid16x15_22@.txt"
    grid_file = open(filename)
    grid = []
    for _ in range(0, height):
        grid.append(list(grid_file.readline()))
    start_x, start_y, fill_char = input("Enter the start index and fill character (space separated): ").split(" ")
    start_y, start_x = int(start_y), int(start_x)
    char_to_change = grid[start_y][start_x]
    print_grid()
    if wrap_flag and recur_flag:
        recursive_fill_with_wrap(start_x, start_y)
    elif recur_flag and not wrap_flag:
        recursive_fill_without_wrap(start_x, start_y)
    elif wrap_flag and not recur_flag:
        iterative_fill_with_wrap(start_x, start_y)
    else:
        iterative_fill_without_wrap(start_x, start_y)
    print_grid()
