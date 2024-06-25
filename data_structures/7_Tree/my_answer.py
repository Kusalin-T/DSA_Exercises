class TreeNode:
    def __init__(self, data) -> None:
        self.data=data
        self.children=[]
        self.parent=None

    def add(self, child):
        child.parent=self
        self.children.append(child)

    def getlvl(self):
        count=0
        itr=self.parent
        while itr:
            count+=1
            itr=itr.parent
        return count    

    def printme(self):
        prefix='   '*self.getlvl() + ('|__' if self.getlvl()!=0 else '')
        print(prefix + self.data)
        for child in self.children:
            child.printme()

aaa=TreeNode('AAA')

bbb=TreeNode('bbb')
bbb.add(TreeNode('bb1'))
bbb.add(TreeNode('bb2'))
bbb.add(TreeNode('bb3'))

ccc=TreeNode('ccc')
ccc.add(TreeNode('cc1'))
ccc.add(TreeNode('cc2'))

aaa.add(bbb)
aaa.add(ccc)
aaa.printme()

class CompanyNode(TreeNode):
    def __init__(self, name, title):
        self.name=name
        self.title=title
        self.children=[]
        self.parent=None

    def printme(self, command):
        prefix = '   '*self.getlvl() + ('|__' if self.getlvl()!=0 else '')
        if command=='name':
            print(prefix+self.name)
        elif command=='designation':
            print(prefix+self.title)
        else:
            print(prefix+f'{self.name} ({self.title})')   
        for child in self.children:
            child.printme(command)         

print('\n'*3)
company = CompanyNode('Nilupul', 'CEO')

cto = CompanyNode('Chainmay', "CTO")
cto.add(CompanyNode('Hola', "Dev"))
cto.add(CompanyNode('Hoho', "Cleaner"))

hrhead = CompanyNode('SomeoneHR', "HRHEAD")
hrhead.add(CompanyNode('Max','Recruiter'))
hrhead.add(CompanyNode('Bobby','Lawyer'))
hrhead.add(CompanyNode('Johnson','Intern'))
company.add(cto)
company.add(hrhead)
company.printme("name") # prints only name hierarchy
company.printme("designation") # prints only designation hierarchy
company.printme("both") # prints both (name and designation) 

class LevelNode(TreeNode):
    def printme(self, level):
        if level<self.getlvl():
            return
        prefix='   '*self.getlvl() + ('|__' if self.getlvl()!=0 else '')
        print(prefix + self.data)
        for child in self.children:
            child.printme(level)

levle = LevelNode('top loc')
br1 = LevelNode('left')
br11= LevelNode('ddep')
br11.add(LevelNode('deep'))
br1.add(br11)
br1.add(LevelNode('not dep'))
br2 = LevelNode('right')     
br2.add(LevelNode('shallow'))
br2.add(LevelNode('supa shy'))       
levle.add(br1)
levle.add(br2)
levle.printme(0)
levle.printme(1)
levle.printme(2)
levle.printme(3)