__author__ = 'Brian Rieder'

# Difficulty: Intermediate

# Link: http://www.reddit.com/r/dailyprogrammer/comments/2uo3yf/20150204_challenge_200_intermediate_metro_tile/

# In the continued name of backward-compatibility, Microsoft has released a version of their flagship operating
# system for VGA text-mode terminals. In this version of their operating system, rectangular tiles consisting of a
# single character are displayed on the screen, like so:
# ..........................................................................
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# ................................bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# ...................cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.............................jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
# .eeeeeeeeee...............................................................
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# ..........................................................................
# Screen space with no tile is denoted by a period (.). Tiles can be made of any character other than periods (due to
# the reason given) and spaces.
# However, the dev team forgot to add support for screen-readers! Now visually impaired users cannot determine the
# location of the tiles on their display. Your task is, given a tile display such as the one above, write a program to
# find the location and size of each rectangular tile on the screen, along with the character in it, and output it in
# a way that can be read by a screen reader. For example, one such tile in the above example is located at position
# (1, 1) on the screen (from the top-left), consists of the character a and is 30 characters wide and 8 characters tall.
# Tiles
#
# A tile will always be perfectly rectangular:
# aaaaaaaaaa
# aaaaaaaaaa
# aaaaaaaaaa
# There will never be a non-rectangular tile on the screen, or one that is not completely filled in. These are not
# single tiles:
# ..................................
# .bbbbbbbbbb.........ccccccccccccc.
# .bbbbbbbbb..........c...........c.
# .bbbbbbbb...........c...........c.
# .bbbbbbb............ccccccccccccc.
# ..................................
# A tile is something completely bordered by empty space (.), so this is two separate tiles:
# .....................................
# .aaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaa.
# .aaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaa.
# .aaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaa.
# .aaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaa.
# .....................................
# Lastly, if a tile is made of two regions of separate colours, then they are separate tiles:
# .....................................
# .aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb.
# .aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb.
# .aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb.
# .aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb.
# .....................................
# The above 'tile' is two separate tiles: one made of a, one made of b.
# Handling of invalid input is undefined and thus mostly up to you; your program can try and make sense of the input
# if you want, but for the purpose of the challenge, assume all tiles will be rectangular, separated by empty space (.)
# and consisting of a single character.

# Input and Output Description
#
# Sample Input
#
# You will first be given two numbers, like so:
# 74 30
# These denote the width and height of the tile display in characters. You will then be given the tile display of that
# size via standard input, for example:
# ..........................................................................
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
# ...........................................bbbbbbbb.ddddddddddddddddddddd.
# .jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
# .jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
# .jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
# .jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
# .jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.......................
# .jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
# .jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
# ...........................eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
# .iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
# .iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee................................
# .iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii................................fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
# .iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
# ..........................................................................
# Sample Output
#
# You are to print the location (with (0, 0) being the top-left), width, height and filled character of each tile on
# the screen, like this:
# 41×6 tile of character 'a' located at (1,1)
# 8×16 tile of character 'b' located at (43,1)
# 21×4 tile of character 'c' located at (52,13)
# 21×11 tile of character 'd' located at (52,1)
# 15×14 tile of character 'e' located at (27,8)
# 15×11 tile of character 'f' located at (43,18)
# 14×11 tile of character 'g' located at (59,18)
# 30×6 tile of character 'h' located at (12,23)
# 10×13 tile of character 'i' located at (1,16)
# 25×7 tile of character 'j' located at (1,8)
# 14×6 tile of character 'k' located at (12,16)
# Sample Inputs and Outputs
#
# Input
#
# 4 4
# xx.z
# xx..
# ..yy
# z.yy
# Output
#
# 2×2 tile of character 'x' located at (0,0)
# 1×1 tile of character 'z' located at (0,3)
# 2×2 tile of character 'y' located at (2,2)
# 1×1 tile of character 'z' located at (3,0)
# Input
#
# 10 10
# ..........
# .@@@@@.ss.
# .@@@@@.ss.
# .......ss.
# .\\\\\.ss.
# .\\\\\....
# .\\\\\.\\.
# .......\\.
# ./////.\\.
# ..........
# Output
#
# 5×2 tile of character '@' located at (1,1)
# 5×3 tile of character '\' located at (1,4)
# 5×1 tile of character '/' located at (1,8)
# 2×4 tile of character 's' located at (7,1)
# 2×3 tile of character '\' located at (7,6)
# Input
#
# 74 30
# ..........................................................................
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# ................................bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# ...................cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.............................jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
# .eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
# .eeeeeeeeee...............................................................
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# .eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
# ..........................................................................
# Output
#
# 30×8 tile of character 'a' located at (1,1)
# 17×3 tile of character 'd' located at (1,10)
# 10×15 tile of character 'e' located at (1,14)
# 6×7 tile of character 'f' located at (12,14)
# 38×7 tile of character 'g' located at (12,22)
# 12×11 tile of character 'c' located at (19,10)
# 10×16 tile of character 'b' located at (32,1)
# 27×3 tile of character 'h' located at (32,18)
# 16×16 tile of character 'k' located at (43,1)
# 22×7 tile of character 'i' located at (51,22)
# 13×20 tile of character 'j' located at (60,1)


def cleanup(orig_x, orig_y, curr_x, curr_y, x_dim, y_dim):
    if curr_x - orig_x == x_dim:
        return
    if curr_y - orig_y == y_dim:
        return
    tiles[curr_y][curr_x] = '.'
    cleanup(orig_x, orig_y, curr_x + 1, curr_y, x_dim, y_dim)
    cleanup(orig_x, orig_y, curr_x, curr_y + 1, x_dim, y_dim)


def define_block(test_x, test_y):
    orig_x, orig_y = test_x, test_y
    char_to_check = tiles[test_y][test_x]
    x_dim, y_dim = 0, 1
    while test_x < width and tiles[test_y][test_x] is char_to_check:
        x_dim += 1
        tiles[test_y][test_x] = '.'
        test_x += 1
    test_x -= 1
    test_y += 1
    while test_y < height and tiles[test_y][test_x] is char_to_check:
        y_dim += 1
        tiles[test_y][test_x] = '.'
        test_y += 1
    cleanup(orig_x, orig_y, orig_x, orig_y, x_dim, y_dim)
    print(str(x_dim) + "x" + str(y_dim) + " tile of character '"
          + char_to_check + "' located at (" + str(orig_x) + "," + str(orig_y) + ")")


def find_characters():
    for curr_y in range(0, height):
        for curr_x in range(0, width):
            if tiles[curr_y][curr_x] is not '.':
                define_block(curr_x, curr_y)


if __name__ == "__main__":
    filename = input("Enter name of file to analyze: ")
    tile_file = open(filename)
    width, height = [int(x) for x in tile_file.readline().split(" ")]
    tiles = []
    for i in range(0, height):
        tiles.append(list(tile_file.readline()))
        tiles[i].pop()
    find_characters()
