import threading
import ue

serviceList = []

Blackboard = {}
Blackboard["SelfActor"] = None
Blackboard["Print"] = False

def printFirst_C_0():
	print("First print String")

def BTDecorator_Blackboard_1():
	if not Blackboard["Print"]:
		return True
	return False

def printSecond_C_0():
	print("Second print String!!!!!!!!!")

def BTDecorator_Blackboard_2():
	if Blackboard["Print"]:
		return True
	return False

def BTComposite_Selector_0():
	if BTDecorator_Blackboard_1():
		if printFirst_C_0():
			return True
	if BTDecorator_Blackboard_2():
		if printSecond_C_0():
			return True
		return False


def BTComposite_Selector_0():
	if BTDecorator_Blackboard_1():
		if printFirst_C_0():
			return True
	if BTDecorator_Blackboard_2():
		if printSecond_C_0():
			return True
		return False


def changeBlackboard_C_0():
	Blackboard["Print"] = not Blackboard["Print"]

def BTComposite_Sequence_0():
	if BTComposite_Selector_0() is False:
		return False
	if changeBlackboard_C_0() is False:
		return False
	return True


def RunPyBehaviorTree():
	BTComposite_Sequence_0()