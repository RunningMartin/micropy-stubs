class Align:
    """
    Alignment of an image on the display.
    """
    BOTTOM_LEFT: ...
    BOTTOM: ...
    BOTTOM_RIGHT: ...
    LEFT: ...
    CENTER: ...
    RIGHT: ...
    TOP_LEFT: ...
    TOP: ...
    TOP_RIGHT: ...


class Button:
    """
    Buttons on a brick or remote.
    """
    LEFT_DOWN: ...
    DOWN: ...
    RIGHT_DOWN: ...
    LEFT: ...
    CENTER: ...
    RIGHT: ...
    LEFT_UP: ...
    UP: ...
    BEACON: ...
    RIGHT_UP: ...


class Color:
    """
    Light or surface color.
    """
    BLACK: ...
    BLUE: ...
    GREEN: ...
    YELLOW: ...
    RED: ...
    WHITE: ...
    BROWN: ...
    ORANGE: ...
    PURPLE: ...


class Port:
    """
    Port on the EV3 Programmable Brick.

    ----------
    Motor Ports: A, B, C, D

    Sensor Ports: S1, S2, S3, S4
    """
    A: ...
    B: ...
    C: ...
    D: ...
    S1: ...
    S2: ...
    S3: ...
    S4: ...


class Direction:
    """
    Rotational direction for positive speed values: clockwise or counterclockwise.
    For all motors, this is defined when looking at the shaft, just like looking at a clock.
    For NXT or EV3 motors, make sure to look at the motor with the red/orange shaft to the lower right.

    ----------
    CLOCKWISE: A positive speed value should make the motor move clockwise.

    COUNTERCLOCKWISE: A positive speed value should make the motor move counterclockwise.
    """
    CLOCKWISE: ...
    COUNTERCLOCKWISE: ...


class Stop:
    """
    Action after the motor stops: coast, brake, or hold.

    ----------
    COAST: Let the motor move freely.

    BRAKE: Passively resist small external forces.

    HOLD: Keep controlling the motor to hold it at the commanded angle. This is only available on motors with encoders.
    """
    COAST: ...
    BRAKE: ...
    HOLD: ...


class ImageFile:
    """
    Paths to standard EV3 images.

    ----------
    Information: RIGHT, FORWARD, ACCEPT, QUESTION_MARK, STOP_1, LEFT, DECLINE, THUMBS_DOWN, BACKWARD, NO_GO, WARNING, STOP_2, THUMBS_UP

    LEGO&reg;: EV3, EV3_ICON

    Objects: TARGET

    Eyes: BOTTOM_RIGHT, BOTTOM_LEFT, EVIL, CRAZY_2, KNOCKED_OUT, PINCHED_RIGHT, WINKING, DIZZY, DOWN, TIRED_MIDDLE, MIDDLE_RIGHT, SLEEPING, MIDDLE_LEFT, TIRED_RIGHT, PINCHED_LEFT, PINCHED_MIDDLE, CRAZY_1, NEUTRAL, AWAKE, UP, TIRED_LEFT, ANGRY
    """
    RIGHT: ...
    FORWARD: ...
    ACCEPT: ...
    QUESTION_MARK: ...
    STOP_1: ...
    LEFT: ...
    DECLINE: ...
    THUMBS_DOWN: ...
    BACKWARD: ...
    NO_GO: ...
    WARNING: ...
    STOP_2: ...
    THUMBS_UP: ...
    EV3: ...
    EV3_ICON: ...
    TARGET: ...
    BOTTOM_RIGHT: ...
    BOTTOM_LEFT: ...
    EVIL: ...
    CRAZY_2: ...
    KNOCKED_OUT: ...
    PINCHED_RIGHT: ...
    WINKING: ...
    DIZZY: ...
    DOWN: ...
    TIRED_MIDDLE: ...
    MIDDLE_RIGHT: ...
    SLEEPING: ...
    MIDDLE_LEFT: ...
    TIRED_RIGHT: ...
    PINCHED_LEFT: ...
    PINCHED_MIDDLE: ...
    CRAZY_1: ...
    NEUTRAL: ...
    AWAKE: ...
    UP: ...
    TIRED_LEFT: ...
    ANGRY: ...


