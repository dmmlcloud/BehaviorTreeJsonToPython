import ue


class MyBehaviorTree:
    def __init__(self, robot):
        self.robot = robot
        self.servicesList = []
        self.blackboard = {}
        self.blackboard["SelfActor"] = None
        self.blackboard["Print"] = False

    def printFirst_C_0(self):
        print("First print String")
        return True

    def BTDecorator_Blackboard_1(self):
        if not self.blackboard["Print"]:
            return True
        return False

    def printSecond_C_0(self):
        print("Second print String!!!!!!!!!")
        return True

    def BTDecorator_Blackboard_2(self):
        if self.blackboard["Print"]:
            return True
        return False

    def BTComposite_Selector_0(self):
        if self.BTDecorator_Blackboard_1():
            if self.printFirst_C_0():
                return True
        if self.BTDecorator_Blackboard_2():
            if self.printSecond_C_0():
                return True
        return False

    def changeBlackboard_C_0(self):
        self.blackboard["Print"] = not self.blackboard["Print"]
        return True

    def BTComposite_Sequence_0(self):
        if self.BTComposite_Selector_0() is False:
            return False
        if self.changeBlackboard_C_0() is False:
            return False
        return True

    def Run(self):
        self.BTComposite_Sequence_0()
