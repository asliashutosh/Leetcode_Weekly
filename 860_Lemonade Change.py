# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        count_of_fives = 0
        count_of_tens = 0
        count_of_twenty = 0

        for price in bills:
            if price == 5:
                count_of_fives += 1

            elif price == 10:
                # Now check if you have change
                if count_of_fives > 0:
                    count_of_fives -= 1
                    count_of_tens += 1
                    
                else:
                    return False

            elif price == 20:

                if count_of_tens>0:
                    count_of_tens -= 1

                    if count_of_fives>0:
                        count_of_fives -= 1
                        count_of_twenty += 1

                    else:
                        return False

                elif count_of_fives>=3:
                    count_of_fives -= 3
                    count_of_twenty += 1

                else:
                    return False

        return True