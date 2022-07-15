class BehaviorTree:
    def __init__(self, _name, _blackboard, _root):
        self._name = _name
        self._blackboard = _blackboard
        self._root = _root


class Blackboard:
    def __init__(self, _keys):
        self._keys = _keys


class BlackboardKey:
    def __init__(self, _name, _type):
        self._name = _name
        self._type = _type


class BlackboardGeneratedKey:
    def __init__(self, _name, _type, _base):
        self._name = _name
        self._type = _type
        self._base = _base


class CompositeNode:
    def __init__(self, _name, _type, _children, _services):
        self._name = _name
        self._type = _type
        self._children = _children
        self._service = _services
    def translate(self):
        # translate node to function, use node name as function's name
        transString = "def " + self._name + ":\n"
        indent = "\t"
        # first begin service
        # todo: maybe need create thread to execute
        if self._service != None:
            for service in self._services:
        
        # depends on different composite type
        if self._type == "Selector":
            if self._children != None:
                for child in self._children:
                    # if have decorator, call function and judge from the result of the decorator function
                    if child._decorators != None:
                        transString += indent + "if "
                        for i, decorator in enumerate(child._decorators):
                            transString += decorator._name + "()"
                            if i != len(child._decorators) - 1:
                                transString += " && "
                            else:
                                transString += ":\n"
                        indent += "\t"
                    # call children nodes
                    if child._childComposite != None:
                        transString += indent + "if " + child._childComposite._name + "():\n" + indent + "\treturn True"
                        transString += indent + "\treturn True"
                        transString += indent + "else:"
                        transString += indent + "\treturn False"
                    if child._childTask != None:
                        for task in child._childTask:
                            transString += indent + "if " + child._childTask._name + "():\n" + indent + "\treturn True"
                            transString += indent + "\treturn True"
                            transString += indent + "else:"
                            transString += indent + "\treturn False"
        if self._service != None:
            for service in self._services:
                
        return transString


class ChildNode:
    def __init__(self, _childComposite, _childTask, _decorators,
                 _decoratorOps):
        self._childComposite = _childComposite
        self._childTask = _childTask
        self._decorators = _decorators
        self._decoratorOps = _decoratorOps


class TaskNode:
    def __init__(self, _name, _type, _property):
        self._name = _name
        self._type = _type
        self._property = _property
    def translate(self):
        transString = ""
        return transString


class DecoratorNode:
    def __init__(self, _name, _type, _property):
        self._name = _name
        self._type = _type
        self._property = _property
    def translate(self):
        transString = ""
        return transString


class DecoratorOps:
    def __init__(self, _operation, _number):
        self._operation = _operation
        self._number = _number
    def translate(self):
        transString = ""
        return transString


class ServicesNode:
    def __init__(self, _name, _type, _property):
        self._name = _name
        self._type = _type
        self._property = _property
    def translate(self):
        transString = ""
        return transString
