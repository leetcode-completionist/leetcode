# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_losses = defaultdict(int)
        
        for match in matches:
          winner = match[0]
          loser = match[1]
          
          player_losses[winner] = player_losses[winner]
          player_losses[loser] += 1
          
        res = [[], []]
        
        for player, losses in player_losses.items():
          if losses == 0:
            res[0].append(player)
          elif losses == 1:
            res[1].append(player)
          
        res[0].sort()
        res[1].sort()
          
        return res
