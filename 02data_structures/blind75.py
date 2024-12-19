"""
This file contains function stubs for the Blind 75 coding interview questions set.
Each function is named based on the problem's common English name.
Due to the variety of problems, parameters are chosen to match typical LeetCode function signatures.

At the bottom of the file, there are sample function calls with example data and expected results.
"""

###################
# Array (10)
###################

def two_sum(nums, target):
    """
    Given an array of integers and a target integer, return indices of the 
    two numbers such that they add up to target.
    """
    pass

def best_time_to_buy_and_sell_stock(prices):
    """
    Given an array prices where prices[i] is the price of a given stock on the i-th day,
    return the maximum profit you can achieve by buying and selling one share of stock.
    """
    pass

def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array.
    """
    pass

def product_of_array_except_self(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    """
    pass

def maximum_subarray(nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum.
    """
    pass

def maximum_product_subarray(nums):
    """
    Given an integer array nums, find the contiguous subarray within an array
    (containing at least one number) which has the largest product.
    """
    pass

def find_minimum_in_rotated_sorted_array(nums):
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    Return the minimum element of the rotated array.
    """
    pass

def search_in_rotated_sorted_array(nums, target):
    """
    Given the array nums after rotation and an integer target, return the index of target if it is in nums,
    or -1 if it is not in nums.
    """
    pass

def three_sum(nums):
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    """
    pass

def container_with_most_water(height):
    """
    Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
    n vertical lines are drawn. Find two lines which together with the x-axis forms a container,
    such that the container contains the most water.
    """
    pass

###################
# Binary (5)
###################

def sum_of_two_integers(a, b):
    """
    Given two integers a and b, return the sum of the two integers without using the operators + and -.
    """
    pass

def number_of_1_bits(n):
    """
    Write a function that takes an unsigned integer and returns the number of '1' bits it has.
    """
    pass

def counting_bits(n):
    """
    Given an integer n, return an array ans of length n+1 such that ans[i] is the number 
    of 1-bits of i.
    """
    pass

def missing_number(nums):
    """
    Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.
    """
    pass

def reverse_bits(n):
    """
    Reverse bits of a given 32 bits unsigned integer.
    """
    pass

###################
# Dynamic Programming (11)
###################

def climbing_stairs(n):
    """
    You are climbing a staircase. It takes n steps to reach the top. 
    Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    pass

def coin_change(coins, amount):
    """
    Given an array of coins and a value amount, return the fewest number of coins that make up that amount.
    If that amount cannot be made up by any combination of the coins, return -1.
    """
    pass

def longest_increasing_subsequence(nums):
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.
    """
    pass

def longest_common_subsequence(text1, text2):
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    """
    pass

def word_break(s, wordDict):
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
    into a space-separated sequence of one or more dictionary words.
    """
    pass

def combination_sum(candidates, target):
    """
    Given an array of distinct integers and a target integer, return a list of all unique combinations 
    of candidates where the chosen numbers sum to target.
    """
    pass

def house_robber(nums):
    """
    You are a robber planning to rob houses along a street. Each house has some amount of money.
    If you rob two adjacent houses, the security system is triggered. 
    Return the maximum amount you can rob without triggering the system.
    """
    pass

def house_robber_ii(nums):
    """
    Similar to House Robber, but houses are arranged in a circle.
    """
    pass

def decode_ways(s):
    """
    Given a string s containing only digits, return the number of ways to decode it.
    """
    pass

def unique_paths(m, n):
    """
    A robot is located at the top-left corner of a m x n grid. 
    The robot can only move either down or right at any point in time.
    Return the number of unique paths to get to the bottom-right corner.
    """
    pass

def jump_game(nums):
    """
    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Determine if you are able to reach the last index.
    """
    pass

###################
# Graph (7)
###################

def clone_graph(node):
    """
    Given a reference of a node in a connected undirected graph, return a deep copy of the graph.
    """
    pass

def course_schedule(numCourses, prerequisites):
    """
    There are a total of numCourses you have to take. Some courses have prerequisites.
    Return true if you can finish all courses.
    """
    pass

def pacific_atlantic_water_flow(heights):
    """
    Given an m x n matrix of non-negative integers representing the height of each unit cell,
    find all coordinates from which water can flow to both the Pacific and Atlantic ocean.
    """
    pass

def number_of_islands(grid):
    """
    Given an m x n 2D binary grid of '1's and '0's, return the number of distinct islands.
    """
    pass

def word_ladder(beginWord, endWord, wordList):
    """
    Given two words (beginWord and endWord), and a dictionary wordList, 
    return the length of the shortest transformation sequence from beginWord to endWord.
    """
    pass

def alien_dictionary(words):
    """
    Given a list of words sorted lexicographically, return the order of letters in the alien language.
    """
    pass

def graph_valid_tree(n, edges):
    """
    Given n nodes labeled from 0 to n-1 and a list of edges, 
    check if these edges make up a valid tree.
    """
    pass

###################
# Interval (5)
###################

def insert_interval(intervals, newInterval):
    """
    Given a set of non-overlapping intervals, insert a new interval into the intervals 
    (merge if necessary).
    """
    pass

def merge_intervals(intervals):
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], 
    merge all overlapping intervals.
    """
    pass

def non_overlapping_intervals(intervals):
    """
    Given an array of intervals, find the minimum number of intervals you need to remove 
    to make the rest of the intervals non-overlapping.
    """
    pass

def meeting_rooms(intervals):
    """
    Given an array of meeting time intervals, determine if a person can attend all meetings.
    """
    pass

def meeting_rooms_ii(intervals):
    """
    Given an array of meeting time intervals, find the minimum number of conference rooms required.
    """
    pass

###################
# Linked List (7)
###################

def reverse_linked_list(head):
    """
    Reverse a singly linked list.
    """
    pass

def linked_list_cycle(head):
    """
    Given head, return true if the linked list has a cycle in it.
    """
    pass

def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists and return it as a sorted list.
    """
    pass

def merge_k_sorted_lists(lists):
    """
    Merge k sorted linked lists and return it as one sorted list.
    """
    pass

def remove_nth_node_from_end_of_list(head, n):
    """
    Given a linked list, remove the n-th node from the end of list and return its head.
    """
    pass

def reorder_list(head):
    """
    Reorder a linked list.
    """
    pass

def lru_cache_operations(operations, capacities):
    """
    Simulate LRU cache operations.
    """
    pass

###################
# Matrix (4)
###################

def set_matrix_zeroes(matrix):
    """
    Given an m x n matrix, if an element is 0, set its entire row and column to 0.
    """
    pass

def spiral_matrix(matrix):
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
    """
    pass

def rotate_image(matrix):
    """
    Rotate an n x n matrix by 90 degrees (clockwise).
    """
    pass

def word_search(board, word):
    """
    Given an m x n board and a word, return true if the word exists in the grid.
    """
    pass

###################
# String (6)
###################

def longest_substring_without_repeating_characters(s):
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """
    pass

def longest_repeating_character_replacement(s, k):
    """
    Given a string s and an integer k, return the length of the longest substring 
    that contains the same letter you can get after replacing up to k characters.
    """
    pass

def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring in s.
    """
    pass

def palindromic_substrings(s):
    """
    Given a string s, return the number of palindromic substrings in it.
    """
    pass

def encode_and_decode_strings(strs):
    """
    Encode a list of strings to a single string, and decode it back to a list of strings.
    """
    pass

def minimum_window_substring(s, t):
    """
    Given two strings s and t, return the minimum window in s which will contain all the characters in t.
    """
    pass

###################
# Tree (8)
###################

def maximum_depth_of_binary_tree(root):
    """
    Given the root of a binary tree, return its maximum depth.
    """
    pass

def same_tree(p, q):
    """
    Given the roots of two binary trees p and q, determine if they are the same.
    """
    pass

def invert_binary_tree(root):
    """
    Invert a binary tree.
    """
    pass

def binary_tree_level_order_traversal(root):
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    """
    pass

def serialize_and_deserialize_binary_tree(root):
    """
    Serialize and deserialize a binary tree.
    """
    pass

def subtree_of_another_tree(root, subRoot):
    """
    Given the roots of two binary trees root and subRoot, 
    return true if there is a subtree of root that matches subRoot.
    """
    pass

def construct_binary_tree_from_preorder_and_inorder(preorder, inorder):
    """
    Given preorder and inorder traversal of a tree, construct the binary tree.
    """
    pass

def validate_binary_search_tree(root):
    """
    Given the root of a binary tree, determine if it is a valid BST.
    """
    pass

###################
# Heap & Priority Queue (3)
###################

def kth_largest_element_in_a_stream(k, nums, operations):
    """
    Design a class to find the kth largest element in a stream.
    """
    pass

def last_stone_weight(stones):
    """
    Given stones with weights, smash the two heaviest stones and return the weight of the last stone.
    """
    pass

def k_closest_points_to_origin(points, k):
    """
    Given an array of points, return the k closest points to the origin (0,0).
    """
    pass

###################
# Backtracking (4)
###################

def permutations(nums):
    """
    Return all permutations of a given array of distinct integers.
    """
    pass

def combination_sum_ii(candidates, target):
    """
    Given a collection of candidate numbers and a target number,
    find all unique combinations where the numbers sum to target.
    """
    pass

def subsets(nums):
    """
    Return all possible subsets (the power set) of the given integer array.
    """
    pass

def word_search_ii(board, words):
    """
    Given an m x n board of characters and a list of words,
    return all words on the board.
    """
    pass

###################
# Advanced Topics (5)
###################

def implement_trie():
    """
    Implement a Trie with insert, search, and startsWith methods.
    """
    pass

def add_and_search_word():
    """
    Implement a data structure that supports adding new words and searching.
    """
    pass

def find_median_from_data_stream():
    """
    Continuously read integers and return the median of all elements so far.
    """
    pass

def longest_increasing_path_in_a_matrix(matrix):
    """
    Given a matrix, return the length of the longest increasing path.
    """
    pass

def trapping_rain_water(height):
    """
    Given non-negative integers representing elevation map, compute trapped rain water.
    """
    pass

###################
# Example Calls
###################

if __name__ == "__main__":
    # Array
    print(two_sum([2,7,11,15], 9))                    # Expect indices of two numbers that add to 9, e.g. [0,1]
    print(best_time_to_buy_and_sell_stock([7,1,5,3,6,4])) # Expect max profit, e.g. 5
    print(contains_duplicate([1,2,3,1]))              # Expect True
    print(product_of_array_except_self([1,2,3,4]))    # Expect [24,12,8,6]
    print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Expect 6 (subarray [4,-1,2,1])
    print(maximum_product_subarray([2,3,-2,4]))       # Expect 6 (subarray [2,3])
    print(find_minimum_in_rotated_sorted_array([3,4,5,1,2])) # Expect 1
    print(search_in_rotated_sorted_array([4,5,6,7,0,1,2], 0)) # Expect 4
    print(three_sum([-1,0,1,2,-1,-4]))                # Expect [[-1,-1,2],[-1,0,1]]
    print(container_with_most_water([1,8,6,2,5,4,8,3,7]))     # Expect 49
    
    # Binary
    print(sum_of_two_integers(1,2))                   # Expect 3
    print(number_of_1_bits(0b00000000000000000000000000001011)) # Expect 3
    print(counting_bits(5))                           # Expect [0,1,1,2,1,2]
    print(missing_number([3,0,1]))                    # Expect 2
    print(reverse_bits(0b00000010100101000001111010011100)) # Example, expect reversed bits
    
    # Dynamic Programming
    print(climbing_stairs(3))                         # Expect 3 (ways: 1+1+1, 1+2, 2+1)
    print(coin_change([1,2,5], 11))                   # Expect 3 (11 = 5+5+1)
    print(longest_increasing_subsequence([10,9,2,5,3,7,101,18])) # Expect 4 ([2,3,7,101])
    print(longest_common_subsequence("abcde","ace"))  # Expect 3 ("ace")
    print(word_break("leetcode", ["leet","code"]))    # Expect True
    print(combination_sum([2,3,6,7], 7))              # Expect [[2,2,3],[7]]
    print(house_robber([1,2,3,1]))                    # Expect 4 (rob houses 1 and 3)
    print(house_robber_ii([2,3,2]))                   # Expect 3
    print(decode_ways("226"))                         # Expect 3 ("BZ", "VF", "BBF")
    print(unique_paths(3,7))                          # Expect 28
    print(jump_game([2,3,1,1,4]))                     # Expect True
    
    # Graph
    # clone_graph, course_schedule, pacific_atlantic_water_flow, number_of_islands, word_ladder,
    # alien_dictionary, graph_valid_tree would require more complex inputs (nodes/graphs).
    # Here we just show indicative calls (Expect comments are hypothetical, since no implementations):
    print(course_schedule(2, [[1,0]]))               # Expect True
    print(number_of_islands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))                                               # Expect 1
    
    # Interval
    print(insert_interval([[1,3],[6,9]], [2,5]))     # Expect [[1,5],[6,9]]
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]])) # Expect [[1,6],[8,10],[15,18]]
    print(non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]])) # Expect minimum removals
    print(meeting_rooms([[0,30],[5,10],[15,20]]))    # Expect False
    print(meeting_rooms_ii([[0,30],[5,10],[15,20]])) # Expect 2
    
    # Linked List (just showing calls; these need linked list setup)
    print(reverse_linked_list(None))                  # Expect None
    print(linked_list_cycle(None))                    # Expect False
    
    # Matrix
    print(set_matrix_zeroes([[1,1,1],[1,0,1],[1,1,1]])) # Expect modified matrix with zeroes
    print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))     # Expect [1,2,3,6,9,8,7,4,5]
    print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))      # Expect [[7,4,1],[8,5,2],[9,6,3]]
    print(word_search(
        [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']], 
        "ABCCED"))                                    # Expect True
    
    # String
    print(longest_substring_without_repeating_characters("abcabcbb")) # Expect 3
    print(longest_repeating_character_replacement("AABABBA", 1))      # Expect 4
    print(longest_palindromic_substring("babad"))         # Expect "bab" or "aba"
    print(palindromic_substrings("aaa"))                  # Expect 6 (all substrings "a","a","a","aa","aa","aaa")
    print(encode_and_decode_strings(["lint","code","love","you"])) # Expect encoded and decoded back same list
    print(minimum_window_substring("ADOBECODEBANC","ABC"))          # Expect "BANC"
    
    # Tree (just showing calls; these require tree nodes)
    print(maximum_depth_of_binary_tree(None))            # Expect 0
    print(same_tree(None, None))                         # Expect True
    print(invert_binary_tree(None))                      # Expect None
    print(binary_tree_level_order_traversal(None))       # Expect []
    print(subtree_of_another_tree(None, None))           # Expect True
    
    # Heap & Priority Queue
    print(last_stone_weight([2,7,4,1,8,1]))             # Expect 1 (after smashes)
    print(k_closest_points_to_origin([[3,3],[5,-1],[-2,4]], 2)) # Expect [[3,3],[-2,4]]
    
    # Backtracking
    print(permutations([1,2,3]))                         # Expect [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(combination_sum_ii([10,1,2,7,6,1,5], 8))       # Expect combinations that sum to 8
    print(subsets([1,2,3]))                              # Expect [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
    
    # Advanced Topics
    print(longest_increasing_path_in_a_matrix([
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]))                                                  # Expect 4 (path: 1->2->6->9 or similar)
    print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1])) # Expect 6
