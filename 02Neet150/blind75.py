"""
This file contains function stubs for the NeetCode 150 coding interview questions set.
Each function is named based on the problem's common English name.
Due to the variety of problems, parameters are chosen to match typical LeetCode function signatures.

At the bottom of the file, there are sample function calls with example data and expected results.
"""

###################
# Arrays & Hashing (9)
###################

def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array.
    """
    pass

def valid_anagram(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s.
    """
    pass

def two_sum(nums, target):
    """
    Given an array of integers (nums) and an integer (target), 
    return indices of the two numbers such that they add up to target.
    
    Example:
    nums = [2, 7, 11, 15], target = 9
    two_sum(nums, target) -> [0, 1]
    because nums[0] + nums[1] = 2 + 7 = 9
    """
    value_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in value_to_index:
            return [value_to_index[complement], index]
        value_to_index[num] = index
    return None

def group_anagrams(strs):
    """
    Given an array of strings strs, group the anagrams together.
    """
    pass

def top_k_frequent(nums, k):
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    """
    pass

def product_of_array_except_self(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    """
    pass

def encode_decode_strings(strs):
    """
    Design an algorithm to encode a list of strings to a string and decode it back to the list.
    """
    pass

def longest_consecutive(nums):
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive sequence.
    """
    pass

def is_valid_sudoku(board):
    """
    Determine if a 9 x 9 Sudoku board is valid.
    """
    pass

###################
# Two Pointers (5)
###################

def is_palindrome(s):
    """
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters.
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
    Find two lines which together with the x-axis forms a container, containing the most water.
    """
    pass

def trap_rain_water(height):
    """
    Given n non-negative integers representing an elevation map, compute how much water it can trap.
    """
    pass

def is_subsequence(s, t):
    """
    Given two strings s and t, return true if s is a subsequence of t.
    """
    pass

###################
# Sliding Window (6)
###################

def max_profit(prices):
    """
    Given an array prices where prices[i] is the price of a stock on day i,
    return the maximum profit you can achieve from a single buy and sell.
    """
    pass

def length_of_longest_substring(s):
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """
    pass

def character_replacement(s, k):
    """
    Given a string s and an integer k, return the length of the longest substring containing
    the same letter you can get after replacing up to k characters.
    """
    pass

def check_inclusion(s1, s2):
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1.
    """
    pass

def min_window(s, t):
    """
    Given two strings s and t, return the minimum window substring of s such that every character in t is included.
    """
    pass

def max_sliding_window(nums, k):
    """
    Given an array nums and an integer k, return the maximum sliding window.
    """
    pass

###################
# Stack (7)
###################

def is_valid_parentheses(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    """
    pass

def daily_temperatures(temperatures):
    """
    Given an array of integers temperatures representing daily temperatures,
    return an array answer such that answer[i] is the number of days you have to wait after day i.
    """
    pass

def eval_rpn(tokens):
    """
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    """
    pass

def generate_parenthesis(n):
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    """
    pass

class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    """
    def __init__(self):
        pass
    
    def push(self, val):
        pass
    
    def pop(self):
        pass
    
    def top(self):
        pass
    
    def getMin(self):
        pass

def largest_rectangle_area(heights):
    """
    Given an array of integers heights representing the histogram's bar height,
    return the area of the largest rectangle in the histogram.
    """
    pass

def car_fleet(target, position, speed):
    """
    There are n cars going to the same destination. Determine how many car fleets will arrive at the destination.
    """
    pass

###################
# Binary Search (7)
###################

def search(nums, target):
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target,
    write a function to search target in nums. Return the index if target exists, otherwise return -1.
    """
    pass

def search_matrix(matrix, target):
    """
    Write an efficient algorithm that searches for a value target in an m x n integer matrix.
    """
    pass

def min_eating_speed(piles, h):
    """
    Koko loves to eat bananas. Return the minimum integer k such that she can eat all bananas within h hours.
    """
    pass

def find_min(nums):
    """
    Suppose an array of length n sorted in ascending order is rotated. Return the minimum element.
    """
    pass

def search_rotated(nums, target):
    """
    Given the array nums after rotation and an integer target, return the index of target if it is in nums.
    """
    pass

class TimeMap:
    """
    Design a time-based key-value data structure that can store multiple values for the same key.
    """
    def __init__(self):
        pass
    
    def set(self, key, value, timestamp):
        pass
    
    def get(self, key, timestamp):
        pass

def find_median_sorted_arrays(nums1, nums2):
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.
    """
    pass

