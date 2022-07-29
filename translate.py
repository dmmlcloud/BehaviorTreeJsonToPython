import json
import behaviorTreeType
import parseBehaviorTree


def initialize(file, blackboard: behaviorTreeType.Blackboard):
    initialString = "import ue\n\n"
    initialString += "class MyBehaviorTree:\n"
    initialString += "\tdef __init__(self, robot):\n"
    initialString += "\t\tself.robot = robot\n"
    initialString += "\t\tself.servicesList = []\n"
    initialString += "\t\tself.blackboard = {}\n"
    initialString += blackboard.initialize()
    file.write(initialString)


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
                # transString = child._childComposite.translate()
                # file.write(transString)

    # service node
    if node._services is not None:
        for service in node._services:
            transString = service.translate()
            file.write(transString)

    # node self
    transString = node.translate()
    file.write(transString)


def translateBTBegin(file):
    file.write("\tdef Run(self):\n")


def translateRoot(compositeNode, file):
    transString = "\t\tself." + compositeNode._name + "()"
    file.write(transString)


def translateBehaviorTree(behaviorTree: behaviorTreeType.BehaviorTree):
    file = open("myPyBehaviorTree.py", "w")
    initialize(file, behaviorTree._blackboard)
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
    newBlackboard = parseBehaviorTree.parseBlackboard(btBlackboard)
    newComposite = parseBehaviorTree.parseCompositeNode(btRoot, newBlackboard)
    pyBT = behaviorTreeType.BehaviorTree(btName, newBlackboard, newComposite)
    translateBehaviorTree(pyBT)
