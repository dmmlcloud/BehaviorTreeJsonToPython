import propertyType


class BehaviorTree:
    def __init__(self, _name, _blackboard, _root):
        self._name = _name
        self._blackboard = _blackboard
        self._root = _root


class Blackboard:
    def __init__(self, _keys):
        self._keys = _keys

    def initialize(self):
        blackboardStr = ""
        for key in self._keys:
            blackboardStr += "blackboard[\"" + \
                 key._name + "\"] = "
            if key._type == "Bool":
                blackboardStr += "False\n"
            if key._type == "Int" or key._type == "Enum":
                blackboardStr += "0\n"
            if key._type == "Float":
                blackboardStr += "0.0\n"
            if key._type == "String" or key._type == "Name":
                blackboardStr += "\"\"\n"
            if key._type == "Class" or key._type == "Object" or \
                    key._type == "Vector" or key._type == "Rotator":
                blackboardStr += "None\n"
        blackboardStr += "\n"
        return blackboardStr

    def findEntry(self, keyName):
        for key in self._keys:
            if keyName == key._name:
                return key
        return None


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
    def __init__(self, _name, _type, _children, _services, _finishMode,
                 _blackboard):
        self._name = _name
        self._type = _type
        self._children = _children
        self._services = _services
        self._finishMode = _finishMode
        self._blackboard = _blackboard

    def translate(self):
        # translate node to function, use node name as function's name
        transString = "\tdef " + self._name + "(self, exePending):\n"
        indent = "\t\t"
        # first begin service
        if self._services is not None:
            for service in self._services:
                transString += indent + "self." + service._name + "()\n"
        # depends on different composite type
        # selector
        if self._type == "Selector":
            transString += indent + "for _ in range(len(exePending)):\n"
            indent = "\t\t\t"
            transString += indent + "exe = exePending[0]\n"
            transString += indent + "flag = True\n"
            transString += indent + "if exe.decorators is not None and len(exe.decorators) != 0:\n"
            indent = "\t\t\t\t"
            transString += indent + "for decorator in exe.decorators:\n"
            indent = "\t\t\t\t\t"
            transString += indent + "if not decorator():\n"
            indent = "\t\t\t\t\t\t"
            transString += indent + "exePending.pop(0)\n"
            transString += indent + "flag = False\n"
            transString += indent + "break\n"
            indent = "\t\t\t\t"
            transString += indent + "if not flag:\n"
            indent = "\t\t\t\t\t"
            transString += indent + "continue\n"
            indent = "\t\t\t"
            transString += indent + "if exe.task is not None:\n"
            indent = "\t\t\t\t"
            transString += indent + "result, isRunning = exe.task.Run()\n"
            indent = "\t\t\t"
            transString += indent + "if exe.composite is not None:\n"
            indent = "\t\t\t\t"
            transString += indent + "result, isRunning = exe.composite.Run()\n"
            indent = "\t\t\t"
            transString += indent + "if result:\n"
            indent = "\t\t\t\t"
            transString += indent + "return result, isRunning\n"
            indent = "\t\t\t"
            transString += indent + "exePending.pop(0)\n"
            indent = "\t\t"
            transString += indent + "return False, False\n"
            # if self._children is not None:
            #     for child in self._children:
            #         # if have decorator, call function and judge from the
            #         # result of the decorator function
            #         indent = "\t\t"
            #         if child._decorators is not None:
            #             transString += indent + "if "
            #             for i, decorator in enumerate(child._decorators):
            #                 transString += "self." + decorator._name + "()"
            #                 if i != len(child._decorators) - 1:
            #                     transString += " && "
            #                 else:
            #                     transString += ":\n"
            #             indent += "\t"
            #         # call children nodes
            #         if child._childComposite is not None:
            #             transString += indent + "if self." + \
            #                 child._childComposite._name + "():\n" + \
            #                 indent + "\treturn True\n"
            #         if child._childTask is not None:
            #             transString += indent + "if self." + \
            #                 child._childTask._name + "():\n" + indent + \
            #                 "\treturn True\n"
            #     indent = "\t\t"
            #     transString += indent + "return False\n"
        # sequence
        if self._type == "Sequence":
            transString += indent + "for _ in range(len(exePending)):\n"
            indent = "\t\t\t"
            transString += indent + "exe = exePending[0]\n"
            transString += indent + "if exe.decorators is not None and len(exe.decorators) != 0:\n"
            indent = "\t\t\t\t"
            transString += indent + "for decorator in exe.decorators:\n"
            indent = "\t\t\t\t\t"
            transString += indent + "if not decorator():\n"
            indent = "\t\t\t\t\t\t"
            transString += indent + "return False, False\n"
            indent = "\t\t\t"
            transString += indent + "if exe.task is not None:\n"
            indent = "\t\t\t\t"
            transString += indent + "result, isRunning = exe.task.Run()\n"
            indent = "\t\t\t"
            transString += indent + "if exe.decorators is not None and exe.composite is not None:\n"
            indent = "\t\t\t\t"
            transString += indent + "result, isRunning = exe.composite.Run()\n"
            indent = "\t\t\t"
            transString += indent + "if not result:\n"
            indent = "\t\t\t\t"
            transString += indent + "return False, False\n"
            indent = "\t\t\t"
            transString += indent + "if isRunning:\n"
            indent = "\t\t\t\t"
            transString += indent + "return True, True\n"
            indent = "\t\t\t"
            transString += indent + "exePending.pop(0)\n"
            indent = "\t\t"
            transString += indent + "return True, False\n"
            # if self._children is not None:
            #     for child in self._children:
            #         indent = "\t\t"
            #         if child._decorators is not None:
            #             transString += indent + "if "
            #             for i, decorator in enumerate(child._decorators):
            #                 transString += "self." + decorator._name + "()"
            #                 if i != len(child._decorators) - 1:
            #                     transString += " && "
            #                 else:
            #                     transString += ":\n"
            #             indent += "\t"
            #         # call children nodes
            #         if child._childComposite is not None:
            #             transString += indent + "if self." + \
            #                 child._childComposite._name + "() is False:\n" + \
            #                 indent + "\treturn False\n"
            #         if child._childTask is not None:
            #             transString += indent + "if self." + \
            #                 child._childTask._name + "() is False:\n" + \
            #                 indent + "\treturn False\n"
            #     indent = "\t\t"
            #     transString += indent + "return True\n"
        # parallel
        secondTask = False
        if self._type == "SimpleParallel":
            if self._children is not None:
                for child in self._children:
                    indent = "\t\t"
                    if child._decorators is not None:
                        transString += indent + "if "
                        for i, decorator in enumerate(child._decorators):
                            transString += "self." + decorator._name + "()"
                            if i != len(child._decorators) - 1:
                                transString += " && "
                            else:
                                transString += ":\n"
                        indent += "\t"
                    # call children nodes
                    # if have composite child, it must be background
                    if child._childComposite is not None:
                        transString += indent + \
                            "paraThread = threading.Thread(target = " +\
                            "self." + child._childComposite._name + ")\n"
                    # execute main task
                    if child._childTask is not None:
                        if secondTask is True:
                            transString += indent + \
                                "paraThread = threading.Thread(target = " +\
                                "self." + child._childTask._name + ")\n"
                        else:
                            transString += indent + "result = self." + \
                                child._childTask._name + "()\n"
                            secondTask = True
                if self._finishMode == "AbortBackground":
                    transString += indent + "print(\"Stop thread\")\n"
                else:
                    transString += indent + "paraThread.join()\n"
                transString += indent + "return result\n"
        transString += "\n\n"
        return transString