class SoundFile:
    """
    Paths to standard EV3 sounds.

    ----------
    Expressions: SHOUTING, CHEERING, CRYING, OUCH, LAUGHING_2, SNEEZING, SMACK, BOING, BOO, UH_OH, SNORING, KUNG_FU, FANFARE, CRUNCHING, MAGIC_WAND, LAUGHING_1

    Information: LEFT, BACKWARDS, RIGHT, OBJECT, COLOR, FLASHING, ERROR, ERROR_ALARM, DOWN, FORWARD, ACTIVATE, SEARCHING, TOUCH, UP, ANALYZE, STOP, DETECTED, TURN, START

    Communication: MORNING, EV3, GO, GOOD_JOB, OKEY_DOKEY, GOOD, NO, THANK_YOU, YES, GAME_OVER, OKAY, SORRY, BRAVO, GOODBYE, HI, HELLO, MINDSTORMS, LEGO, FANTASTIC

    Movements: SPEED_IDLE, SPEED_DOWN, SPEED_UP

    Color: BROWN, GREEN, BLACK, WHITE, RED, BLUE, YELLOW

    Mechanical: TICK_TACK, HORN_1, BACKING_ALERT, MOTOR_IDLE, AIR_RELEASE, AIR, BRAKE, RATCHET, MOTOR_STOP, HORN_2, LASER, SONAR, MOTOR_START

    Animals: INSECT_BUZZ_2, ELEPHANT_CALL, SNAKE_HISS, DOG_BARK_2, DOG_WHINE, INSECT_BUZZ_1, DOG_SNIFF, T_REX_ROAR, INSECT_CHIRP, DOG_GROWL, SNAKE_RATTLE, DOG_BARK_1, CAT_PURR

    Numbers: ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN

    System: READY, CONFIRM, GENERAL_ALERT, CLICK, OVERPOWER
    """
    SHOUTING: ...
    CHEERING: ...
    CRYING: ...
    OUCH: ...
    LAUGHING_2: ...
    SNEEZING: ...
    SMACK: ...
    BOING: ...
    BOO: ...
    UH_OH: ...
    SNORING: ...
    KUNG_FU: ...
    FANFARE: ...
    CRUNCHING: ...
    MAGIC_WAND: ...
    LAUGHING_1: ...
    LEFT: ...
    BACKWARDS: ...
    RIGHT: ...
    OBJECT: ...
    COLOR: ...
    FLASHING: ...
    ERROR: ...
    ERROR_ALARM: ...
    DOWN: ...
    FORWARD: ...
    ACTIVATE: ...
    SEARCHING: ...
    TOUCH: ...
    UP: ...
    ANALYZE: ...
    STOP: ...
    DETECTED: ...
    TURN: ...
    START: ...
    MORNING: ...
    EV3: ...
    GO: ...
    GOOD_JOB: ...
    OKEY_DOKEY: ...
    GOOD: ...
    NO: ...
    THANK_YOU: ...
    YES: ...
    GAME_OVER: ...
    OKAY: ...
    SORRY: ...
    BRAVO: ...
    GOODBYE: ...
    HI: ...
    HELLO: ...
    MINDSTORMS: ...
    LEGO: ...
    FANTASTIC: ...
    SPEED_IDLE: ...
    SPEED_DOWN: ...
    SPEED_UP: ...
    BROWN: ...
    GREEN: ...
    BLACK: ...
    WHITE: ...
    RED: ...
    BLUE: ...
    YELLOW: ...
    TICK_TACK: ...
    HORN_1: ...
    BACKING_ALERT: ...
    MOTOR_IDLE: ...
    AIR_RELEASE: ...
    AIR: ...
    BRAKE: ...
    RATCHET: ...
    MOTOR_STOP: ...
    HORN_2: ...
    LASER: ...
    SONAR: ...
    MOTOR_START: ...
    INSECT_BUZZ_2: ...
    ELEPHANT_CALL: ...
    SNAKE_HISS: ...
    DOG_BARK_2: ...
    DOG_WHINE: ...
    INSECT_BUZZ_1: ...
    DOG_SNIFF: ...
    T_REX_ROAR: ...
    INSECT_CHIRP: ...
    DOG_GROWL: ...
    SNAKE_RATTLE: ...
    DOG_BARK_1: ...
    CAT_PURR: ...
    ZERO: ...
    ONE: ...
    TWO: ...
    THREE: ...
    FOUR: ...
    FIVE: ...
    SIX: ...
    SEVEN: ...
    EIGHT: ...
    NINE: ...
    TEN: ...
    READY: ...
    CONFIRM: ...
    GENERAL_ALERT: ...
    CLICK: ...
    OVERPOWER: ...
