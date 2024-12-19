class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.dic_tables = {}
        for name in names:
            self.dic_tables[name] = {}
        
        for i, name in enumerate(names):
            table = self.dic_tables[name]
            list_ = [""] * columns[i]
            table[1] = list_

        self.dic_ids = {}
        for name in names:
            self.dic_ids[name] = 1

    def insertRow(self, name: str, row: List[str]) -> None:
        table = self.dic_tables[name]
        new_id = self.dic_ids[name]
        for i, r in enumerate(row):
            table[new_id][i] = r
        new_id += 1
        self.dic_ids[name] = new_id
        table[new_id] = [""] * len(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        table = self.dic_tables[name]
        del table[rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        table = self.dic_tables[name]
        return table[rowId][columnId - 1]

# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)