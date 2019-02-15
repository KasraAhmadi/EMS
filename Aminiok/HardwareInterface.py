# Serial Communication Program with Main Board

import serial
import time
import Constants
# import ColorSubmit

# color = ColorSubmit.ColorSubmit()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class HardwareInterface:
    __metaclass__ = Singleton
    # try:
    ser = serial.Serial(Constants.SERIAL_PORT_NUMBER, Constants.SERIAL_BAUD_RATE, timeout=Constants.SERIAL_READ_TIMEOUT)
    # color.ChangeSharedPref("Physical","True")

    # except Exception as e:
    #  color.ChangeSharedPref("Physical","False")
    # #pass    # TODO: Omit this and uncomment above line

    def __init__(self):
        print('Hardware Interface Class was Invoked')

    def flush_buffers(self):
        self.ser.flushInput()
        self.ser.flushOutput()

    def reconnect_to_board(self):
        self.flush_buffers()

        dummy_value = bytearray([Constants.SERIAL_DUMMY_SEND_VALUE])
        write_counter = 0

        # while write_counter < 40:
        while True:

            print 'trying to connect to board', write_counter
            self.send_msg_to_board(dummy_value)

            time.sleep(Constants.SERIAL_WRITE_WAIT)
            write_counter += 1

            bytes_to_read = self.ser.in_waiting
            self.read_msg_from_board()      # isn't this extra?

            if bytes_to_read != 0:
                print('Connected to Board!')
                self.read_msg_from_board()  # flush or read?
                break

            if write_counter > Constants.BOARD_CONNECTION_MAX_TRY:
                return False

        return True

    def send_msg_to_board(self, msg):

        self.ser.write(self.byte_array_to_str(msg))
        time.sleep(Constants.SERIAL_WRITE_WAIT)

    def read_msg_from_board(self):

        bytes_to_read = self.ser.in_waiting

        if bytes_to_read != Constants.SERIAL_BUFFER_SIZE:
            # color.ChangeSharedPref("Physical","False")
            print 'Data was not Received Completely'
            self.ser.read(bytes_to_read)
            return ""

        else:
            # color.ChangeSharedPref("Physical","True")
            return self.ser.read(Constants.SERIAL_BUFFER_SIZE)

    def get_elv_count(self):

        elv_count = 0

        for i in range(Constants.MAX_ELEVATORS):
            if self.check_if_alive(i + 1):
                elv_count += 1

        return elv_count

    def check_if_alive(self, elv_id):

        msg = bytearray(40)
        msg[Constants.SERIAL_STAGE_BYTE] = 0x1   # TODO: find out how stage works
        msg[Constants.SERIAL_OP_BYTE] = Constants.SERIAL_OP_MONITOR
        msg[Constants.SERIAL_ID_BYTE] = elv_id + 16  # for some reasons id starts from 17

        self.send_msg_to_board(msg)

        msg = self.read_msg_from_board()
        msg_u16 = self.msg_to_u16(msg)

        return self.is_msg_valid(msg_u16)

    @staticmethod
    def is_msg_valid(msg_u16):
        elv_id = msg_u16[3]
        elv_id &= 15  # b1111 since id is 4 bits

        if 0 < elv_id < 9:
            return True
        return False

    @staticmethod
    def msg_to_u16(byte_msg):

        main_message_u16 = [0] * Constants.SERIAL_MSG_SIZE_U16  # can use range(x) too

        msg_counter = 0
        for i in range(Constants.SERIAL_MSG_SIZE_U16):
            first_byte = ord(byte_msg[msg_counter])
            second_byte = ord(byte_msg[msg_counter+1])

            main_message_u16[i] = second_byte
            main_message_u16[i] <<= 8
            main_message_u16[i] |= first_byte

            msg_counter += 2

        return main_message_u16

    @staticmethod
    def setting_mst_to_u16(byte_msg):

        u16_size = len(byte_msg) / 2

        main_message_u16 = [0] * u16_size  # can use range(x) too
        msg_counter = 0
        for i in range(u16_size):
            first_byte = ord(byte_msg[msg_counter])
            second_byte = ord(byte_msg[msg_counter+1])

            main_message_u16[i] = second_byte
            main_message_u16[i] <<= 8
            main_message_u16[i] |= first_byte

            msg_counter += 2

        return main_message_u16

    @staticmethod
    def u16_to_msg_byte(message_u16, u16_size):
        msg_byte = []  # can use range(x) too
        for i in range(u16_size):
            first_byte = (message_u16[i]) & 0xff
            msg_byte.append(first_byte)

            second_byte = (message_u16[i]) >> 8
            msg_byte.append(second_byte)

        return msg_byte

    @staticmethod
    def byte_array_to_str(arr_input):
        return ''.join(map(chr, arr_input))
