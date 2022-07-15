import json
import behaviorTreeType
import parseBehaviorTree

def translateBTBegin(file):
    file.write("while True:\n")

def translateNodeFunction(node, file):
    if node == None:
        return None
    # children node
    if node._children != None:
        for child in node._children:
            # task node
            if child._childTask != None:
                transString = child._childTask.translate()
                file.write(transString)
            # decorator node
            if child._decorators != None:
                for decorator in child._decorators:
                    transString = decorator.translate()
                    file.write(transString)
            # composite node
            if child._childComposite != None:
                translateNodeFunction(child._childComposite, file)
                transString = child._childComposite.translate()
                file.write(transString)

    # service node
    if node._services != None:
        for service in node._services:
            transString = service.translate()
            file.write(transString)
        

def translateRoot(compositeNode, file):
    transString = "\t" + compositeNode._name + "()"

def translateBehaviorTree(behaviorTree):
    file = open("generated.py", "w")
    translateBTBegin(file)
    translateNodeFunction(file)
    translateRoot(behaviorTree._root, file)
    file.close()

if __name__ == "__main__":
    BTAsset = open("temp.json", "r", encoding="utf-8")
    bt = json.load(BTAsset)
    # first parse last construct
    # parse behaviorTree
    btName = bt["Name"]
    btBlackboard = bt["Blackboard"]
    btRoot = bt["Root"]
    keys = []
    for entry in btBlackboard["Keys"]:
        if entry["Type"] == "Object" or entry["Type"] == "Class":
            insertEntry = behaviorTreeType.BlackboardGeneratedKey(
                entry["Name"], entry["Type"], entry["BaseClass"])
        else:
            insertEntry = behaviorTreeType.BlackboardKey(
                entry["Name"], entry["Type"])
        keys.append(insertEntry)
    newBlackboard = behaviorTreeType.Blackboard(keys)
    newComposite = parseBehaviorTree.parseCompositeNode(btRoot)
    pyBT = behaviorTreeType.BehaviorTree(btName, newBlackboard, newComposite)
    translateBehaviorTree(pyBT)
