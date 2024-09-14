# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            
            if rank[root_x] == rank[root_y]:
                root[root_y] = root_x
                rank[root_x] += 1
            elif rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            else:
                root[root_x] = root_y
        
        N = len(accounts)
        root = [i for i in range(N)]
        rank = [1 for _ in range(N)]
        
        email_idx = collections.defaultdict(int)
        
    
        for idx, acc in enumerate(accounts):    
            for email in acc[1:]:
                if email not in email_idx:
                    email_idx[email] = idx
                else:
                    union(email_idx[email], idx)
        
        group_ids_to_accounts = collections.defaultdict(list) 
        for email in email_idx:
            # email_idx[email] = find(email_idx[email])
            # idx = email_idx[email]
            
            # The find function will fix the group id and return it
            group_id = find(email_idx[email])            
            group_ids_to_accounts[group_id].append(email) 
        
        res = []
        for group_id in group_ids_to_accounts:
            accts_in_same_group = sorted(group_ids_to_accounts[group_id])
            
            temp = [accounts[group_id][0]]
            temp.extend(accts_in_same_group) 
            
            res.append(temp)
        
        return res