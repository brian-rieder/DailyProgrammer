__author__ = 'Brian Rieder'

# Link to reddit: https://www.reddit.com/r/dailyprogrammer/comments/2sfs8f/20150114_challenge_197_intermediate_food_delivery/
# Credit to: /u/Gronner for help in Python implementation of Dijkstra's algorithm.

# Difficulty: Intermediate

# Description:
# You are owner of a new restaurant that is open 24 hours a day 7 days a week. To be helpful to your customers
# you deliver. To make sure you are the best in business you offer a guarantee of the fastest delivery of food
# during your hours of operation (which is all the time)
# Our challenge this week is to build a program our delivery people can use to help pick the fastest route in
# time to get from a source to a destination in the town of our restaurant.
# City Routes
# The city has many streets connected to many intersections. For the sake of naming we will label intersections
# with letters. Streets between intersections will use their street name.
# Time Intervals
# The data for each street has 4 values of time in minutes. They represent the time it takes one to travel that
# street based on a fixed interval of time of day to travel on that street. The varied time is due to different
# traffic loads on that street.
# T1 = 0600-1000 (6 am to 10 am)
# T2 = 1000 - 1500 (10 am to 3 pm)
# T3 = 1500 - 1900 (3 pm to 7 pm)
# T4 = 1900 - 0600 (7 pm to 6 am)
# Data Format
# (Start Intersection) (Stop Intersection) (Name of street) (T1) (T2) (T3) (T4)
# (Start Intersection) - The letter of that unique intersection
# (Stop Intersection) - The letter of that unique intersection
# (Name of Street) - Name of the street with this time data
#  (T1 to T4) are the minutes it takes to travel based on fixed time intervals (described above)

# Data

# The data:
#  A B "South Acorn Drive" 5 10 5 10
#  B C "Acorn Drive" 15 5 15 5
#  C D "North Acorn Drive" 7 10 15 7
#  H G "South Almond Way" 10 10 10 10
#  G F "Almond Way" 15 20 15 20
#  F E "North Almond Way" 5 6 5 6
#  I J "South Peanut Lane" 8 9 10 11
#  J K "Peanut Lane" 11 10 9 8
#  K L "North Peanut Lane" 7 5 7 5
#  P O "South Walnut" 6 5 6 5
#  O N "Walnut" 10 8 10 8
#  N M "North Walnut" 9 6 9 6
#  D E "West Elm Street" 10 8 12 7
#  E L "Elm Street" 12 11 12 8
#  L M "East Elm Street" 5 4 5 4
#  C F "West Central Avenue" 9 8 9 8
#  F K "Central Avenue" 5 4 5 4
#  K N "East Central Avenue" 9 9 9 9
#  B G "West Pine Road" 7 6 7 6
#  G J "Pine Road" 9 8 9 8
#  J O "East Pine Road" 6 5 6 5
#  A H "West Oak Expressway" 9 8 7 7
#  H I "Oak Expressway" 10 10 10 10
#  I P "East Oak Expressway" 8 7 8 7
# Time Changes and Routes
# It is possible that a route might take you long enough that it might cross you over a time change such that the
# route times get change. To make this easier just please consider the time between intersections based on the start
# time of the drive. So say I pick 5:50am - and if the route would take us into 6am hour you don't have to compute
# the route times for 6am to 10am but just keep the route computed based on 7pm to 6am since our starting time was
# 5:50am.

# Challenge Input:
# You will be given start and end intersections and time of day to compute a route.
# Challenge Output:
# List the route direction street by street and time. This must be the "Fastest" route from start to end at that
# time of day. Also list the time it took you in minutes.

# Challenge Routes to solve:
# A M 0800
# A M 1200
# A M 1800
# A M 2200
#
#
# P D 0800
# P D 1200
# P D 1800
# P D 2200


