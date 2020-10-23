class TrieNode:
    def __init__(self):
        self.data = {} #数据以字典形式存放
        self.is_word = False   #是否是一个完整单词
    def __repr__(self):
        return str(self.data)
class Trie:
    def __init__(self):
        self.root = TrieNode()  #插入结点时从根节点开始,根节点是一个空字典
    def insert(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char) # child = node.data[char] 获取char(键)对应的值
            #(两者区别:如果不存在,get的方法结果为None,布尔值为False,而对应下键取值,不存在会报错)
            if child is None: #如果值是空的,建立新字典,新的字典,值为空字典
                node.data[char] = TrieNode()
            node = node.data[char] #结点下移
        node.is_word = True #单词每个字符全部插入的结束标志

    def search(self,word): #查找单词是否存在
        node = self.root
        for char in word:
            node = node.data[char]
            if not node: #如果为空
                return False
        return node.is_word #判断结点是否完整的存在trie中,存在返回True,否则False

    def startWith(self,prefix):#查找前缀prefix是否存在
        node = self.root
        for char in prefix:
            node = node.data[char]
            if not node:
                return False
        return True #只要prefix存在,即可认为是正确的,不需要判断是否是一个完整单词






if __name__ == '__main__':
   t = Trie()
   t.insert('something')
   t.insert('some')
   t.insert('someone')
   print(t.root)
   print(t.search('some'))
   print(t.startWith('some'))

