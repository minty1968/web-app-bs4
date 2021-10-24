import os, random

class Lottery(object):
    def get_sorted_main_numbers(max_main, balls):
        random_nums = random.sample(range(1, max_main), balls)
        sorted_random_main = sorted(random_nums)
        return sorted_random_main

    def get_sorted_bonus_numbers(max_bonus, balls):
        random_nums = random.sample(range(1, max_bonus), balls)
        sorted_random_bonus = sorted(random_nums)
        return sorted_random_bonus

    def get_tot_main_numbers(main):
        tot_num = 0
        for num in main:
            tot_num = tot_num + num
        return tot_num

    def get_tot_bonus_numbers(bonus):
        tot_num = 0
        for num in bonus:
            tot_num = tot_num + num
        return tot_num

    def get_avg_main_numbers(tot_main_num, balls):
        avg_main_nums = tot_main_num / balls
        avg_main_nums = round(avg_main_nums, 1)
        return avg_main_nums

    def get_avg_bonus_numbers(tot_bonus_num, balls):
        avg_bonus_nums = tot_bonus_num / balls
        avg_bonus_nums = round(avg_bonus_nums, 1)
        return avg_bonus_nums
