class Join:
    def __init__(self,dict1:dict,dict2:dict,key1:str,key2:str) -> None:
        self._dict1 = dict1
        self._dict2 = dict2
        self._key1 = key1
        self._key2 = key2
        self._commonIndex()

    def _commonIndex(self)->list:
        self._dict1_index = []
        self._dict2_index = []
        for i1,j1 in enumerate(self._dict1[self._key1]):
            for i2,j2 in enumerate(self._dict2[self._key2]):
                if j1 == j2:
                    self._dict1_index.append(i1)
                    self._dict2_index.append(i2)

    def _showResult(self,joinType:str,dic:dict)->None:
        print(f'    {joinType}\n')
        for index,(key,value) in enumerate(dic.items()):
            print(f'{index:<5}{key:<15}{value}')
        print('\n')

    def innerJoin(self)->None:
        inner_join = dict()
        for i,j in self._dict1.items():
            temp = []
            for k in self._dict1_index:
                temp.append(j[k])
            if i == self._key1:
                inner_join['join_key'] = temp
            else:
                inner_join[i] = temp
                
        for i,j in self._dict2.items():
            temp = []
            if i == self._key2:
                continue
            else:
                for k in self._dict2_index:
                    temp.append(j[k])
                inner_join[i] = temp
        self._showResult("Inner Join",inner_join)

    def leftJoin(self)->None:
        self._left_join = self._dict1.copy()
        for i,j in self._dict2.items():
            if i == self._key2:
                continue
            else:
                self._left_join[i] = ['Null']*len(j)
                p = 0
                for k in range(len(j)):
                    if k in self._dict2_index:
                        self._left_join[i][self._dict1_index[p]] = j[k]
                        p+=1
        self._showResult("Left Join",self._left_join)

    def rightJoin(self)->None:
        self._right_join = self._dict2.copy()
        for i,j in self._dict1.items():
            if i == self._key1:
                continue
            else:
                self._right_join[i] = ['Null']*len(j)
                p = 0
                for k in range(len(j)):
                    if k in self._dict1_index:
                        self._right_join[i][self._dict2_index[p]] = j[k]
                        p+=1
        self._showResult("Right Join",self._right_join)

    def outerJoin(self)->None:
        outer_join = self._left_join.copy()
        outer_join['join_key'] = outer_join[self._key1]
        del outer_join[self._key1]
        outerJoin2 = self._right_join.copy()
        outerJoin2['join_key'] = outerJoin2[self._key2]
        del outerJoin2[self._key2]
        for i,j in outerJoin2.items():
            for k in range(len(j)):
                if k in self._dict1_index:
                    outer_join[i].append(j[k])
        self._showResult('Outer Join',outer_join)