###################
# Linked List (11)
###################

def reverse_list(head):
    """
    Reverse a singly linked list.
    """
    pass

def merge_two_lists(l1, l2):
    """
    Merge two sorted linked lists and return it as a sorted list.
    """
    pass

def has_cycle(head):
    """
    Given head, return true if the linked list has a cycle in it.
    """
    pass

def reorder_list(head):
    """
    Reorder the list to be on the following form: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
    """
    pass

def remove_nth_from_end(head, n):
    """
    Given a linked list, remove the nth node from the end of list and return its head.
    """
    pass

def copy_random_list(head):
    """
    A linked list of length n is given such that each node contains an additional random pointer.
    Return a deep copy of the list.
    """
    pass

def add_two_numbers(l1, l2):
    """
    Given two non-empty linked lists representing two non-negative integers,
    add the two numbers and return the sum as a linked list.
    """
    pass

def detect_cycle(head):
    """
    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
    """
    pass

def find_duplicate(nums):
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n],
    return the duplicate number.
    """
    pass

class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    """
    def __init__(self, capacity):
        pass
    
    def get(self, key):
        pass
    
    def put(self, key, value):
        pass

def merge_k_lists(lists):
    """
    Merge k sorted linked lists and return it as one sorted list.
    """
    pass

def reverse_k_group(head, k):
    """
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    """
    pass

###################
# Trees (15)
###################

def invert_tree(root):
    """
    Invert a binary tree.
    """
    pass

def max_depth(root):
    """
    Given the root of a binary tree, return its maximum depth.
    """
    pass

def diameter_of_binary_tree(root):
    """
    Given the root of a binary tree, return the length of the diameter of the tree.
    """
    pass

def is_balanced(root):
    """
    Given a binary tree, determine if it is height-balanced.
    """
    pass

def is_same_tree(p, q):
    """
    Given the roots of two binary trees p and q, determine if they are the same.
    """
    pass

def is_subtree(root, subRoot):
    """
    Given the roots of two binary trees root and subRoot, return true if subRoot is a subtree of root.
    """
    pass

def lowest_common_ancestor(root, p, q):
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes.
    """
    pass

def level_order(root):
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    """
    pass

def right_side_view(root):
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.
    """
    pass

def good_nodes(root):
    """
    Given a binary tree root, a node X in the tree is named good if in the path from root to X
    there are no nodes with a value greater than X. Return the number of good nodes.
    """
    pass

def is_valid_bst(root):
    """
    Given the root of a binary tree, determine if it is a valid binary search tree.
    """
    pass

def kth_smallest(root, k):
    """
    Given the root of a binary search tree, and an integer k, return the kth smallest value in the BST.
    """
    pass

def build_tree(preorder, inorder):
    """
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
    and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    """
    pass

def max_path_sum(root):
    """
    Given the root of a binary tree, return the maximum path sum of any non-empty path.
    """
    pass

class Codec:
    """
    Design an algorithm to serialize and deserialize a binary tree.
    """
    def serialize(self, root):
        pass
    
    def deserialize(self, data):
        pass

###################
# Tries (3)
###################

class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """
    def __init__(self):
        pass
    
    def insert(self, word):
        pass
    
    def search(self, word):
        pass
    
    def startsWith(self, prefix):
        pass

class WordDictionary:
    """
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
    """
    def __init__(self):
        pass
    
    def addWord(self, word):
        pass
    
    def search(self, word):
        pass

def find_words(board, words):
    """
    Given an m x n board of characters and a list of strings words, return all words on the board.
    """
    pass

###################
# Heap / Priority Queue (7)
###################

class KthLargest:
    """
    Design a class to find the kth largest element in a stream.
    """
    def __init__(self, k, nums):
        pass
    
    def add(self, val):
        pass

def last_stone_weight(stones):
    """
    We have a collection of stones. Each time we choose the two heaviest stones and smash them together.
    Return the weight of the last remaining stone.
    """
    pass

def k_closest(points, k):
    """
    Given an array of points and an integer k, return the k closest points to the origin (0, 0).
    """
    pass