class ChildNode:
    def __init__(self, _childComposite, _childTask, _decorators,
                 _decoratorOps):
        self._childComposite = _childComposite
        self._childTask = _childTask
        self._decorators = _decorators
        self._decoratorOps = _decoratorOps


class TaskNode:
    def __init__(self, _name, _type, _property, _blackboard):
        self._name = _name
        self._type = _type
        self._property = _property
        self._blackboard = _blackboard

    def translate(self):
        transString = "\tdef " + self._name + "(self):\n"
        indent = "\t\t"
        if self._type == "MoveTo":
            transString += self.translateMoveTo()
        if self._type == "Blueprint":
            transString += self.translateBlueprint()
        if self._type == "MakeNoise":
            transString += indent + "print(\"MakeNoise task\\n\")\n\n"
        if self._type == "MoveDirectlyToward":
            transString += indent + \
                "print(\"Move Directly Toward task!\\n\")\n\n"
        if self._type == "PlayAnimation":
            transString += indent + "print(\"Play animation task\\n\")\n\n"
        if self._type == "PlaySound":
            transString += indent + "print(\"Play Sound task\\n\")\n\n"
        if self._type == "PushPawnAction":
            transString += indent + "print(\"Push Pawn Action task!\\n\")\n\n"
        if self._type == "RotateToFaceBBEntry":
            transString += indent + \
                "print(\"Rotate To Face BB Entry task\\n\")\n\n"
        if self._type == "RunBehavior":
            transString += indent + "print(\"Run Behavior task\\n\")\n\n"
        if self._type == "WaitBlackboardTime":
            transString += indent + \
                "print(\"Wait Blackboard Time task\\n\")\n\n"
        if self._type == "Wait":
            transString += indent + "print(\"Wait task!\\n\")\n\n"
        if self._type == "RunBehaviorDynamic":
            transString += indent + \
                "print(\"Run behavior dynamic task\\n\")\n\n"
        if self._type == "SetTagCooldown":
            transString += indent + "print(\"Set tag cooldown task\\n\")\n\n"
        if self._type == "RunEQSQuery":
            transString += indent + "print(\"Run EQS Query task\\n\")\n\n"
        return transString

    def translateMoveTo(self):
        transString = ""
        indent = "\t\t"
        transString += indent + "nowLocation = self.robot.GetActorLocation()\n"
        transString += indent + "targetLocation = blackboard[\"" + self._property.blackboardKey + "\"]\n"
        transString += indent + "if(ue.Vector.Distance(targetLocation, nowLocation) < 100.0):\n"
        transString += indent + "\treturn True, False\n"
        transString += indent + "normalVector = (targetLocation - nowLocation).GetSafeNormal()\n"
        transString += indent + "robotMovement = self.robot.GetMovementComponent()\n"
        transString += indent + "robotMovement.AddInputVector(normalVector, False)\n"
        transString += indent + "return True, True\n\n"
        return transString

    def translateBlueprint(self):
        transString = ""
        indent = "\t\t"
        # for test
        if "printFirst" in self._name:
            transString += indent + "print(\"First print String\")\n"
        if "printSecond" in self._name:
            transString += indent + "print(\"Second print String!!!!!!!!!\")\n"
        if "changeBlackboard" in self._name:
            transString += indent + "blackboard[\"Print\"] = " + \
                "not blackboard[\"Print\"]\n"

        # for move Task
        if "ChangeMoveSpeed" in self._name:
            transString += indent + "robotMovement = self.robot.GetMovementComponent()\n"
            transString += indent + "robotMovement.MaxWalkSpeed = " + self._property.variable["Speed"] + "\n"
        if "MoveToRandomPos" in self._name:
            # floor = robotMovementComponent.FindFloor(randomVector)
            transString += indent + "randomVector = ue.KismetMathLibrary.RandomPointInBoundingBox(self.robot.GetActorLocation(), ue.Vector(1000.0, 1000.0, 0.0))\n"
            transString += indent + "floor = self.robot.GetMovementComponent().FindFloor(randomVector)\n"
            transString += indent + "if floor is None or not floor.bWalkableFloor:\n"
            transString += indent + "\treturn True, True\n"
            transString += indent + "blackboard[\"RandomPos\"] = randomVector\n"
        transString += indent + "return True, False\n\n"
        return transString


