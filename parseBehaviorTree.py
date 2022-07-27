import propertyType
import behaviorTreeType


def parseTaskProperty(property, _type):
    if _type == "Blueprint":
        return None
    if _type == "MoveTo":
        parseProperty = propertyType.TaskMoveToProperty(
            property["AcceptableRadius"], property["BlackboardKey"])
    if _type == "MakeNoise":
        parseProperty = propertyType.TaskMakeNoiseProperty(
            property["Loudnes"])
    if _type == "MoveDirectlyToward":
        parseProperty = propertyType.TaskMoveDirectlyTowardProperty(
            property["AcceptableRadius"], property["BlackboardKey"])
    if _type == "PlayAnimation":
        parseProperty = propertyType.TaskPlayAnimationProperty(
            property["Animation"], property["Loop"],
            property["Block"])
    if _type == "PlaySound":
        parseProperty = propertyType.TaskPlaySoundProperty(
            property["Sound"])
    if _type == "PushPawnAction":
        parseProperty = propertyType.TaskPushPawnAction(
            property["Action"])
    if _type == "RotateToFaceBBEntry":
        parseProperty = propertyType.TaskRotateToFaceBBEntryProperty(
            property["Precision"], property["BlackboardKey"])
    if _type == "RunBehavior":
        parseProperty = propertyType.TaskRunBehaviorProperty(
            property["Behavior"])
    if _type == "WaitBlackboardTime":
        parseProperty = propertyType.TaskWaitBlackboardTimeProperty(
            property["BlackboardKey"])
    if _type == "Wait":
        parseProperty = propertyType.TaskWaitProperty(
            property["WaitTime"], property["RandomDeviation"])
    if _type == "RunBehaviorDynamic":
        parseProperty = propertyType.TaskRunBehaviorDynamicProperty(
            property["Tag"], property["Behavior"])
    if _type == "SetTagCooldown":
        parseProperty = propertyType.TaskSetTagCooldownProperty(
            property["Tag"], property["Cooldown"])
    if _type == "RunEQSQuery":
        parseProperty = propertyType.TaskRunEQSQueryProperty(
            property["QueryName"], property["BlackboardKey"],
            property["RunMode"], property["QueryConfig"])
    return parseProperty


def parseTaskNode(taskNode):
    taskName = taskNode["Name"]
    taskType = taskNode["Type"]
    taskProperty = parseTaskProperty(taskNode["Property"], taskType)
    newTaskNode = behaviorTreeType.TaskNode(taskName, taskType, taskProperty)
    return newTaskNode


def parseDecoratorProperty(property, _type):
    # print(_type)
    if _type == "Blackboard":
        parseProperty = propertyType.DecoratorBlackboardProperty(
            property["BlackboardKey"], property["OpsType"],
            property["IntValue"], property["FloatValue"],
            property["StringValue"])
    if _type == "CheckGameplayTagsOnActor":
        parseProperty = propertyType.DecoratorCheckGameplayTagsProperty(
            property["ActorToCheck"], property["TagsToMatch"], property["tags"]
        )
    if _type == "CompareBBEntries":
        parseProperty = propertyType.DecoratorCompareBBEntryProperty(
            property["BlackboardKeyA"], property["BlackboardKeyB"],
            property["Operation"])
    if _type == "ConditionalLoop":
        parseProperty = propertyType.DecoratorConditionLoopProperty(
            property["BlackboardKey"], property["OpsType"],
            property["IntValue"], property["FloatValue"],
            property["StringValue"])
    if _type == "ConeCheck":
        parseProperty = propertyType.DecoratorConeCheckProperty(
            property["ConeHalfAngle"], property["ConeOrigin"],
            property["ConeDirection"], property["Observed"])
    if _type == "Cooldown":
        parseProperty = propertyType.DecoratorCooldownProperty(
            property["CoolDownTime"])
    if _type == "DoesPathExist":
        parseProperty = propertyType.DecoratorDoesPathExistProperty(
            property["BlackboardKeyA"], property["BlackboardKeyB"])
    if _type == "ForceSuccess":
        return None
    if _type == "IsAtLocation":
        parseProperty = propertyType.DecoratorIsAtLocationProperty(
            property["BlackboardKey"], property["AcceptableRadius"],
            property["GeometricDistanceType"],
            property["ParametrizedAcceptableRadius"],
            property["bUseParametrizedRadius"],
            property["bUseNavAgentGoalLocation"],
            property["bPathFindingBasedTest"])
    if _type == "IsBBEntryOfClass":
        parseProperty = propertyType.DecoratorIsBBEntryOfClassProperty(
            property["BlackboardKey"], property["TestClass"])
    if _type == "KeepInCone":
        parseProperty = propertyType.DecoratorKeepInConeProperty(
            property["ConeHalfAngle"], property["ConeOrigin"],
            property["Observed"])
    if _type == "Loop":
        parseProperty = propertyType.DecoratorLoopProperty(
            property["NumLoops"], property["InfiniteLoop"],
            property["InfiniteLoopTimeoutTime"])
    if _type == "SetTagCooldown":
        parseProperty = propertyType.DecoratorSetTagCooldownProperty(
            property["CooldownTag"], property["CooldownDuration"],
            property["AddToExistingDuration"])
    if _type == "TimeLimit":
        parseProperty = propertyType.DecoratorTimeLimitProperty(
            property["TimeLimit"])
    if _type == "TagCooldown":
        parseProperty = propertyType.DecoratorTagCooldownProperty(
            property["CooldownTag"], property["CooldownDuration"],
            property["AddToExistingDuration"],
            property["ActivatesCooldown"])
    if _type == "Blueprint":
        return None
    return parseProperty