def find_kth_largest(nums, k):
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.
    """
    pass

def least_interval(tasks, n):
    """
    Given a characters array tasks, representing the tasks a CPU needs to do, and a positive integer n,
    return the least number of units of times that the CPU will take to finish all the given tasks.
    """
    pass

class Twitter:
    """
    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
    and see the 10 most recent tweets in the user's news feed.
    """
    def __init__(self):
        pass
    
    def postTweet(self, userId, tweetId):
        pass
    
    def getNewsFeed(self, userId):
        pass
    
    def follow(self, followerId, followeeId):
        pass
    
    def unfollow(self, followerId, followeeId):
        pass

class MedianFinder:
    """
    The median is the middle value in an ordered integer list. Design a data structure that supports
    the following two operations: void addNum(int num) and double findMedian()
    """
    def __init__(self):
        pass
    
    def addNum(self, num):
        pass
    
    def findMedian(self):
        pass

###################
# Backtracking (9)
###################

def subsets(nums):
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    """
    pass

def combination_sum(candidates, target):
    """
    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen numbers sum to target.
    """
    pass

def permute(nums):
    """
    Given an array nums of distinct integers, return all the possible permutations.
    """
    pass

def subsets_with_dup(nums):
    """
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
    """
    pass

def combination_sum2(candidates, target):
    """
    Given a collection of candidate numbers (candidates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sum to target.
    """
    pass

def exist(board, word):
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    """
    pass

def partition(s):
    """
    Given a string s, partition s such that every substring of the partition is a palindrome.
    Return all possible palindrome partitioning of s.
    """
    pass

def letter_combinations(digits):
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations.
    """
    pass

def solve_n_queens(n):
    """
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
    no two queens attack each other. Return all distinct solutions to the n-queens puzzle.
    """
    pass

###################
# Graphs (13)
###################

def num_islands(grid):
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.
    """
    pass

def clone_graph(node):
    """
    Given a reference of a node in a connected undirected graph, return a deep copy of the graph.
    """
    pass

def max_area_of_island(grid):
    """
    You are given an m x n binary matrix grid. Return the maximum area of an island in grid.
    """
    pass

def pacific_atlantic(heights):
    """
    Given an m x n integer matrix heights representing the height of each unit cell,
    return a list of coordinates where water can flow to both the Pacific and Atlantic oceans.
    """
    pass

def solve_surrounded_regions(board):
    """
    Given an m x n matrix board containing 'X' and 'O', capture all regions that are surrounded.
    """
    pass

def oranges_rotting(grid):
    """
    You are given an m x n grid where each cell can have one of three values representing rotting time.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    """
    pass

def walls_and_gates(rooms):
    """
    You are given an m x n grid rooms. Fill each empty room with the distance to its nearest gate.
    """
    pass

def can_finish(numCourses, prerequisites):
    """
    There are a total of numCourses courses you have to take. Some courses have prerequisites.
    Return true if you can finish all courses.
    """
    pass

def find_order(numCourses, prerequisites):
    """
    There are a total of numCourses courses you have to take. Return the ordering of courses you should take.
    """
    pass

def find_redundant_connection(edges):
    """
    A tree is an undirected graph in which any two vertices are connected by exactly one path.
    Return an edge that can be removed so that the resulting graph is a tree.
    """
    pass

def count_components(n, edges):
    """
    You have a graph of n nodes labeled from 0 to n - 1. Return the number of connected components.
    """
    pass

def valid_tree(n, edges):
    """
    Given n nodes labeled from 0 to n-1 and a list of edges, check if these edges make up a valid tree.
    """
    pass

def ladder_length(beginWord, endWord, wordList):
    """
    A transformation sequence from beginWord to endWord is valid if only one letter can be changed at a time.
    Return the number of words in the shortest transformation sequence from beginWord to endWord.
    """
    pass

###################
# Advanced Graphs (6)
###################

def find_itinerary(tickets):
    """
    You are given a list of airline tickets. Find the itinerary in order that uses all the tickets once.
    """
    pass

def min_cost_connect_points(points):
    """
    Return the minimum cost to make all points connected. All points are connected if there is exactly
    one simple path between any two points.
    """
    pass

def network_delay_time(times, n, k):
    """
    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times.
    Return the minimum time it takes for all the n nodes to receive the signal.
    """
    pass

def swim_in_water(grid):
    """
    You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation.
    Return the least time until you can reach the bottom right square.
    """
    pass

def alien_order(words):
    """
    There is a new alien language that uses the English alphabet. However, the order among letters is unknown.
    Return a string of the unique letters in the new alien language sorted in lexicographically increasing order.
    """
    pass

def find_cheapest_price(n, flights, src, dst, k):
    """
    There are n cities connected by some number of flights. Find the cheapest price from src to dst
    with at most k stops.
    """
    pass

###################
# 1-D Dynamic Programming (12)
###################

def climb_stairs(n):
    """
    You are climbing a staircase. It takes n steps to reach the top. Each time you can climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
    """
    pass

def rob(nums):
    """
    You are a robber planning to rob houses along a street. Each house has some amount of money.
    If you rob two adjacent houses, the security system is triggered.
    Return the maximum amount you can rob without triggering the system.
    """
    pass

def rob_circular(nums):
    """
    Similar to House Robber, but houses are arranged in a circle.
    """
    pass

def longest_palindrome(s):
    """
    Given a string s, return the longest palindromic substring in s.
    """
    pass

def count_substrings(s):
    """
    Given a string s, return the number of palindromic substrings in it.
    """
    pass

def num_decodings(s):
    """
    Given a string s containing only digits, return the number of ways to decode it.
    """
    pass

def coin_change(coins, amount):
    """
    Given an array of coins and a value amount, return the fewest number of coins that make up that amount.
    """
    pass

def max_product(nums):
    """
    Given an integer array nums, find the contiguous subarray within an array which has the largest product.
    """
    pass

def word_break(s, wordDict):
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented
    into a space-separated sequence of one or more dictionary words.
    """
    pass

