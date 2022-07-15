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


class DecoratorNode:
    def __init__(self, _name, _type, _property):
        self._name = _name
        self._type = _type
        self._property = _property


class DecoratorOps:
    def __init__(self, _operation, _number):
        self._operation = _operation
        self._number = _number


class ServicesNode:
    def __init__(self, _name, _type, _property):
        self._name = _name
        self._type = _type
        self._property = _property