class DecoratorNode:
    def __init__(self, _name, _type,
                 _property,
                 _blackboard):
        self._name = _name
        self._type = _type
        self._property = _property
        self._blackboard = _blackboard

    def translate(self):
        transString = "\tdef " + self._name + "(self):\n"
        indent = "\t\t"
        if self._type == "Blackboard":
            transString += self.translateBlackboardNode()
        if self._type == "Blueprint":
            transString += indent + "print(\"Blueprint decorator!\\n\")\n\n"
        if self._type == "CheckGameplayTagsOnActor":
            transString += indent + \
                "print(\"Check gameplay tags on actor decorator!\\n\")\n\n"
        if self._type == "CompareBBEntries":
            transString += indent + \
                "print(\"Compare BB entries decorator\\n\")\n\n"
        if self._type == "ConditionalLoop":
            transString += indent + \
                "print(\"Conditional loop decorator\\n\")\n\n"
        if self._type == "ConeCheck":
            transString += indent + \
                "print(\"Cone Check decorator!\\n\")\n\n"
        if self._type == "Cooldown":
            transString += indent + "print(\"Cooldown decorator\\n\")\n\n"
        if self._type == "DoesPathExist":
            transString += indent + \
                "print(\"Does Path Exist decorator\\n\")\n\n"
        if self._type == "ForceSuccess":
            transString += indent + \
                "print(\"Force Success decorator!\\n\")\n\n"
        if self._type == "IsAtLocation":
            transString += indent + \
                "print(\"Is at location decorator\\n\")\n\n"
        if self._type == "IsBBEntryOfClass":
            transString += indent + \
                "print(\"Is BB entry of class decorator\\n\")\n\n"
        if self._type == "KeepInCone":
            transString += indent + \
                "print(\"Keep in cone decorator\\n\")\n\n"
        if self._type == "Loop":
            transString += indent + "print(\"Wait decorator!\\n\")\n\n"
        if self._type == "SetTagCooldown":
            transString += indent + \
                "print(\"Set tag cooldown decorator\\n\")\n\n"
        if self._type == "TimeLimit":
            transString += indent + "print(\"Time limit decorator\\n\")\n\n"
        if self._type == "TagCooldown":
            transString += indent + "print(\"Tag cooldown decorator\\n\")\n\n"
        return transString

    def translateBlackboardNode(self):
        transString = ""
        indent = "\t\t"
        blackboardKey = self._property.blackboardKey
        keyEntry = self._blackboard.findEntry(blackboardKey)
        valueType = keyEntry._type
        if valueType == "Bool" or valueType == "Class" or \
           valueType == "Object" or valueType == "Rotator" or \
           valueType == "Vector":
            if self._property.opsType == "NotSet":
                transString += indent + "if not blackboard[\"" + \
                    self._property.blackboardKey + "\"]:\n"
            if self._property.opsType == "Set":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"]:\n"
        if valueType == "Int" or valueType == "Float" or \
            valueType == "Enum":
            if valueType == "Float":
                keyValue = self._property.floatValue
            else:
                keyValue = self._property.intValue
            if self._property.opsType == "Equal":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] == " + \
                    keyValue + ":\n"
            if self._property.opsType == "NotEqual":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] != " + \
                    keyValue + ":\n"
            if self._property.opsType == "Less":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] < " + \
                    keyValue + ":\n"
            if self._property.opsType == "LessOrEqual":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] <= " + \
                    keyValue + ":\n"
            if self._property.opsType == "Greater":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] > " + \
                    keyValue + ":\n"
            if self._property.opsType == "GreaterOrEqual":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] >= " + \
                    keyValue + ":\n"
        if valueType == "String" or valueType == "Name":
            if self._property.opsType == "Equal":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] == \"" + \
                    self._property.stringValue + "\":\n"
            if self._property.opsType == "NotEqual":
                transString += indent + "if blackboard[\"" + \
                    self._property.blackboardKey + "\"] != \"" + \
                    self._property.stringValue + "\":\n"
            if self._property.opsType == "Contain":
                transString += indent + "if \"" + self._property.stringValue \
                    + "\" in blackboard[\"" + self._property.blackboardKey \
                    + "\"]:\n"
            if self._property.opsType == "NotContain":
                transString += indent + "if \"" + self._property.stringValue \
                    + "\" not in blackboard[\"" + self._property.blackboardKey\
                    + "\"]:\n"
        transString += indent + "\treturn True\n"
        transString += indent + "return False\n\n"
        return transString


