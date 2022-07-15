# Task node
class TaskMoveToProperty:
    def __init__(self, acceptableRadius, blackboardKey):
        self.acceptableRadius = acceptableRadius
        self.blackboardKey = blackboardKey


class TaskMakeNoiseProperty:
    def __init__(self, loudnes):
        self.loudnes = loudnes


class TaskMoveDirectlyTowardProperty:
    def __init__(self, acceptableRadius, blackboardKey):
        self.acceptableRadius = acceptableRadius
        self.blackboardKey = blackboardKey


class TaskPlayAnimationProperty:
    def __init__(self, animation, loop, block):
        self.animation = animation
        self.loop = loop
        self.block = block


class TaskPlaySoundProperty:
    def __init__(self, sound):
        self.sound = sound


class TaskPushPawnAction:
    def __init__(self, action):
        self.action = action


class TaskRotateToFaceBBEntryProperty:
    def __init__(self, precision, blackboardKey):
        self.precision = precision
        self.blackboardKey = blackboardKey


class TaskRunBehaviorProperty:
    def __init__(self, behavior):
        self.behavior = behavior


class TaskWaitBlackboardTimeProperty:
    def __init__(self, blackboardKey):
        self.blackboardKey = blackboardKey


class TaskWaitProperty:
    def __init__(self, waitTime, randonDeviation):
        self.waitTime = waitTime
        self.randonDeviation = randonDeviation


class TaskRunBehaviorDynamicProperty:
    def __init__(self, tag, behavior):
        self.tag = tag
        self.behaivor = behavior


class TaskSetTagCooldownProperty:
    def __init__(self, tag, cooldown):
        self.tag = tag
        self.cooldown = cooldown


class TaskRunEQSQueryProperty:
    def __init__(self, queryName, blackboardKey, runMode, queryConfig):
        self.queryName = queryName
        self.blackboardKey = blackboardKey
        self.runMode = runMode
        self.queryConfig = queryConfig

# Decorator node


class DecoratorBlackboardProperty:
    def __init__(self, blackboardKey, opsType, intValue, floatValue,
                 stringValue):
        self.blackboardKey = blackboardKey
        self.opsType = opsType
        self.intValue = intValue
        self.floatValue = floatValue
        self.stringValue = stringValue


class DecoratorCheckGameplayTagsProperty:
    def __init__(self, actorToCheck, tagToMatch, tags):
        self.actorToCheck = actorToCheck
        self.tagToMatch = tagToMatch
        self.tags = tags


class DecoratorCompareBBEntryProperty:
    def __init__(self, blackboardKeyA, blackboardKeyB, operation):
        self.blackboardKeyA = blackboardKeyA
        self.blackboardKeyB = blackboardKeyB
        self.operation = operation


class DecoratorConditionLoopProperty:
    def __init__(self, blackboardKey, opsType, intValue, floatValue,
                 stringValue):
        self.blackboardKey = blackboardKey
        self.opsType = opsType
        self.intValue = intValue
        self.floatValue = floatValue
        self.stringValue = stringValue


class DecoratorConeCheckProperty:
    def __init__(self, coneHalfAngle, coneOrigin, coneDirection,
                 observed):
        self.coneHalfAngle = coneHalfAngle
        self.coneOrigin = coneOrigin
        self.coneDirection = coneDirection
        self.observed = observed


class DecoratorCooldownProperty:
    def __init__(self, cooldownTime):
        self.cooldownTime = cooldownTime


class DecoratorDoesPathExistProperty:
    def __init__(self, blackboardKeyA, blackboardKeyB):
        self.blackboardKeyA = blackboardKeyA
        self.blackboardKeyB = blackboardKeyB


class DecoratorIsAtLocationProperty:
    def __init__(self, blackboardKey, acceptableRadius,
                 geometricDistanceType, parametrizedAcceptableRadius,
                 bUseParametrizedRadius, bUseNavAgentGoalLocation,
                 bPathFindingBasedTest):
        self.blackboardKey = blackboardKey
        self.acceptableRadius = acceptableRadius
        self.geometricDistanceType = geometricDistanceType
        self.parametrizedAcceptableRadius = parametrizedAcceptableRadius
        self.bUseParametrizedRadius = bUseParametrizedRadius
        self.bUseNavAgentGoalLocation = bUseNavAgentGoalLocation
        self.bPathFindingBasedTest = bPathFindingBasedTest


class DecoratorIsBBEntryOfClassProperty:
    def __init__(self, blackboardKey, testClass):
        self.blackboardKey = blackboardKey
        self.testClass = testClass


class DecoratorKeepInConeProperty:
    def __init__(self, coneHalfAngle, coneOrigin, observed):
        self.coneHalfAngle = coneHalfAngle
        self.coneOrigin = coneOrigin
        self.observed = observed


class DecoratorLoopProperty:
    def __init__(self, numLoops, infiniteLoop, infiniteLoopTimeoutTime):
        self.numLoops = numLoops
        self.infiniteLoop = infiniteLoop
        self.infiniteLoopTimeoutTime = infiniteLoopTimeoutTime


class DecoratorSetTagCooldownProperty:
    def __init__(self, cooldownTag, cooldownDuration, addToExistingDuration):
        self.cooldownTag = cooldownTag
        self.cooldownDuration = cooldownDuration
        self.addToExistingDuration = addToExistingDuration


class DecoratorTimeLimitProperty:
    def __init__(self, timeLimit):
        self.timeLimit = timeLimit


class DecoratorTagCooldownProperty:
    def __init__(self, cooldownTag, cooldownDuration, addToExistingDuration,
                 activatesCooldown):
        self.cooldownTag = cooldownTag
        self.cooldownDuration = cooldownDuration
        self.addToExistingDuration = addToExistingDuration
        self.activatesCooldown = activatesCooldown


# Service Node
class ServiceEQSProperty:
    def __init__(self, blackboardKey, interval, deviation, queryName, runMode,
                 queryConfig):
        self.blackboardKey = blackboardKey
        self.interval = interval
        self.deviation = deviation
        self.queryName = queryName
        self.runMode = runMode
        self.queryConfig = queryConfig


class ServiceDefaultFocusProperty:
    def __init__(self, blackboardKey, interval, deviation):
        self.blackboardKey = blackboardKey
        self.interval = interval
        self.deviation = deviation


class ServiceBlueprintProperty:
    def __init__(self, interval, deviation):
        self.interval = interval
        self.deviation = deviation
