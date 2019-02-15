# constants definitions

WRAPPER_IP = "127.0.0.1"
WRAPPER_PORT = 60005

# switch to get a different approach
PYTHON_MODEL = 0
HARDWARE_INTERFACE = 1

COLLECTIVE_SELECTIVE_MODE = 1

# fault paramters
FAULT_EMERGENCY_STOP = 0x1
FAULT_POSITION_FAULT = 0x2
FAULT_US_DS_FAULT = 0x3
FAULT_EXTERNAL_FAULT = 0x4
FAULT_CAN_BUS_PORT = 0x5
FAULT_4BS = 0x6
FAULT_FLAG = 0x7
FAULT_CONTACTOR_FEEDBACK = 0x8
FAULT_OPENING_FAULT = 0x9
FAULT_DOOR_CONTACT_BRIDGE = 0xa
FAULT_SAFETY_OPEN = 0xb
FAULT_OVERLOAD = 0xc
OVER_HEAT = 0xd
LOCK_ERROR = 0xe
FAULT_FULL_LOAD = 0xf
FAULT_DOOR_PHOTOCELL = 0x10
FAULT_FOSS_FAULT = 0x11
FAULT_OVER_CURRENT = 0x12
FAULT_FIRE_DETECTION = 0x13
FAULT_LIFT_OFF = 0x14
FAULT_CAR_PHASE_LOSE = 0x15
FAULT_DOOR_OPEN = 0x16
FAULT_ENCODER_FAULT = 0x17
FAULT_POWER_WEAK = 0x18
FAULT_SPDZ_UNDEFINED = 0x39
FAULT_SPDZ_INACTIVE = 0x3a

# lift status parameters
LIFT_STAT_FAULT = 0x0
LIFT_STAT_READY = 0x1
LIFT_STAT_LOW_UP = 0x2
LIFT_STAT_LOW_DOWN = 0x3
LIFT_STAT_DOOR_CLOSE = 0x4
LIFT_STAT_DOOR_OPEN = 0x5
LIFT_STAT_HIGH_UP = 0x6
LIFT_STAT_HIGH_DOWN = 0x7
LIFT_STAT_RELEVEL_UP = 0x8
LIFT_STAT_RELEVEL_DOWN = 0x9
LIFT_STAT_DIRECTION = 0xa
LIFT_STAT_SPEED_SELECT = 0xb
LIFT_STAT_BLINK = 0xc
LIFT_STAT_LEVEL_SET = 0xd
LIFT_STAT_EVACUATION = 0xf
LIFT_STAT_DEEP_STANDBY = 0x10
LIFT_STAT_REVISION = 0x1
LIFT_STAT_REVISION_UP = 0x2
LIFT_STAT_REVISION_DOWN = 0x3
LIFT_STAT_REVISION_DC = 0x4
LIFT_STAT_REVISION_DO = 0x5

# mode
ELV_MODE_NORMAL = 0x1
ELV_MODE_REVISION = 0x2
ELV_MODE_CORRECTION = 0x3
ELV_MODE_LEARN = 0x4
ELV_MODE_LEVEL_SET = 0x5
ELV_MODE_LIFTER = 0x6
ELEVATOR_DEFAULT_MODE = ELV_MODE_NORMAL

# directions
ELV_DIR_NONE = 0x0
ELV_DIR_UP = 0x1
ELV_DIR_DOWN = 0x2

# Common Parameters
ELEVATOR_CALL = 0x0
ELEVATOR_NO_CALL = 0xff
SERVER_COMMUNICATION_INTERVAL = 0.2  # seconds
MAX_FLOORS = 0x30
MAX_ELEVATORS = 0x8

# Python Model Parameters
PYTHON_MODEL_NUMBER_OF_ELEVATORS = 0x8
PYTHON_MODEL_MAX_FLOORS = 0x10

# Hardware Interface Parameters
#SERIAL_PORT_NUMBER = "/dev/ttyUSB0"
SERIAL_PORT_NUMBER = "/dev/ttyS0"
SERIAL_BAUD_RATE = 128000
SERIAL_DUMMY_SEND_VALUE = 0x32  # used to empty main board buffer
SERIAL_OP_MONITOR = 0x2
SERIAL_OP_ORDER = 0x3
SERIAL_OP_SETTING = 0x4
STAGE_WRITE_SETTING = 0x10
STAGE_READ_SETTING = 0x20
SERIAL_REQ_FRAME_COUNT0_BYTE = 0x3
SERIAL_REQ_FRAME_COUNT1_BYTE = 0x4
SERIAL_BOARD_FRAME_COUNT0_BYTE = 0x26
SERIAL_BOARD_FRAME_COUNT1_BYTE = 0x27
SERIAL_BUFFER_SIZE = 0x28
SERIAL_READ_TIMEOUT = 1  # seconds
SERIAL_WRITE_WAIT = 0.2  # TODO: find the correct value for this
SERIAL_STAGE_BYTE = 0x0
SERIAL_OP_BYTE = 0x1
SERIAL_ID_BYTE = 0x2
SERIAL_CALL_REG0_BYTE = 0x20
SERIAL_DEFAULT_VALUE = 0x00  # or -1??
SERIAL_MSG_SIZE_U16 = 0x13
BOARD_CONNECTION_MAX_TRY = SERIAL_BUFFER_SIZE * 4

LEARN_BIT = 0x40
STAGE_CLEAR_FAULT = 0x01
STAGE_CNTR_RST = 0x02