def length_of_lis(nums):
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.
    """
    pass

def can_partition(nums):
    """
    Given a non-empty array nums containing only positive integers, find if the array can be partitioned
    into two subsets such that the sum of elements in both subsets is equal.
    """
    pass

def unique_paths(m, n):
    """
    A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right.
    Return the number of unique paths to get to the bottom-right corner.
    """
    pass

###################
# 2-D Dynamic Programming (8)
###################

def unique_paths_with_obstacles(obstacleGrid):
    """
    A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right.
    Some obstacles are added to the grid. Return the number of unique paths.
    """
    pass

def longest_common_subsequence(text1, text2):
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    """
    pass

def max_profit_with_cooldown(prices):
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You may complete as many transactions as you like but must cooldown one day between transactions.
    """
    pass

def change(amount, coins):
    """
    You are given an integer array coins representing coins of different denominations and an integer amount.
    Return the number of combinations that make up that amount.
    """
    pass

def find_target_sum_ways(nums, target):
    """
    You are given an integer array nums and an integer target. Build an expression out of nums by adding
    one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    Return the number of different expressions that you can build.
    """
    pass

def is_interleave(s1, s2, s3):
    """
    Given strings s1, s2, and s3, determine whether s3 is formed by an interleaving of s1 and s2.
    """
    pass

def longest_increasing_path(matrix):
    """
    Given an m x n integers matrix, return the length of the longest increasing path in matrix.
    """
    pass

def num_distinct(s, t):
    """
    Given two strings s and t, return the number of distinct subsequences of s which equals t.
    """
    pass

def min_distance(word1, word2):
    """
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    """
    pass

def max_coins(nums):
    """
    You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number.
    Return the maximum coins you can collect by bursting the balloons.
    """
    pass

def is_match(s, p):
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
    """
    pass

###################
# Greedy (8)
###################