class DecoratorOps:
    def __init__(self, _operation, _number):
        self._operation = _operation
        self._number = _number

    def translate(self):
        transString = "\tdef " + self._name + "(self):\n"
        indent = "\t\t"
        transString += indent + "print(\"decorator ops\")\n\n"
        return transString


class ServicesNode:
    def __init__(self, _name, _type, _property):
        self._name = _name
        self._type = _type
        self._property = _property

    def translate(self):
        transString = "\tdef " + self._name + "(self):\n"
        indent = "\t\t"
        if self._type == "Blueprint":
            if "CheckIfAISeePlayer" in self._name:
                transString += indent + "targetLocation = self.playerController.GetActorLocation()\n"
                transString += indent + "targetLocation.Z = 0.0\n"
                transString += indent + "robotLocation = self.robot.GetActorLocation()\n"
                transString += indent + "robotLocation.Z = 0.0\n"
                transString += indent + "disVector = (targetLocation - robotLocation).GetSafeNormal()\n"
                transString += indent + "robotForward = self.robot.GetActorForwardVector()\n"
                transString += indent + "angle = ue.KismetMathLibrary.DegAcos(ue.Vector.DotProduct(disVector, robotForward))\n"
                transString += indent + "if angle < 20.0:\n"
                transString += indent + "\tblackboard[\"State\"] = 1\n"
                transString += indent + "\tblackboard[\"TargetActor\"] = targetLocation\n\n"
        if self._type == "DefaultFocus":
            transString += indent + "print(\"default focus\")\n"
            transString += indent + "sleep(" + self._property.interval\
                + ")\n\n"
        if self._type == "RunEQS":
            transString += indent + "print(\"run EQS\")\n"
            transString += indent + "sleep(" + self._property.interval\
                + ")\n\n"
        return transString
