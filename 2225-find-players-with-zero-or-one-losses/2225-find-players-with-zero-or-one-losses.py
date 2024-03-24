from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = defaultdict(int)
        losers = defaultdict(int)
        result = []

        for match in matches:
            
            winners[match[1]] = -1

            losers[match[1]] += 1

            if match[0] in winners and winners[match[0]] == -1:
                continue
            
            else:
                winners[match[0]] = 1

        losers_list = []
        for key in losers:
            if losers[key] == 1:
                losers_list.append(key)
        
        winners_list = []

        # Get the winners list
        for key in winners:
            if winners[key] == 1:
                winners_list.append(key)
        
        winners_list.sort()
        losers_list.sort()
        result.append(winners_list)
        result.append(losers_list)

        return result
