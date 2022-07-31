import ue

class ChildNode:
	def __init__(self, composite, task, decorator):
		self.composite = composite
		self.task = task
		self.decorator = decorator

class CompositeNode:
	def __init__(self, func, children):
		self.func = func
		self.children = children
		self.exePending = []

	def Run(self):
		if len(self.exePending) == 0:
			self.exePending = self.children.copy()
		result, isRunning = self.func(self.exePending)
		if not isRunning:
			self.exePending.clear()
		return result, isRunning

class TaskNode:
	def __init__(self, func):
		self.func = func

	def Run(self):
		result, isRunning = self.func(self.exePending)
		return result, isRunning

class MyBehaviorTree:
	def __init__(self, robot):
		self.root = None
		self.robot = robot
		self.servicesList = []
		self.blackboard = {}
		self.blackboard["SelfActor"] = None
		self.blackboard["Print"] = False

	def printFirst_C_0(self):
		print("First print String")
		return True, False

	def BTDecorator_Blackboard_1(self):
		if not self.blackboard["Print"]:
			return True
		return False

	def printSecond_C_0(self):
		print("Second print String!!!!!!!!!")
		return True, False

	def BTDecorator_Blackboard_2(self):
		if self.blackboard["Print"]:
			return True
		return False

	def BTComposite_Selector_0(self, exePending):
		for _ in range(len(exePending)):
			exe = exePending[0]
			if len(exe.decorators) != 0:
				for decorator in exe.decorators:
					if not decorator():
						return False, False
			if exe.task != None:
				result, isRunning = exe.task.Run()
			if exe.composite != None:
				result, isRunning = exe.composite.Run()
			if result:
				return result, isRunning
			exePending.pop(0)
		return False, False


	def changeBlackboard_C_0(self):
		self.blackboard["Print"] = not self.blackboard["Print"]
		return True, False

	def BTComposite_Sequence_0(self, exePending):
		for _ in range(len(exePending)):
			exe = exePending[0]
			if len(exe.decorators) != 0:
				for decorator in exe.decorators:
					if not decorator():
						return False, False
			if exe.task != None:
				result, isRunning = exe.task.Run()
			if exe.composite != None:
				result, isRunning = exe.composite.Run()
			if not result:
				return False, False
			if isRunning:
				return True, True
			exePending.pop(0)
		return True, False


	def Create(self):
		children_0 = []
		task_0 = None
		decorators_0 = None
		children_1 = []
		task_1 = TaskNode(self.printFirst_C_0)
		decorators_1 = []
		decorators_1.append(self.BTDecorator_Blackboard_1)
		composite_1 = None
		childNode_1 = ChildNode(composite_1, task_1, decorators_1)
		children_1.append(childNode_1)
		task_1 = TaskNode(self.printSecond_C_0)
		decorators_1 = []
		decorators_1.append(self.BTDecorator_Blackboard_2)
		composite_1 = None
		childNode_1 = ChildNode(composite_1, task_1, decorators_1)
		children_1.append(childNode_1)
		composite_0 = CompositeNode(self.BTComposite_Selector_0, children_1)
		childNode_0 = ChildNode(composite_0, task_0, decorators_0)
		children_0.append(childNode_0)
		task_0 = TaskNode(self.changeBlackboard_C_0)
		decorators_0 = None
		composite_0 = None
		childNode_0 = ChildNode(composite_0, task_0, decorators_0)
		children_0.append(childNode_0)
		self.root = CompositeNode(self.BTComposite_Sequence_0, children_0)


	def Run(self):
		self.root.Run()