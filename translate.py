import json
import behaviorTreeType
import parseBehaviorTree

def initializeChildNode():
    initialString = ""
    initialString += "class ChildNode:\n"
    initialString += "\tdef __init__(self, composite, task, decorator):\n"
    initialString += "\t\tself.composite = composite\n"
    initialString += "\t\tself.task = task\n"
    initialString += "\t\tself.decorator = decorator\n\n"
    return initialString

def initializeCompositeNode():
    initialString = ""
    initialString += "class CompositeNode:\n"
    initialString += "\tdef __init__(self, func, children):\n"
    initialString += "\t\tself.func = func\n"
    initialString += "\t\tself.children = children\n"
    initialString += "\t\tself.exePending = []\n\n"
    initialString += "\tdef Run(self):\n"
    initialString += "\t\tif len(self.exePending) == 0:\n"
    initialString += "\t\t\tself.exePending = self.children.copy()\n"
    initialString += "\t\tresult, isRunning = self.func(self.exePending)\n"
    initialString += "\t\tif not isRunning:\n"
    initialString += "\t\t\tself.exePending.clear()\n"
    initialString += "\t\treturn result, isRunning\n\n"
    return initialString

def initializeTaskNode():
    initialString = ""
    initialString += "class TaskNode:\n"
    initialString += "\tdef __init__(self, func):\n"
    initialString += "\t\tself.func = func\n\n"
    initialString += "\tdef Run(self):\n"
    initialString += "\t\tresult, isRunning = self.func(self.exePending)\n"
    initialString += "\t\treturn result, isRunning\n\n"
    return initialString

def initializeNodeClass():
    initialString = ""
    initialString += initializeChildNode()
    initialString += initializeCompositeNode()
    initialString += initializeTaskNode()
    return initialString

def initialize(file, blackboard: behaviorTreeType.Blackboard):
    initialString = "import ue\n\n"
    initialString += initializeNodeClass()
    initialString += "class MyBehaviorTree:\n"
    initialString += "\tdef __init__(self, robot):\n"
    initialString += "\t\tself.root = None\n"
    initialString += "\t\tself.robot = robot\n"
    initialString += "\t\tself.servicesList = []\n"
    initialString += "\t\tself.blackboard = {}\n"
    initialString += blackboard.initialize()
    file.write(initialString)


def CreateNode(node, createNodeString, file):
    header = "\tdef Create(self):\n" + createNodeString
    header += "\t\tself.root = CompositeNode(self." + node._name + ", children_0)\n"
    file.write(header + "\n\n")
    

def translateNodeFunction(node, file, num):
    if node is None:
        return None
    # children node
    no = num
    num += 1
    createNodeString = ""
    if node._children is not None:
        createNodeString += "\t\tchildren_" + str(no) + " = []\n"
        for child in node._children:
            # task node
            if child._childTask is not None:
                transString = child._childTask.translate()
                file.write(transString)
                createNodeString += "\t\ttask_" + str(no) + " = TaskNode(self." + child._childTask._name + ")\n"
            else:
                createNodeString += "\t\ttask_" + str(no) + " = None\n"
            # decorator node
            if child._decorators is not None:
                createNodeString += "\t\tdecorators_" + str(no) + " = []\n"
                for decorator in child._decorators:
                    transString = decorator.translate()
                    file.write(transString)
                    createNodeString += "\t\tdecorators_" + str(no) + ".append(self." +decorator._name + ")\n"
            else:
                createNodeString += "\t\tdecorators_" + str(no) + " = None\n"
            # composite node
            if child._childComposite is not None:
                appnedString, childNo = translateNodeFunction(child._childComposite, file, num)
                createNodeString += appnedString
                createNodeString += "\t\tcomposite_" + str(no) + " = CompositeNode(self." + child._childComposite._name + \
                                ", children_" + str(childNo) + ")\n"
            else:
                createNodeString += "\t\tcomposite_" + str(no) + " = None\n"
            createNodeString += "\t\tchildNode_" + str(no) + " = ChildNode(composite_"\
                             + str(no) + ", task_" + str(no) + ", decorators_" + str(no) + ")\n"
            createNodeString += "\t\tchildren_" + str(no) + ".append(" + "childNode_" + str(no) + ")\n"
    # service node
    if node._services is not None:
        for service in node._services:
            transString = service.translate()
            file.write(transString)

    # node self
    transString = node.translate()
    file.write(transString)
    return createNodeString, no


def translateBTBegin(file):
    file.write("\tdef Run(self):\n")


def translateRoot(compositeNode, file):
    transString = "\t\tself.root.Run()"
    file.write(transString)


def translateBehaviorTree(behaviorTree: behaviorTreeType.BehaviorTree):
    file = open("myPyBehaviorTree.py", "w")
    initialize(file, behaviorTree._blackboard)
    createNodeString, _ = translateNodeFunction(behaviorTree._root, file, 0)
    CreateNode(behaviorTree._root, createNodeString, file)
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
