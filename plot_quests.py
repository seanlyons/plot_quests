import matplotlib.pyplot as plt
import pdb

color = ['r', 'g', 'b', 'y']
data = {
    'Lord Agrippa': {
        'first': [13, 16, 17, 20, 22, 25, 25, 27, 27, 35, 38, 40, 41, 42, 43, 44, 44, 45, 46, 46, 48, 49, 49, 50, 51, 51, 51, 51, 52, 52, 53, 54, 54, 55, 55, 55, 56, 56, 56, 57, 58, 58, 58, 58, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 65, 65, 65, 67, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 70, 70, 71, 71, 71, 71, 71, 71, 72, 72, 72, 73, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 77, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 86, 87, 87, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 88, 88, 89, 89, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 98, 98, 98, 98, 98, 98, 98, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 100, 100, 100, 100, 100, 100],
        'second': [10, 13, 14, 15, 15, 16, 16, 17, 17, 18, 18, 18, 21, 22, 22, 23, 25, 25, 25, 26, 26, 31, 35, 38, 41, 41, 41, 45, 46, 46, 47, 47, 48, 48, 49, 50, 51, 51, 52, 53, 54, 54, 54, 54, 55, 55, 55, 56, 56, 59, 59, 59, 60, 60, 60, 61, 61, 61, 61, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 65, 65, 66, 66, 66, 67, 67, 68, 68, 68, 68, 68, 69, 69, 69, 70, 70, 70, 71, 72, 72, 72, 72, 72, 72, 73, 73, 74, 74, 74, 74, 74, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 77, 77, 78, 78, 79, 79, 79, 80, 80, 80, 80, 81, 82, 82, 83, 85, 85, 85, 85, 86, 86, 86, 86, 87, 87, 87, 87, 88, 88, 88, 89, 89, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 92, 92, 92, 93, 94, 94, 94, 94, 95, 95, 95, 96, 96, 96, 97, 97, 97, 98, 98, 98, 99, 99, 100],
        'third': [4, 5, 6, 6, 7, 8, 8, 10, 10, 11, 13, 13, 14, 14, 15, 15, 16, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 22, 23, 23, 24, 25, 25, 26, 26, 27, 27, 29, 38, 44, 47, 49, 50, 52, 53, 54, 55, 55, 55, 56, 56, 57, 58, 58, 60, 60, 60, 62, 62, 63, 64, 64, 64, 64, 66, 67, 69, 70, 70, 70, 71, 72, 72, 74, 74, 75, 75, 75, 76, 76, 76, 78, 79, 79, 80, 80, 81, 81, 81, 82, 83, 83, 83, 85, 87, 87, 87, 88, 88, 89, 89, 89, 90, 90, 92, 94, 96],
        'fourth': [3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 20, 21, 21, 21, 21, 21, 22, 22, 22, 23, 23, 24, 24, 24, 25, 25, 25, 25, 26, 27, 27, 28, 29, 29, 30, 30, 31, 31, 31, 33, 40, 40, 40, 41, 41, 43, 43, 43, 45, 45, 46, 46, 46, 47, 49, 50, 51, 51, 51, 52, 52, 53, 53, 55, 56, 56, 56, 56, 58, 60, 60, 60, 60, 60, 60, 62, 62, 62, 62, 63, 64, 64, 64, 64, 64, 66, 69, 71, 71, 72, 81, 81, 81]
    },
    'Lord Vendredi': {
        'first': [4, 6, 8, 9, 12, 24, 29, 35, 47, 47, 47, 48, 48, 51, 52, 52, 53, 53, 53, 54, 56, 56, 59, 61, 62, 63, 63, 63, 64, 64, 65, 65, 66, 66, 66, 66, 67, 67, 67, 68, 68, 68, 68, 68, 68, 69, 69, 69, 69, 70, 70, 70, 70, 70, 71, 71, 71, 72, 72, 72, 73, 73, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 76, 76, 76, 76, 77, 77, 77, 77, 78, 78, 79, 79, 80, 80, 81, 81, 81, 81, 81, 82, 83, 83, 83, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 86, 86, 86, 86, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 89, 89, 89, 89, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 99, 99, 99, 99, 99, 99, 99, 99, 99, 100, 100, 101, 101],
        'second': [2, 4, 4, 5, 7, 7, 8, 9, 10, 10, 11, 16, 18, 20, 20, 23, 23, 24, 28, 28, 28, 33, 45, 47, 47, 48, 48, 49, 50, 50, 51, 52, 54, 54, 55, 56, 56, 58, 58, 59, 59, 59, 59, 60, 61, 62, 63, 63, 63, 64, 64, 65, 65, 66, 66, 66, 66, 66, 67, 67, 67, 67, 68, 68, 68, 69, 69, 69, 70, 70, 70, 70, 70, 71, 71, 71, 72, 72, 73, 73, 73, 74, 74, 76, 76, 77, 77, 77, 77, 79, 79, 79, 80, 80, 81, 82, 82, 82, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 87, 87, 88, 88, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 97, 98, 98, 98, 98, 98, 98, 99, 99, 99, 99, 99, 99, 99, 99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 101, 101, 101],
        'third': [2, 2, 3, 4, 4, 5, 7, 8, 8, 8, 9, 10, 12, 12, 13, 14, 15, 16, 19, 19, 20, 23, 24, 24, 26, 26, 28, 30, 31, 33, 40, 48, 48, 49, 50, 50, 51, 53, 55, 55, 56, 56, 56, 56, 56, 56, 57, 58, 58, 59, 59, 60, 60, 61, 61, 62, 62, 63, 64, 65, 65, 66, 66, 67, 68, 68, 69, 69, 70, 70, 70, 71, 72, 72, 72, 72, 72, 73, 73, 73, 74, 74, 74, 75, 75, 76, 78, 78, 79, 79, 79, 80, 81, 81, 81, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 84, 84, 85, 85, 86, 86, 86, 87, 87, 88, 88, 88, 88, 89, 89, 89, 90, 90, 91, 91, 91, 91, 92, 93, 93, 93, 94, 94, 94, 95, 97, 98, 98, 98, 99, 100, 100, 100, 102],
        'fourth': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 10, 10, 11, 12, 14, 19, 19, 20, 41, 51, 52, 56, 60, 61, 62, 62, 63, 63, 65, 65, 66, 67, 67, 71, 73, 74, 75, 75, 78, 79, 81, 81, 82, 83, 83, 85, 86, 86, 99, 99, 101, 101, 101, 101, 101, 101, 101, 101, 101, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102]
    },
    'Lord Telleri': {
        'first': [13, 34, 34, 38, 38, 48, 50, 50, 52, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 55, 55, 55, 55, 55, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 61, 62, 62, 62, 62, 62, 63, 63, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 68, 69, 69, 69, 69, 69, 69, 69, 70, 70, 71, 71, 71, 71, 71, 71, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 80, 80, 80, 80, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 87, 87, 87, 88, 88, 88, 88, 88, 89, 89, 90, 90, 90, 90, 90, 90, 91, 91, 92, 92, 92, 92, 94, 94],
        'second': [2, 4, 6, 9, 11, 11, 12, 13, 14, 15, 16, 20, 22, 26, 28, 33, 34, 36, 45, 45, 49, 50, 53, 54, 57, 58, 59, 61, 61, 62, 64, 65, 65, 66, 66, 67, 68, 70, 73, 73, 73, 73, 76, 78, 79, 79, 79, 80, 81, 82, 83, 83, 84, 84, 84, 84, 85, 85, 85, 86, 87, 88, 90, 90, 90, 91, 92, 92, 92, 92, 93, 94, 94, 94, 94, 94, 95, 95, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 98, 98, 98, 98, 98],
        'third': [2, 5, 5, 6, 6, 10, 11, 13, 13, 14, 14, 15, 20, 21, 26, 27, 29, 34, 35, 36, 40, 40, 44, 52, 54, 54, 57, 60, 65, 66, 69, 69, 70, 71, 74, 75, 75, 76, 77, 81, 82, 88, 90, 90, 92, 93, 93],
        'fourth': [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 9, 9, 12, 12, 13, 17, 18, 19, 20, 27, 29, 32, 34, 34, 35, 35, 50, 54, 54, 56, 57, 65, 74, 87, 95]
    },
    'Lord Maldra': {
        'second': [13],
        'third': [1, 1, 2, 7, 8, 8, 9, 14, 18, 24, 54, 54, 55, 57, 72, 73, 75, 77, 79, 79, 80, 82, 82, 86, 88, 89, 91, 91, 96, 97, 97, 98, 99, 99, 99, 100, 100, 100, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 102, 102, 102, 102, 102, 102],
        'fourth': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 12, 12, 13, 15, 16, 16, 17, 18, 19, 20, 20, 21, 23, 24, 27, 29, 30, 31, 31, 42, 43, 49, 52, 54, 54, 55, 55, 56, 57, 58, 65, 68, 68, 69, 72, 72, 72, 73, 73, 74, 76, 76, 77, 77, 79, 80, 81, 84, 85, 86, 87, 88, 88, 89, 89, 89, 90, 90, 91, 91, 93, 94, 95, 96, 97, 97, 97, 98, 98, 99, 99, 99, 100, 100, 100, 100, 100, 101, 101, 101, 101, 101, 101, 101, 102, 102, 102]
    },
    'Lord Vashir': {
        'first': [15, 16, 17, 21, 22, 24, 25, 26, 31, 31, 39, 41, 42, 43, 44, 45, 46, 46, 47, 47, 47, 48, 48, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 52, 52, 52, 53, 53, 53, 53, 54, 54, 54, 55, 55, 55, 56, 56, 56, 56, 57, 57, 57, 57, 57, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 65, 65, 65, 66, 67, 67, 67, 67, 68, 68, 70, 70, 70, 70, 72, 73, 76, 77, 80, 80, 81, 82, 82, 83, 83, 84, 84, 89, 93, 93, 95, 97],
        'second': [7, 10, 14, 15, 16, 17, 17, 20, 20, 21, 22, 22, 23, 23, 24, 24, 25, 26, 26, 26, 27, 27, 28, 28, 29, 30, 31, 31, 31, 37, 38, 39, 40, 42, 42, 43, 44, 45, 46, 46, 47, 48, 48, 48, 48, 49, 49, 50, 51, 51, 51, 52, 52, 52, 52, 53, 54, 55, 55, 55, 56, 57, 57, 58, 58, 58, 58, 59, 60, 60, 60, 61, 61, 61, 61, 61, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 64, 64, 64, 65, 65, 65, 66, 66, 66, 66, 67, 67, 67, 67, 68, 68, 69, 69, 70, 70, 70, 70, 70, 71, 71, 71, 72, 73, 73, 73, 73, 74, 75, 76, 76, 77, 77, 77, 78, 79, 80, 80, 80, 80, 81, 81, 82, 82, 82, 83, 83, 84, 84, 84, 87, 87, 88, 89, 89, 91, 92, 93, 93, 95, 95, 97],

        'third': [7, 8, 11, 12, 14, 15, 15, 16, 16, 17, 18, 19, 20, 21, 22, 27, 29, 29, 30, 30, 40, 40, 41, 42, 43, 44, 44, 45, 45, 45, 46, 46, 46, 46, 46, 48, 48, 48, 48, 49, 49, 50, 50, 50, 50, 51, 51, 51, 51, 51, 51, 52, 52, 53, 53, 53, 53, 54, 55, 55, 56, 57, 57, 58, 58, 58, 59, 59, 61, 61, 62, 62, 63, 63, 64, 64, 64, 64, 65, 65, 65, 66, 67, 68, 68, 68, 68, 69, 69, 70, 70, 70, 70, 72, 72, 74, 76, 77, 77, 77, 80, 82, 82, 82, 86, 87, 95, 95],
        'fourth': [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 11, 13, 14, 15, 16, 16, 16, 16, 17, 17, 17, 17, 18, 18, 19, 19, 20, 21, 21, 22, 23, 23, 25, 26, 29, 29, 30, 30, 30, 39, 39, 42, 43, 43, 43, 45, 45, 46, 46, 46, 47, 48, 48, 48, 48, 49, 49, 49, 49, 50, 50, 52, 52, 52, 54, 55, 57, 58, 59, 60, 61, 63, 64, 65, 65, 65, 66, 67, 69, 72, 73, 73, 74, 74, 76, 78, 78, 82, 82, 87, 87, 91, 92, 93, 94]
    },
    'Lady Templeton': {
        'first': [20, 24, 37, 42, 48, 52, 61, 68, 85, 98],
        'second': [2, 2, 2, 4, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9, 10, 10, 13, 13, 14, 14, 14, 16, 16, 18, 18, 22, 23, 23, 24, 26, 26, 28, 28, 29, 30, 30, 36, 37, 39, 40, 42, 42, 43, 44, 45, 45, 46, 47, 47, 48, 48, 48, 48, 50, 50, 50, 51, 52, 52, 52, 52, 53, 55, 57, 58, 58, 59, 59, 60, 60, 61, 62, 62, 62, 62, 63, 63, 65, 65, 66, 66, 66, 67, 68, 68, 68, 69, 69, 69, 71, 71, 71, 71, 71, 72, 73, 73, 76, 76, 76, 78, 78, 78, 80, 80, 81, 81, 81, 81, 82, 82, 83, 83, 83, 84, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 87, 87, 87, 88, 88, 89, 89, 90, 91, 91, 91, 91, 92, 93, 93, 94, 94, 95, 95, 96, 96, 96, 97, 97, 97, 97, 97, 97, 98, 98, 98, 98, 98, 99, 99, 99, 99, 99, 99, 99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 101, 101, 101, 101, 101, 101, 101],
        'third': [2, 3, 5, 5, 6, 6, 9, 9, 9, 18, 22, 23, 26, 26, 29, 30, 36, 38, 43, 44, 47, 48, 52, 52, 52, 55, 57, 57, 58, 59, 62, 62, 69, 71, 71, 72, 72, 77, 78, 79, 80, 85, 87, 88, 90, 96, 97, 99, 100],
        'fourth': [1, 2, 2, 3, 3, 3, 4, 5, 6, 30, 44, 47, 54, 57, 69, 70, 76, 80, 82, 90, 90, 93, 98, 100]
    },
    'Lady Undya': {
        'first': [4, 4, 6, 7, 7, 8, 9, 13, 15, 17, 19, 26, 44, 46, 46, 47, 49, 50, 50, 51, 53, 53, 55, 56, 56, 56, 56, 56, 56, 57, 58, 59, 59, 59, 60, 60, 61, 63, 63, 63, 64, 64, 65, 65, 67, 67, 68, 69, 69, 70, 71, 71, 71, 72, 72, 73, 73, 73, 74, 74, 74, 74, 75, 75, 76, 77, 77, 77, 77, 78, 78, 78, 79, 79, 79, 79, 79, 80, 80, 81, 81, 81, 82, 84, 85, 89],
        'second': [3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10, 11, 11, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 16, 17, 17, 18, 18, 19, 20, 20, 20, 21, 22, 22, 23, 23, 24, 25, 26, 27, 31, 40, 41, 42, 42, 44, 45, 47, 49, 50, 53, 54, 56, 56, 61, 61, 61, 62, 64, 64, 66, 67, 69, 69, 73, 76, 77, 83],
        'third': [3, 6, 7, 8, 8, 9, 9, 11, 12, 13, 13, 15, 20, 23, 23, 23, 23, 24, 27, 28, 30, 39, 40, 42, 43, 44, 45, 45, 52, 52, 53, 54, 56, 67],
        'fourth': [4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 10, 10, 10, 11, 12, 13, 14, 14, 15, 15, 15, 16, 17, 17, 17, 18, 18, 20, 20, 21, 22, 23, 23, 23, 25, 26, 27, 27, 30, 39, 41, 45, 46, 48, 48, 49, 50, 51, 51, 52, 53, 54, 56, 64]
    }
}

    for word in words:
        full_set[lord][class_num].append(int(word))

classes = {'second': 'y', 'third': 'g', 'fourth': 'b'}
for qm in full_set:
    if 'first' in qm:
        points = []
        count = 0
        for datum in full_set[qm]['first']:
            print('plotting for {0}'.format(qm))
            points.append((count, datum))
            plt.plot(points, 'r')
    for class_num in classes:
        count = 0
        points = []
        for datum in full_set[qm][class_num]:
            print('plotting for {0} ({1})'.format(qm, class_num))
            points.append((count, datum))
            plt.plot(points, classes[class_num])
            
    plt.ylabel("{0}".format(lord.replace("-", " ")))
    plt.savefig('{0}.png'.format(lord))