def dijkstra_algorithm(graph, orig_start, start, end, time_setting, visited_list, distances, prev):
    # Base Case: Last node is reached
    if start == end:
        # Begin constructing the path we used to get there
        path = []
        # Start from the back and build forward
        itr_prev = end
        # Iterate and append until we've gone back home
        while itr_prev is not None:
            if itr_prev != orig_start:
                # Append the previous location
                path.append(graph[prev.get(itr_prev, orig_start)][itr_prev][1])
            # Set iterative previous to value preceding itself
            itr_prev = prev.get(itr_prev)
        # Print results:
        print("\nPath: " + str(path))
        print("Time: " + str(distances[end]) + "minutes")
        return None
    # Recursive Case: Finding shortest path
    if not visited_list:
        distances[start] = 0
    for next_loc in graph[start]:
        if next_loc not in visited_list:
            temp_dist = distances[start] + graph[start][next_loc][0][time_setting]
            if temp_dist < distances.get(next_loc, float('inf')):
                distances[next_loc] = temp_dist
                prev[next_loc] = start
    visited_list.append(start)
    unvisited = {}
    for i in graph:
        if i not in visited_list:
            unvisited[i] = distances.get(i, float('inf'))
    new_start = min(unvisited, key = unvisited.get)
    dijkstra_algorithm(graph, orig_start, new_start, end, time_setting, visited_list, distances, prev)



A_B = [[5, 10, 5, 10], "South Acorn Drive"]
B_C = [[15, 5, 15, 5], "Acorn Drive"]
C_D = [[7, 10, 15, 7], "North Acorn Drive"]
H_G = [[10, 10, 10, 10], "South Almond Way"]
G_F = [[15, 20, 15, 20], "Almond Way"]
F_E = [[5, 6, 5, 6], "North Almond Way"]
I_J = [[8, 9, 10, 11], "South Peanut Lane"]
J_K = [[11, 10, 9, 8], "Peanut Lane"]
K_L = [[7, 5, 7, 5], "North Peanut Lane"]
P_O = [[6, 5, 6, 5], "South Walnut"]
O_N = [[10, 8, 10, 8], "Walnut"]
N_M = [[9, 6, 9, 6], "North Walnut"]
D_E = [[10, 8, 12, 7], "West Elm Street"]
E_L = [[12, 11, 12, 8], "Elm Street"]
L_M = [[5, 4, 5, 4], "Elm Street"]
C_F = [[9, 8, 9, 8], "West Central Avenue"]
F_K = [[5, 4, 5, 4], "Central Avenue"]
K_N = [[9, 9, 9, 9], "East Central Avenue"]
B_G = [[7, 6, 7, 6], "West Pine Road"]
G_J = [[9, 8, 9, 8], "Pine Road"]
J_O = [[6, 5, 6, 5], "East Pine Road"]
A_H = [[9, 8, 7, 7], "West Oak Expressway"]
H_I = [[10, 10, 10, 10], "Oak Expressway"]
I_P = [[8, 7, 8, 7], "East Oak Expressway"]

street_map = {"A": {"B": A_B, "H": A_H},
              "B": {"A": A_B, "C": B_C, "G": B_G},
              "C": {"B": B_C, "D": C_D, "F": C_F},
              "D": {"C": C_D, "E": D_E},
              "E": {"D": D_E, "F": F_E, "L": E_L},
              "F": {"C": C_F, "E": F_E, "G": G_F, "K": F_K},
              "G": {"B": B_G, "F": G_F, "H": H_G, "J": G_J},
              "H": {"A": A_H, "G": H_G, "I": H_I},
              "I": {"H": H_I, "J": I_J, "P": I_P},
              "J": {"G": G_J, "I": I_J, "K": J_K, "O": J_O},
              "K": {"F": F_K, "J": J_K, "L": K_L, "N": K_N},
              "L": {"E": E_L, "K": K_L, "M": L_M},
              "M": {"L": L_M, "N": N_M},
              "N": {"K": K_N, "M": N_M, "O": O_N},
              "O": {"J": J_O, "N": O_N, "P": P_O},
              "P": {"I": I_P, "O": P_O}}


if __name__ == "__main__":
    user_input = input("Enter start vertex, end vertex, and time separated by a space: ").split(" ")
    if user_input[1] not in street_map or user_input[1] not in street_map:
        raise TypeError("Address not in map.")
    if 600 <= int(user_input[2]) < 1000:  # case for T1
        time_set = 1
    elif 1000 <= int(user_input[2]) < 1500:  # case for T2
        time_set = 2
    elif 1500 <= int(user_input[2]) < 1900:  # case for T3
        time_set = 3
    elif 1900 <= int(user_input[2]) < 2399 or int(user_input[2]) < 600:  # case for T4
        time_set = 4
    else:  # Invalid time
        raise TypeError("Please enter a valid time.")
    visited = []
    distance = {}
    prev_nodes = {}
    dijkstra_algorithm(street_map, user_input[0], user_input[0], user_input[1], time_set, visited, distance, prev_nodes)