def parseDecorator(decoratorNodes):
    decoratorNodeList = []
    for decoratorNode in decoratorNodes:
        decoratorName = decoratorNode["Name"]
        decoratorType = decoratorNode["Type"]
        decoratorProperty = parseDecoratorProperty(
            decoratorNode["Property"], decoratorType)
        newDecoratorNode = behaviorTreeType.DecoratorNode(
            decoratorName, decoratorType, decoratorProperty)
        decoratorNodeList.append(newDecoratorNode)
    return decoratorNodeList


def parseDecoratorOp(decoratorOp):
    decoratorOpList = []
    for op in decoratorOp:
        newDecoratorOp = behaviorTreeType.DecoratorOps(
            op["Operation"], op["Number"])
        decoratorOpList.append(newDecoratorOp)
    return decoratorOpList


def parseServiceProperty(property, _type):
    if _type == "RunEQS":
        parseProperty = propertyType.ServiceEQSProperty(
            property["BlackboardKey"], property["Interval"],
            property["RandomDeviation"], property["QueryName"],
            property["RunMode"], property["QueryConfig"])
    if _type == "DefaultFocus":
        parseProperty = propertyType.ServiceDefaultFocusProperty(
            property["BlackboardKey"], property["Interval"],
            property["RandomDeviation"])
    if _type == "Blueprint":
        parseProperty = propertyType.ServiceBlueprintProperty(
            property["Interval"], property["RandomDeviation"])
    return parseProperty


def parseCompositeNode(compositeNode):
    compositeName = compositeNode["Name"]
    compositeType = compositeNode["Type"]
    compositeFinishMode = compositeNode["FinishMode"]
    compositeChildren = compositeNode["Children"]
    compositeServices = compositeNode["Services"]
    parseChildren = []
    for child in compositeChildren:
        childComposite = None
        childTask = None
        childDecorator = None
        childDecoratorOp = None
        if child["ChildComposite"] is not None:
            childComposite = parseCompositeNode(child["ChildComposite"])
        if child["ChildTask"] is not None:
            childTask = parseTaskNode(child["ChildTask"])
        if child["Decorators"] is not None:
            childDecorator = parseDecorator(child["Decorators"])
        if child["DecoratorOps"] is not None:
            childDecoratorOp = parseDecoratorOp(child["DecoratorOps"])
        child = behaviorTreeType.ChildNode(childComposite, childTask,
                                           childDecorator, childDecoratorOp)
        parseChildren.append(child)
    parseServices = []
    if compositeServices is not None:
        for service in compositeServices:
            serviceProperty = parseServiceProperty(
                service["Property"], service["Type"])
            newService = behaviorTreeType.ServicesNode(
                service["Name"], service["Type"], serviceProperty)
            parseServices.append(newService)
    newComposite = behaviorTreeType.CompositeNode(
        compositeName, compositeType, parseChildren, parseServices,
        compositeFinishMode)
    return newComposite
