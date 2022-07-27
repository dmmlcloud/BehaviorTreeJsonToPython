import json
import behaviorTreeType
import parseBehaviorTree


def initialize(file):
    initialString = "import threading\n"
    initialString += "import ue\n"
    initialString += "serviceList = []\n\n"
    file.write(initialString)


def translateBlackboard(blackboard, file):
    file.write(blackboard.translate())


def translateNodeFunction(node, file):
    if node is None:
        return None
    # children node
    if node._children is not None:
        for child in node._children:
            # task node
            if child._childTask is not None:
                transString = child._childTask.translate()
                file.write(transString)
            # decorator node
            if child._decorators is not None:
                for decorator in child._decorators:
                    transString = decorator.translate()
                    file.write(transString)
            # composite node
            if child._childComposite is not None:
                translateNodeFunction(child._childComposite, file)
                transString = child._childComposite.translate()
                file.write(transString)

    # service node
    if node._services is not None:
        for service in node._services:
            transString = service.translate()
            file.write(transString)


def translateBTBegin(file):
    file.write("def RunPyBehaviorTree:\n")


def translateRoot(compositeNode, file):
    transString = "\t" + compositeNode._name + "()"
    file.write(transString)


def translateBehaviorTree(behaviorTree):
    file = open("myPyBehaviorTree.py", "w")
    initialize(file)
    translateBlackboard(behaviorTree._blackboard, file)
    translateNodeFunction(behaviorTree._root, file)
    translateBTBegin(file)
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