def max_subarray(nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum.
    """
    pass

def can_jump(nums):
    """
    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Determine if you are able to reach the last index.
    """
    pass

def jump(nums):
    """
    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Return the minimum number of jumps to reach the last index.
    """
    pass

def can_complete_circuit(gas, cost):
    """
    There are n gas stations along a circular route. Return the starting gas station's index if you can
    travel around the circuit once in the clockwise direction, otherwise return -1.
    """
    pass

def is_n_straight_hand(hand, groupSize):
    """
    Given an integer array hand representing cards and an integer groupSize,
    return true if she can rearrange the cards, or false otherwise.
    """
    pass

def merge_triplets(triplets, target):
    """
    You are given a 2D integer array triplets and an integer array target. Return true if it is possible
    to obtain target as a merge of some triplets, or false otherwise.
    """
    pass

def partition_labels(s):
    """
    You are given a string s. Partition the string into as many parts as possible so that each letter
    appears in at most one part, and return a list of integers representing the size of these parts.
    """
    pass

def check_valid_string(s):
    """
    Given a string s containing only three types of characters: '(', ')' and '*',
    return true if s is valid.
    """
    pass

###################
# Intervals (6)
###################

def insert_interval(intervals, newInterval):
    """
    Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
    """
    pass

def merge_intervals(intervals):
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals.
    """
    pass

def erase_overlap_intervals(intervals):
    """
    Given an array of intervals, find the minimum number of intervals you need to remove
    to make the rest of the intervals non-overlapping.
    """
    pass

def can_attend_meetings(intervals):
    """
    Given an array of meeting time intervals, determine if a person can attend all meetings.
    """
    pass

def min_meeting_rooms(intervals):
    """
    Given an array of meeting time intervals, find the minimum number of conference rooms required.
    """
    pass

def min_interval_to_include_query(intervals, queries):
    """
    You are given a 2D integer array intervals and an integer array queries.
    Return an array containing the answers to the queries.
    """
    pass

###################
# Math & Geometry (8)
###################

def rotate_image(matrix):
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    """
    pass

def spiral_order(matrix):
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
    """
    pass

def set_zeroes(matrix):
    """
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    """
    pass

def is_happy(n):
    """
    Write an algorithm to determine if a number n is happy.
    """
    pass

def plus_one(digits):
    """
    You are given a large integer represented as an integer array digits. Increment it and return the resulting array.
    """
    pass

def my_pow(x, n):
    """
    Implement pow(x, n), which calculates x raised to the power n.
    """
    pass

def multiply(num1, num2):
    """
    Given two non-negative integers num1 and num2 represented as strings,
    return the product of num1 and num2, also represented as a string.
    """
    pass

class DetectSquares:
    """
    You are given a stream of points on the X-Y plane. Design an algorithm that:
    Adds new points to the data structure.
    Counts the number of ways to form axis-aligned squares with point p as one of the vertices.
    """
    def __init__(self):
        pass
    
    def add(self, point):
        pass
    
    def count(self, point):
        pass

###################
# Bit Manipulation (4)
###################

def single_number(nums):
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    """
    pass

def hamming_weight(n):
    """
    Write a function that takes an unsigned integer and returns the number of '1' bits it has.
    """
    pass

def count_bits(n):
    """
    Given an integer n, return an array ans of length n+1 such that ans[i] is the number of 1's
    in the binary representation of i.
    """
    pass

def reverse_bits(n):
    """
    Reverse bits of a given 32 bits unsigned integer.
    """
    pass

def missing_number(nums):
    """
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    """
    pass

def get_sum(a, b):
    """
    Given two integers a and b, return the sum of the two integers without using the operators + and -.
    """
    pass

###################
# Example Calls
###################

if __name__ == "__main__":
    # Arrays & Hashing
    print(contains_duplicate([1,2,3,1]), "problem01")
    print(valid_anagram("anagram", "nagaram"), "problem02")
    print(two_sum([2,7,11,15], 9), "problem03")  # [0, 1]
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]), "problem04")
    print(top_k_frequent([1,1,1,2,2,3], 2), "problem05")  # [1, 2]
    
    # Two Pointers
    print(is_palindrome("A man, a plan, a canal: Panama"), "problem10")
    print(three_sum([-1,0,1,2,-1,-4]), "problem11")  # [[-1,-1,2],[-1,0,1]]
    print(container_with_most_water([1,8,6,2,5,4,8,3,7]), "problem12")  # 49
    
    # Sliding Window
    print(max_profit([7,1,5,3,6,4]), "problem15")  # 5
    print(length_of_longest_substring("abcabcbb"), "problem16")  # 3
    
    # Stack
    print(is_valid_parentheses("()[]{}"), "problem21")
    print(daily_temperatures([73,74,75,71,69,72,76,73]), "problem22")  # [1,1,4,2,1,1,0,0]
    
    # Binary Search
    print(search([-1,0,3,5,9,12], 9), "problem28")  # 4
    print(find_min([3,4,5,1,2]), "problem31")  # 1
    
    # Linked List (many require linked list setup)
    print(has_cycle(None), "problem37")  # False
    
    # Trees (many require tree node setup)
    print(max_depth(None), "problem48")  # 0
    
    # Dynamic Programming
    print(climb_stairs(3), "problem100")  # 3
    print(rob([1,2,3,1]), "problem101")  # 4
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]), "problem123")  # 6
    
    # Greedy
    print(can_jump([2,3,1,1,4]), "problem124")  # True
    
    # Intervals
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]), "problem132")  # [[1,6],[8,10],[15,18]]
    
    # Math & Geometry
    print(plus_one([1,2,3]), "problem141")  # [1,2,4]
    
    # Bit Manipulation
    print(single_number([2,2,1]), "problem145")  # 1
    print(hamming_weight(0b00000000000000000000000000001011), "problem146")  # 3

