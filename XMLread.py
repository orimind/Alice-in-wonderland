import xml.etree.ElementTree as ET

class XMLreader2():
    def __init__(self):
        self.tree = ET.ElementTree(file='ch2.xml')
        self.root = self.tree.getroot()
    #取得順序
    def get_order(self,pyorder):
        for elem in self.tree.iter(tag = "order"): 
            pyorder.append(elem.get('name'))
        return pyorder
    #依順序輸出劇情
    def output(self,pyorder):
        name = []
        dialog = []
        for i in range(len(pyorder)):  
            for order in self.root.findall('order'):      
                if order.get('name') == str(pyorder[i]):
                    name.append(order.find('character').text)
                    dialog.append(order.find('dialog').text)
            i+=1
        return name,dialog

class XMLreader3():
    def __init__(self):
        self.tree = ET.ElementTree(file='ch3.xml')
        self.root = self.tree.getroot()
    #取得順序
    def get_order(self,pyorder):
        for elem in self.tree.iter(tag = "order"): 
            pyorder.append(elem.get('name'))
        return pyorder
    #依順序輸出劇情
    def output(self,pyorder):
        name = []
        dialog = []
        for i in range(len(pyorder)):  
            for order in self.root.findall('order'):      
                if order.get('name') == str(pyorder[i]):
                    name.append(order.find('character').text)
                    dialog.append(order.find('dialog').text)
            i+=1
        return name,dialog