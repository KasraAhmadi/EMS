# Class for Elevator Parameters

import math
import Constants
import json
from HardwareInterface import HardwareInterface


class ElevatorParams:

    # *************** Settings **************** #
    setting_msg_byte = []
    setting_msg_u16 = []
    # Main Setting
    s_floor_number = Constants.SERIAL_DEFAULT_VALUE
    s_system_type = Constants.SERIAL_DEFAULT_VALUE
    s_bottom_floor = Constants.SERIAL_DEFAULT_VALUE
    s_service_type = Constants.SERIAL_DEFAULT_VALUE
    s_load_level_value = Constants.SERIAL_DEFAULT_VALUE
    s_do_limit_switch = Constants.SERIAL_DEFAULT_VALUE
    s_dc_limit_switch = Constants.SERIAL_DEFAULT_VALUE
    s_adv_door_opening = Constants.SERIAL_DEFAULT_VALUE
    s_park_status = Constants.SERIAL_DEFAULT_VALUE
    s_park_floor = Constants.SERIAL_DEFAULT_VALUE
    s_fire_park_floor = Constants.SERIAL_DEFAULT_VALUE
    s_car_call_mode = Constants.SERIAL_DEFAULT_VALUE
    s_hall_call_mode = Constants.SERIAL_DEFAULT_VALUE
    s_car_capacity = Constants.SERIAL_DEFAULT_VALUE
    s_elv_test = Constants.SERIAL_DEFAULT_VALUE
    s_elv_test_value = Constants.SERIAL_DEFAULT_VALUE
    s_segment_blink = Constants.SERIAL_DEFAULT_VALUE
    s_energy_saving = Constants.SERIAL_DEFAULT_VALUE
    s_double_door = Constants.SERIAL_DEFAULT_VALUE
    s_eva_direct = Constants.SERIAL_DEFAULT_VALUE
    s_flag_zone = Constants.SERIAL_DEFAULT_VALUE
    s_car_lowsdp_blink = Constants.SERIAL_DEFAULT_VALUE
    s_audio_music = Constants.SERIAL_DEFAULT_VALUE
    s_audio_announce = Constants.SERIAL_DEFAULT_VALUE
    s_service_call = Constants.SERIAL_DEFAULT_VALUE
    s_service_call_days = Constants.SERIAL_DEFAULT_VALUE
    s_serviceman_phone = "00"       # or maybe 14 bytes?
    s_counter_reset = Constants.SERIAL_DEFAULT_VALUE
    s_factory_default = Constants.SERIAL_DEFAULT_VALUE

    # Floor Setting
    s_select_floor = Constants.SERIAL_DEFAULT_VALUE
    s_collect_type = []
    s_numerator_code_seg1 = []
    s_numerator_code_seg2 = []
    s_door_type = []
    s_door_park_mode = []
    s_door_action = []
    s_hall_call = []
    s_car_call = []
    s_motion_detector = []
    s_level_position = []
    s_code_segment = []

    # Time Setting
    s_car_light_time = Constants.SERIAL_DEFAULT_VALUE
    s_park_time = Constants.SERIAL_DEFAULT_VALUE
    s_door_open_time = Constants.SERIAL_DEFAULT_VALUE
    s_door_close_time = Constants.SERIAL_DEFAULT_VALUE
    s_travel_time = Constants.SERIAL_DEFAULT_VALUE
    s_lock_debouncer = Constants.SERIAL_DEFAULT_VALUE
    s_cont_debouncer = Constants.SERIAL_DEFAULT_VALUE
    s_passenger_time = Constants.SERIAL_DEFAULT_VALUE
    s_car_acc_time = Constants.SERIAL_DEFAULT_VALUE
    s_hlf_vlt_brk_time = Constants.SERIAL_DEFAULT_VALUE
    s_up_stop_delay = Constants.SERIAL_DEFAULT_VALUE
    s_down_stop_delay = Constants.SERIAL_DEFAULT_VALUE
    s_eva_start_delay = Constants.SERIAL_DEFAULT_VALUE
    s_eva_run_delay = Constants.SERIAL_DEFAULT_VALUE
    s_pot1_on_time = Constants.SERIAL_DEFAULT_VALUE
    s_pot1_off_time = Constants.SERIAL_DEFAULT_VALUE
    s_energy_saving_on = Constants.SERIAL_DEFAULT_VALUE
    s_energy_saving_off = Constants.SERIAL_DEFAULT_VALUE
    s_announce_delay = Constants.SERIAL_DEFAULT_VALUE
    s_lock_mgnt_delay = Constants.SERIAL_DEFAULT_VALUE
    s_encoder_check_start = Constants.SERIAL_DEFAULT_VALUE
    s_encoder_check_per = Constants.SERIAL_DEFAULT_VALUE
    s_lift_init_start = Constants.SERIAL_DEFAULT_VALUE
    s_lift_deep_sleep = Constants.SERIAL_DEFAULT_VALUE
    s_sunday = Constants.SERIAL_DEFAULT_VALUE
    s_sunday_on = Constants.SERIAL_DEFAULT_VALUE
    s_sunday_off = Constants.SERIAL_DEFAULT_VALUE
    s_monday = Constants.SERIAL_DEFAULT_VALUE
    s_monday_on = Constants.SERIAL_DEFAULT_VALUE
    s_monday_off = Constants.SERIAL_DEFAULT_VALUE
    s_tuesday = Constants.SERIAL_DEFAULT_VALUE
    s_tuesday_on = Constants.SERIAL_DEFAULT_VALUE
    s_tuesday_off = Constants.SERIAL_DEFAULT_VALUE
    s_wednesday = Constants.SERIAL_DEFAULT_VALUE
    s_wednesday_on = Constants.SERIAL_DEFAULT_VALUE
    s_wednesday_off = Constants.SERIAL_DEFAULT_VALUE
    s_thursday = Constants.SERIAL_DEFAULT_VALUE
    s_thursday_on = Constants.SERIAL_DEFAULT_VALUE
    s_thursday_off = Constants.SERIAL_DEFAULT_VALUE
    s_friday = Constants.SERIAL_DEFAULT_VALUE
    s_friday_on = Constants.SERIAL_DEFAULT_VALUE
    s_friday_off = Constants.SERIAL_DEFAULT_VALUE
    s_saturday = Constants.SERIAL_DEFAULT_VALUE
    s_saturday_on = Constants.SERIAL_DEFAULT_VALUE
    s_saturday_off = Constants.SERIAL_DEFAULT_VALUE
    # Speed Setting
    s_used_speeds = Constants.SERIAL_DEFAULT_VALUE
    s_lvl_bin_out = Constants.SERIAL_DEFAULT_VALUE
    s_low_bin_out = Constants.SERIAL_DEFAULT_VALUE
    s_rev_bin_out = Constants.SERIAL_DEFAULT_VALUE
    s_full_bin_out = s_full_acc = s_full_decc = Constants.SERIAL_DEFAULT_VALUE
    s_v1_bin_out = s_v1_acc = s_v1_decc = Constants.SERIAL_DEFAULT_VALUE
    s_v2_bin_out = s_v2_acc = s_v2_decc = Constants.SERIAL_DEFAULT_VALUE
    s_v3_bin_out = s_v3_acc = s_v3_decc = Constants.SERIAL_DEFAULT_VALUE
    s_v4_bin_out = s_v4_acc = s_v4_decc = Constants.SERIAL_DEFAULT_VALUE

    # Learn Setup
    s_motor_type = Constants.SERIAL_DEFAULT_VALUE
    s_suspension = Constants.SERIAL_DEFAULT_VALUE
    s_enc_pulse = Constants.SERIAL_DEFAULT_VALUE
    s_enc_filter = Constants.SERIAL_DEFAULT_VALUE
    s_gear_ratio = Constants.SERIAL_DEFAULT_VALUE
    s_sheave_diameter = Constants.SERIAL_DEFAULT_VALUE
    s_low_speed_val = Constants.SERIAL_DEFAULT_VALUE
    s_flags_dls_to_ds = Constants.SERIAL_DEFAULT_VALUE
    s_flgs_uls_to_us = Constants.SERIAL_DEFAULT_VALUE
    s_correction_mode = Constants.SERIAL_DEFAULT_VALUE
    s_learn_button = Constants.SERIAL_DEFAULT_VALUE

    # fixed inputs Setting
    s_ph1i = s_ph2i = s_ph3i = s_doi = s_dci = s_oli = s_fli \
        = s_lfi = s_cncli = s_olsi = s_clsi = Constants.SERIAL_DEFAULT_VALUE

    # programmable inputs Setting
    s_progin1 = s_progin2 = s_progin3 = s_progin4 = s_progin5 = s_progin6 \
        = s_progin7 = s_progin8 = s_progin9 = s_progin10 = Constants.SERIAL_DEFAULT_VALUE
    # normally open/close
    s_pi1 = s_pi2 = s_pi3 = s_pi4 = s_pi5 = s_pi6 = s_pi7 = s_pi8 \
        = s_pi9 = s_pi10 = Constants.SERIAL_DEFAULT_VALUE

    # programmable outputs Setting
    s_progout1 = s_progout2 = s_progout3 = s_progout4 = s_progout5 = s_progout6 \
        = s_progout7 = s_progout8 = s_progout9 = s_progout10 = s_progout11 \
        = s_progout12 = s_progout13 = s_progout14 = s_progout15 = s_progout16 \
        = s_progout17 = Constants.SERIAL_DEFAULT_VALUE
    # normally open/close
    s_pocontact1 = s_pocontact2 = s_pocontact3 = s_pocontact4 = s_pocontact5 = s_pocontact6 = s_pocontact7 \
        = s_pocontact8 = s_pocontact9 = s_pocontact10 = s_pocontact11 = s_pocontact12 = s_pocontact13 = s_pocontact14 \
        = s_pocontact15 = s_pocontact16 = s_pocontact17 = Constants.SERIAL_DEFAULT_VALUE

    # Fault Setting
    s_e3_fault = s_e4_fault = s_e5_fault = s_e6_fault = s_e7_fault = s_e8_fault \
        = s_fl_fault = s_ol_fault = s_oh_fault = s_ph_fault = s_pf_fault \
        = s_oc_fault = s_fi_fault = s_fe_fault = s_clear_fault = Constants.SERIAL_DEFAULT_VALUE

    # ******************** Monitor *************************** #

    #used when serial connection is broken
    hasErrorB = 0
    # used for filtering fault
    elv_perv_fault = 0x00

    # status
    elv_id = Constants.SERIAL_DEFAULT_VALUE
    elv_lift_stat = Constants.SERIAL_DEFAULT_VALUE
    elv_correction = Constants.SERIAL_DEFAULT_VALUE
    elv_learn = Constants.SERIAL_DEFAULT_VALUE
    elv_auto_rev = Constants.SERIAL_DEFAULT_VALUE
    elv_lift_fault = Constants.SERIAL_DEFAULT_VALUE
    elv_up_move = Constants.SERIAL_DEFAULT_VALUE
    elv_down_move = Constants.SERIAL_DEFAULT_VALUE
    elv_car_position = Constants.SERIAL_DEFAULT_VALUE
    elv_floor = Constants.SERIAL_DEFAULT_VALUE
    elv_write_call_key = Constants.SERIAL_DEFAULT_VALUE
    elv_read_call_key = Constants.SERIAL_DEFAULT_VALUE
    elv_clear_call_key = Constants.SERIAL_DEFAULT_VALUE
    elv_read_rtc = Constants.SERIAL_DEFAULT_VALUE
    elv_write_up_call = Constants.SERIAL_DEFAULT_VALUE
    elv_write_down_call = Constants.SERIAL_DEFAULT_VALUE
    elv_tris_call_enable = Constants.SERIAL_DEFAULT_VALUE
    elv_slave_enable = Constants.SERIAL_DEFAULT_VALUE
    elv_lvl_active = Constants.SERIAL_DEFAULT_VALUE
    elv_lifter_active = Constants.SERIAL_DEFAULT_VALUE
    elv_constant_error = Constants.SERIAL_DEFAULT_VALUE
    elv_car_call_clear = Constants.SERIAL_DEFAULT_VALUE
    elv_des_call_load = Constants.SERIAL_DEFAULT_VALUE

    # inputs
    elv_in1 = elv_in2 = elv_in3 = elv_in4 = elv_in5 = elv_in6 \
        = elv_in7 = elv_in8 = elv_in9 = elv_in10 = Constants.SERIAL_DEFAULT_VALUE
    elv_i411 = elv_i419 = elv_i419a = elv_i420 = elv_i401 = elv_i400a\
        = elv_i402 = elv_i403 = elv_i410 = elv_i405 = elv_i406 = elv_i407\
        = elv_iptc = elv_ilvl = elv_i404 = elv_istp = elv_idc = elv_iph1\
        = elv_iol = elv_ifl = elv_ilf = elv_iph2 = elv_iph3 = elv_icl = elv_ios\
        = elv_ics = elv_ido = elv_ic4 = elv_ok = Constants.SERIAL_DEFAULT_VALUE

    # outputs
    elv_upr = elv_dnr = elv_hir = elv_lor = elv_mdr = elv_rcr = elv_dcr = elv_do1r\
        = elv_light = elv_flt = elv_do2r = elv_lvlo = elv_do3r = elv_ane = elv_msc\
        = elv_po17r = elv_a1 = elv_b1 = elv_c1 = elv_d1 = elv_e1 = elv_f1 = elv_g1\
        = elv_ual = elv_a2 = elv_b2 = elv_c2 = elv_d2 = elv_e2 = elv_f2 = elv_g2\
        = elv_dal = elv_po1r = elv_po2r = elv_po3r = elv_po4r = elv_po5r = elv_po6r\
        = elv_po7r = elv_po8r = elv_po9r = elv_po10r = elv_po11r = elv_po12r = elv_po13r\
        = elv_po14r = elv_po15r = elv_po16r = Constants.SERIAL_DEFAULT_VALUE

    # calls
    elv_call_car = []
    elv_call_car_byte = []
    elv_call_hall_up = []
    elv_call_hall_down = []

    # misc
    elv_mode = Constants.ELEVATOR_DEFAULT_MODE
    elv_numerator_segment1 = ""
    elv_numerator_segment2 = ""
    elv_numerator_concat = ""
    elv_numerator_down = 0
    elv_numerator_up = 0
    elv_direction = 0
    mainMessage = bytearray(40)

    def __init__(self):

        print("Elevator Parameters Class was Invoked")

        for i in range(Constants.MAX_FLOORS / 8):
            self.elv_call_car_byte.append(Constants.ELEVATOR_NO_CALL)

        # initialize floor setting parameters
        for i in range(Constants.MAX_FLOORS):
            self.s_collect_type.append(Constants.ELEVATOR_NO_CALL)
            self.s_numerator_code_seg1.append(Constants.ELEVATOR_NO_CALL)
            self.s_numerator_code_seg2.append(Constants.ELEVATOR_NO_CALL)
            self.s_door_type.append(Constants.ELEVATOR_NO_CALL)
            self.s_door_park_mode.append(Constants.ELEVATOR_NO_CALL)
            self.s_door_action.append(Constants.ELEVATOR_NO_CALL)
            self.s_hall_call.append(Constants.ELEVATOR_NO_CALL)
            self.s_car_call.append(Constants.ELEVATOR_NO_CALL)
            self.s_motion_detector.append(Constants.ELEVATOR_NO_CALL)
            self.s_level_position.append(Constants.ELEVATOR_NO_CALL)
            self.s_code_segment.append(Constants.ELEVATOR_NO_CALL)

    def monitor_elevator(self, elv_id):
        self.mainMessage[Constants.SERIAL_STAGE_BYTE] = 0x1
        self.mainMessage[Constants.SERIAL_OP_BYTE] = Constants.SERIAL_OP_MONITOR
        self.mainMessage[Constants.SERIAL_ID_BYTE] = elv_id + 16  # for some reasons id starts from 17

        for i in range(Constants.MAX_FLOORS / 8):
            self.mainMessage[Constants.SERIAL_CALL_REG0_BYTE + i] = 0xff  # self.elv_call_car_byte[i]

        hw_interface = HardwareInterface()
        hw_interface.send_msg_to_board(self.mainMessage)
        msg_byte = hw_interface.read_msg_from_board()

        if len(msg_byte) != Constants.SERIAL_BUFFER_SIZE:
	    print "error B"
            self.hasErrorB = 1

        else:
            self.hasErrorB = 0
            msg_u16 = hw_interface.msg_to_u16(msg_byte)

            if not(hw_interface.is_msg_valid(msg_u16)):
                self.hasErrorB = 1
                print 'Invalid Message Received'  # TODO: catch exception

            else:
                self.parse_parameters(msg_u16, elv_id)

                for i in range(Constants.MAX_FLOORS / 8):
                    self.elv_call_car_byte[i] = msg_byte[Constants.SERIAL_CALL_REG0_BYTE + i]
    def control_elevator(self, elv_id, floor_num):

        self.mainMessage[Constants.SERIAL_STAGE_BYTE] = 0x1
        self.mainMessage[Constants.SERIAL_OP_BYTE] = Constants.SERIAL_OP_ORDER
        self.mainMessage[Constants.SERIAL_ID_BYTE] = elv_id + 16  # for some reasons id starts from 17

        # TODO: should i use previous calls in new command?
        # it seems that new command does not clear previous calls so 0xff should be fine ;)
        for i in range(Constants.MAX_FLOORS / 8):
            self.mainMessage[Constants.SERIAL_CALL_REG0_BYTE + i] = 0xff  # self.elv_call_car_byte[i]

        self.set_floor_control(floor_num)

        hardware_interface = HardwareInterface()
        hardware_interface.send_msg_to_board(self.mainMessage)
        print "data was sent to HW"

        hardware_interface.read_msg_from_board()  # TODO: or just flush buffers
        for i in range(Constants.MAX_FLOORS / 8):
            self.mainMessage[Constants.SERIAL_CALL_REG0_BYTE + 1] = 0xff

        self.mainMessage[Constants.SERIAL_STAGE_BYTE] = 0
        hardware_interface.send_msg_to_board(self.mainMessage)
        hardware_interface.read_msg_from_board()

    def send_read_setting_op(self, elv_id, stage_value, page_num):

        self.mainMessage[Constants.SERIAL_STAGE_BYTE] = stage_value
        self.mainMessage[Constants.SERIAL_OP_BYTE] = Constants.SERIAL_OP_SETTING
        self.mainMessage[Constants.SERIAL_ID_BYTE] = elv_id + 16  # id starts from 17

        for i in range(Constants.MAX_FLOORS / 8):
            self.mainMessage[Constants.SERIAL_CALL_REG0_BYTE + i] = 0xff

        self.mainMessage[Constants.SERIAL_REQ_FRAME_COUNT0_BYTE] = page_num
        self.mainMessage[Constants.SERIAL_REQ_FRAME_COUNT1_BYTE] = 0x00       # TODO: make dynamic

        hw_interface = HardwareInterface()
        hw_interface.send_msg_to_board(self.mainMessage)
        msg_byte = hw_interface.read_msg_from_board()

        if len(msg_byte) != Constants.SERIAL_BUFFER_SIZE:
            return -1  # TODO: Handle Exception
        else:
            return msg_byte

    def read_setting(self, elv_id):
        self.setting_msg_byte = []
        hw_interface = HardwareInterface()

        # wait until receive zero, zero mean that board has received setting read command
        print "wait for zero"
        board_ack = False
        while not board_ack:
            all_zero = True
            msg_byte = self.send_read_setting_op(elv_id, Constants.STAGE_READ_SETTING, 0)
	    if msg_byte != -1:
            	msg_u16 = hw_interface.msg_to_u16(msg_byte)

	        for i in msg_u16:
        		if i != 0x0000:
                		all_zero = False
          	if all_zero:
                		board_ack = True

        # wait for 0xff, 0xff means that board has received parameters from CAN bus
        print "wait for ff"
        board_is_ready = False
        while not board_is_ready:
            all_one = True
            msg_byte = self.send_read_setting_op(elv_id, Constants.STAGE_READ_SETTING, 0)
            msg_u16 = hw_interface.msg_to_u16(msg_byte)
            for i in msg_u16:
                if i != 0xffff:
                    all_one = False
            if all_one:
                board_is_ready = True

        print "start reading setting"
        # start reading setting paramters
        last_frame = False
        frame_count_req = 1
        frame_count = 0
        # while not last_frame:

        for count in range(20):     # 20 to make sure that we receive all the data (not necessary --> alavi's idea)
            msg_byte = self.send_read_setting_op(elv_id, Constants.STAGE_READ_SETTING, frame_count_req)
            frame_count = ord(msg_byte[Constants.SERIAL_BOARD_FRAME_COUNT0_BYTE])   # Count0 -> LSB, Count1 -> MSB
            # msg_u16 = hw_interface.msg_to_u16(msg_byte)  # Temp
            if frame_count == 0xff:
                temp_count = ord(msg_byte[Constants.SERIAL_BOARD_FRAME_COUNT1_BYTE])
                if temp_count == 0xff:
                    last_frame = True
                else:
                    frame_count |= (temp_count << 8)
            if frame_count != frame_count_req and not last_frame:
                print 'requested frame and received frame numbers do not match'

            for i in range(len(msg_byte)):
                if i < Constants.SERIAL_BOARD_FRAME_COUNT0_BYTE:
                    self.setting_msg_byte.append(msg_byte[i])

            frame_count_req += 1

            if last_frame:
                break

        self.setting_msg_u16 = hw_interface.setting_mst_to_u16(self.setting_msg_byte)
        self.parse_setting_params(self.setting_msg_u16)
        return self.build_setting_json(elv_id)

    def write_setting(self, elv_id, json_data):
        print "write setting invoked"
        whole_setting_frame_count = len(self.setting_msg_byte) / 32   # 8 bytes are used for id, op, ...
        whole_setting_frame_count_rem = len(self.setting_msg_byte) % 32
        print "starting parsing json"
        # assign new parameters to msg u16

        self.parse_setting_json(json_data)
        print "starting writing setting params"

        self.write_setting_params()
        print "starting writing setting to board"
        hw_interface = HardwareInterface()
        whole_setting_msg_byte = hw_interface.u16_to_msg_byte(self.setting_msg_u16, len(self.setting_msg_u16))
	print "whole setting msg is ready"
	print len(whole_setting_msg_byte)
        write_setting_msg_frame = [0] * 32  # we send write data in 32 bytes chunks
        write_frame = 1
        for i in range(whole_setting_frame_count):
            for j in range(32):
                write_setting_msg_frame[j] = whole_setting_msg_byte[((write_frame - 1)*32) + j]

            msg_resp = self.send_write_setting_op(elv_id, Constants.STAGE_WRITE_SETTING,
                                                  write_frame, write_setting_msg_frame)
	    print "msg resp"
            print (msg_resp)
            frame_count = ord(msg_resp[Constants.SERIAL_BOARD_FRAME_COUNT0_BYTE])   # Count0 -> LSB, Count1 -> MSB

            if frame_count != write_frame:  # TODO check second byte of frame if first one is 0xff
                print "Error in writing data: sent frame does not match received frame"

            write_frame += 1

        for i in range(whole_setting_frame_count_rem):
            write_setting_msg_frame[i] = whole_setting_msg_byte[((write_frame - 1)*32) + i]

        msg_resp = self.send_write_setting_op(elv_id, Constants.STAGE_WRITE_SETTING,
                                              write_frame, write_setting_msg_frame)
        frame_count = ord(msg_resp[Constants.SERIAL_BOARD_FRAME_COUNT0_BYTE])   # Count0 -> LSB, Count1 -> MSB

        if frame_count != write_frame:  # TODO check second byte of frame if first one is 0xff
            print "Error in writing data: sent frame does not match received frame"
	print "sending last msg"
        # last message inform board that data has finished by sending 0xff
        msg_resp = self.send_write_setting_op(elv_id, Constants.STAGE_WRITE_SETTING, 0xff, write_setting_msg_frame)

    def send_write_setting_op(self, elv_id, stage_value, page_num, msg):

	if self.s_clear_fault:
		print "clear fault received"
		stage_value += Constants.STAGE_CLEAR_FAULT
	if self.s_counter_reset:
		print "counter reset received"
		stage_value += Constants.STAGE_CNTR_RST

        self.mainMessage[Constants.SERIAL_STAGE_BYTE] = stage_value
        self.mainMessage[Constants.SERIAL_OP_BYTE] = Constants.SERIAL_OP_SETTING
        self.mainMessage[Constants.SERIAL_ID_BYTE] = elv_id + 16  # id starts from 17

        msg_index = 8   # previous 8 bytes are id, op, ...
        for i in range(32):  # in each iteration we can send 32 bytes of setting data (8 bytes reserved for id, op, ...)
            self.mainMessage[msg_index] = msg[i]        # TODO: use ord method if a problem encountered
            msg_index += 1

        self.mainMessage[Constants.SERIAL_REQ_FRAME_COUNT0_BYTE] = page_num

        if page_num == 0xff:
            self.mainMessage[Constants.SERIAL_REQ_FRAME_COUNT1_BYTE] = 0xff       # TODO: make dynamic
        else:
            self.mainMessage[Constants.SERIAL_REQ_FRAME_COUNT1_BYTE] = 0x00       # TODO: make dynamic

        hw_interface = HardwareInterface()
        hw_interface.send_msg_to_board(self.mainMessage)
        msg_byte = hw_interface.read_msg_from_board()

        if len(msg_byte) != Constants.SERIAL_BUFFER_SIZE:
            return "\xff"  # TODO: Handle Exception
        else:
            return msg_byte

    def write_setting_params(self):

        # floor setting
        for i in range(Constants.MAX_FLOORS):
            self.set_parameter(self.s_collect_type[i], 4*i,0 , 2)
            self.set_parameter(self.s_numerator_code_seg1[i], 4*i, 2, 5)
            self.set_parameter(self.s_numerator_code_seg2[i], 4*i, 7, 5)
            self.set_parameter(self.s_door_type[i], 4*i, 12, 1)
            self.set_parameter(self.s_door_park_mode[i], 4*i, 13, 1)

            self.set_parameter(self.s_level_position[i], (4*i) + 1, 0, 16)

            self.set_parameter(self.s_hall_call[i], (4*i) + 2, 0, 1)
            self.set_parameter(self.s_car_call[i], (4*i) + 2, 1, 1)
            self.set_parameter(self.s_motion_detector[i], (4*i) + 2, 2, 1)
            self.set_parameter(self.s_door_action[i], (4*i) + 2, 3, 3)
            self.set_parameter(self.s_code_segment[i], (4*i) + 2, 6, 7)

        # main setting
        offset = 192    # offset for EPROM setting parameters

        self.set_parameter(self.s_floor_number, offset + 41, 0, 6)
        self.set_parameter(self.s_system_type, offset + 51, 9, 4)
        self.set_parameter(self.s_bottom_floor, offset + 52, 10, 6)
        self.set_parameter(self.s_service_type, offset + 34, 14, 1)
        self.set_parameter(self.s_do_limit_switch, offset + 33, 15, 1)
        self.set_parameter(self.s_dc_limit_switch, offset + 33, 14, 1)
        self.set_parameter(self.s_adv_door_opening, offset + 40, 0, 6)
        self.set_parameter(self.s_park_status, offset + 49, 13, 1)
        self.set_parameter(self.s_park_floor, offset + 47, 6, 6)
        self.set_parameter(self.s_fire_park_floor, offset + 47, 0, 6)
        self.set_parameter(self.s_car_call_mode, offset + 44, 14, 2)
        self.set_parameter(self.s_hall_call_mode, offset + 51, 13, 2)
        self.set_parameter(self.s_car_capacity, offset + 43, 10, 6)
        self.set_parameter(self.s_elv_test, offset + 55, 6, 2)
        self.set_parameter(self.s_segment_blink, offset + 35, 15, 1)
        self.set_parameter(self.s_energy_saving, offset + 35, 14, 1)
        self.set_parameter(self.s_double_door, offset + 57, 0, 1)
        self.set_parameter(self.s_eva_direct, offset + 57, 14, 1)
        self.set_parameter(self.s_flag_zone, offset + 58,  8, 7)
        self.set_parameter(self.s_car_lowsdp_blink, offset + 58, 15, 1)
        self.set_parameter(self.s_audio_music, offset + 24, 15, 1)
        self.set_parameter(self.s_audio_announce, offset + 24, 14, 1)
	self.set_parameter((self.s_elv_test_value & 0xff), offset + 55, 8, 8)
	self.set_parameter((self.s_elv_test_value >> 8), offset + 56, 0, 16)
	self.set_parameter((self.s_service_call), offset + 22, 0, 16)
	self.set_parameter((self.s_service_call_days), offset + 54, 0, 8)

        # time setting
        self.set_parameter(self.s_car_light_time, offset + 42, 0, 8)
        self.set_parameter(self.s_park_time, offset + 42, 8, 8)
        self.set_parameter(self.s_door_open_time, offset + 48, 9, 7)
        self.set_parameter(self.s_door_close_time, offset + 37, 0, 7)
        self.set_parameter(self.s_travel_time, offset + 38, 6, 10)
        self.set_parameter(self.s_lock_debouncer, offset + 41, 6, 5)
        self.set_parameter(self.s_cont_debouncer, offset + 41, 11, 5)
        self.set_parameter(self.s_passenger_time, offset + 38,  0, 6)
        self.set_parameter(self.s_car_acc_time, offset + 57, 1, 6)
        self.set_parameter(self.s_hlf_vlt_brk_time, offset + 49, 1, 5)
        self.set_parameter(self.s_up_stop_delay, offset + 45, 6, 6)
        self.set_parameter(self.s_down_stop_delay, offset + 49, 6, 6)
        self.set_parameter(self.s_eva_start_delay, offset + 55, 0, 6)
        self.set_parameter(self.s_eva_run_delay, offset + 53, 11, 5)
        self.set_parameter(self.s_pot1_on_time, offset + 40, 6, 5)
        self.set_parameter(self.s_pot1_off_time, offset + 40, 11, 5)
        self.set_parameter(self.s_energy_saving_on, offset + 43, 0, 5)
        self.set_parameter(self.s_energy_saving_off, offset + 43, 5, 5)
        self.set_parameter(self.s_announce_delay, offset + 50, 4, 4)
        self.set_parameter(self.s_lock_mgnt_delay, offset + 50, 0, 4)
        self.set_parameter(self.s_encoder_check_start, offset + 54, 8, 4)
        self.set_parameter(self.s_encoder_check_per, offset + 54, 12, 4)
        self.set_parameter(self.s_lift_init_start, offset + 57, 8, 6)
        self.set_parameter(self.s_lift_deep_sleep, offset + 58,  0, 8)
        self.set_parameter(self.s_sunday, offset, 0, 16)
        self.set_parameter(self.s_monday, offset + 1, 0, 16)
        self.set_parameter(self.s_tuesday, offset + 2, 0, 16)
        self.set_parameter(self.s_wednesday, offset + 3, 0, 16)
        self.set_parameter(self.s_thursday, offset + 4, 0, 16)
        self.set_parameter(self.s_friday, offset + 5, 0, 16)
        self.set_parameter(self.s_saturday, offset + 6, 0, 16)

        #  speed setting
        self.set_parameter(self.s_used_speeds, offset + 45, 12 , 4)
        self.set_parameter(self.s_lvl_bin_out, offset + 36, 7, 3)
        self.set_parameter(self.s_low_bin_out, offset + 36, 10, 3)
        self.set_parameter(self.s_rev_bin_out, offset + 36, 13, 3)
        self.set_parameter(self.s_full_bin_out, offset + 37, 7, 3)
        self.set_parameter(self.s_v1_bin_out, offset + 37, 10, 3)
        self.set_parameter(self.s_v2_bin_out, offset + 37, 13, 3)
        self.set_parameter(self.s_v3_bin_out, offset + 48, 0, 3)
        self.set_parameter(self.s_v4_bin_out, offset + 48, 3, 3)
        self.set_parameter(self.s_full_acc, offset + 9, 0, 16)
        self.set_parameter(self.s_full_decc, offset + 10, 0, 16)
        self.set_parameter(self.s_v1_acc, offset + 11, 0, 16)
        self.set_parameter(self.s_v1_decc, offset + 12, 0, 16)
        self.set_parameter(self.s_v2_acc, offset + 13, 0, 16)
        self.set_parameter(self.s_v2_decc, offset + 14, 0, 16)
        self.set_parameter(self.s_v3_acc, offset + 15, 0, 16)
        self.set_parameter(self.s_v3_decc, offset + 16, 0, 16)
        self.set_parameter(self.s_v4_acc, offset + 17, 0, 16)
        self.set_parameter(self.s_v4_decc, offset + 18, 0, 16)

        # learn setting
        self.set_parameter(self.s_motor_type, offset + 47, 15, 1)
        self.set_parameter(self.s_suspension, offset + 48, 7, 1)
        self.set_parameter(self.s_enc_pulse, offset + 44, 0, 14)
        self.set_parameter(self.s_enc_filter, offset + 47, 12, 3)
        self.set_parameter(self.s_gear_ratio, offset + 46, 10, 6)
        self.set_parameter(self.s_sheave_diameter, offset + 39, 0, 12)
        self.set_parameter(self.s_low_speed_val, offset + 46, 4, 6)
        self.set_parameter(self.s_flags_dls_to_ds, offset + 59, 0, 5)
        self.set_parameter(self.s_flgs_uls_to_us, offset + 59, 5, 5)
        self.set_parameter(self.s_correction_mode, offset + 57, 15, 1)

        # fixed input setting
        self.set_parameter(self.s_ph1i, offset + 53, 1, 1)
        self.set_parameter(self.s_ph2i, offset + 53, 5, 1)
        self.set_parameter(self.s_ph3i, offset + 53, 6, 1)
        self.set_parameter(self.s_doi, offset + 53, 10, 1)
        self.set_parameter(self.s_dci, offset + 53, 0, 1)
        self.set_parameter(self.s_oli, offset + 53, 2, 1)
        self.set_parameter(self.s_fli, offset + 53, 3, 1)
        self.set_parameter(self.s_lfi, offset + 53, 4, 1)
        self.set_parameter(self.s_cncli, offset + 53, 7, 1)
        self.set_parameter(self.s_olsi, offset + 53, 8, 1)
        self.set_parameter(self.s_clsi, offset + 53, 9, 1)

        # programmable input
        self.set_parameter(self.s_progin1, offset + 23, 0, 7)
        self.set_parameter(self.s_progin2, offset + 23, 7, 7)
        self.set_parameter(self.s_progin3, offset + 24, 0, 7)
        self.set_parameter(self.s_progin4, offset + 24, 7, 7)
        self.set_parameter(self.s_progin5, offset + 25, 0, 7)
        self.set_parameter(self.s_progin6, offset + 25, 7, 7)
        self.set_parameter(self.s_progin7, offset + 26, 0, 7)
        self.set_parameter(self.s_progin8, offset + 26, 7, 7)
        self.set_parameter(self.s_progin9, offset + 27, 0, 7)
        self.set_parameter(self.s_progin10, offset + 27, 7, 7)

        self.set_parameter(self.s_pi1, offset + 52, 0, 1)
        self.set_parameter(self.s_pi2, offset + 52, 1, 1)
        self.set_parameter(self.s_pi3, offset + 52, 2, 1)
        self.set_parameter(self.s_pi4, offset + 52, 3, 1)
        self.set_parameter(self.s_pi5, offset + 52, 4, 1)
        self.set_parameter(self.s_pi6, offset + 52, 5, 1)
        self.set_parameter(self.s_pi7, offset + 52, 6, 1)
        self.set_parameter(self.s_pi8, offset + 52, 7, 1)
        self.set_parameter(self.s_pi9, offset + 52, 8, 1)
        self.set_parameter(self.s_pi10, offset + 52, 9, 1)

        # programmable output
        self.set_parameter(self.s_progout1, offset + 28, 0, 7)
        self.set_parameter(self.s_progout2, offset + 28, 7, 7)
        self.set_parameter(self.s_progout3, offset + 29, 0, 7)
        self.set_parameter(self.s_progout4, offset + 29, 7, 7)
        self.set_parameter(self.s_progout5, offset + 30, 0, 7)
        self.set_parameter(self.s_progout6, offset + 30, 7, 7)
        self.set_parameter(self.s_progout7, offset + 31, 0, 7)
        self.set_parameter(self.s_progout8, offset + 31, 7, 7)
        self.set_parameter(self.s_progout9, offset + 32, 0, 7)
        self.set_parameter(self.s_progout11, offset + 32, 7, 7)
        self.set_parameter(self.s_progout11, offset + 33, 0, 7)
        self.set_parameter(self.s_progout12, offset + 33, 7, 7)
        self.set_parameter(self.s_progout13, offset + 34, 0, 7)
        self.set_parameter(self.s_progout14, offset + 34, 7, 7)
        self.set_parameter(self.s_progout15, offset + 35, 0, 7)
        self.set_parameter(self.s_progout16, offset + 35, 7, 7)
        self.set_parameter(self.s_progout17, offset + 36, 0, 7)

        self.set_parameter(self.s_pocontact1, offset + 50, 8, 1)
        self.set_parameter(self.s_pocontact2, offset + 50, 9, 1)
        self.set_parameter(self.s_pocontact3, offset + 50, 10, 1)
        self.set_parameter(self.s_pocontact4, offset + 50, 11, 1)
        self.set_parameter(self.s_pocontact5, offset + 50, 12, 1)
        self.set_parameter(self.s_pocontact6, offset + 50, 13, 1)
        self.set_parameter(self.s_pocontact7, offset + 50, 14, 1)
        self.set_parameter(self.s_pocontact8, offset + 50, 15, 1)
        self.set_parameter(self.s_pocontact9, offset + 51, 0, 1)
        self.set_parameter(self.s_pocontact10, offset + 51, 1, 1)
        self.set_parameter(self.s_pocontact11, offset + 51, 2, 1)
        self.set_parameter(self.s_pocontact12, offset + 51, 3, 1)
        self.set_parameter(self.s_pocontact13, offset + 51, 4, 1)
        self.set_parameter(self.s_pocontact14, offset + 51, 5, 1)
        self.set_parameter(self.s_pocontact15, offset + 51, 6, 1)
        self.set_parameter(self.s_pocontact16, offset + 51, 7, 1)
        self.set_parameter(self.s_pocontact17, offset + 51, 8, 1)

        #fault setting
        self.set_parameter(self.s_e3_fault, offset + 30, 14, 1)
        self.set_parameter(self.s_e4_fault, offset + 30, 15, 1)
        self.set_parameter(self.s_e5_fault, offset + 25, 14, 1)
        self.set_parameter(self.s_e6_fault, offset + 25, 15, 1)
        self.set_parameter(self.s_e7_fault, offset + 26, 14, 1)
        self.set_parameter(self.s_e8_fault, offset + 48, 8, 1)
        self.set_parameter(self.s_fl_fault, offset + 29, 14, 1)
        self.set_parameter(self.s_ol_fault, offset + 29, 15, 1)
        self.set_parameter(self.s_oh_fault, offset + 48, 6, 1)
        self.set_parameter(self.s_ph_fault, offset + 32, 14, 1)
        self.set_parameter(self.s_pf_fault, offset + 32, 15, 1)
        self.set_parameter(self.s_oc_fault, offset + 31, 14, 1)
        self.set_parameter(self.s_fi_fault, offset + 31, 15, 1)
        self.set_parameter(self.s_fe_fault, offset + 51, 15, 1)

        # serviceman phone
        # for i in range(15):  # or maybe 14
            # self.set_parameter(int(self.s_serviceman_phone[i]), 252 + i, 0)

    def enter_learn_mod(self, elv_id):
	learn_bit = self.send_learn_command(elv_id)

	ctr = 0
	#wait until elevator is in learn mod
	while not learn_bit:
		print "waiting to get in learn mod"
		learn_bit = self.send_learn_command(elv_id)
		ctr += 1
		if ctr > 50:
			break

	print "elevator is in learn mod"

    def send_learn_command(self, elv_id):
	self.mainMessage[Constants.SERIAL_STAGE_BYTE] = 0x1
	self.mainMessage[Constants.SERIAL_OP_BYTE] = Constants.SERIAL_OP_ORDER
	self.mainMessage[Constants.SERIAL_ID_BYTE] = 0x10 + elv_id + Constants.LEARN_BIT

	for i in range(3, 40):
		self.mainMessage[i] = 0xff
	hw_interface = HardwareInterface()
	hw_interface.send_msg_to_board(self.mainMessage)
	msg_byte = hw_interface.read_msg_from_board()

	if len(msg_byte) != Constants.SERIAL_BUFFER_SIZE:
		return 0

	msg_u16 = hw_interface.msg_to_u16(msg_byte)

	if not hw_interface.is_msg_valid(msg_u16):
		print "invalid msg received"
		return 0

	return self.get_parameter(msg_u16, 0, 64, 6)


    def parse_setting_params(self, setting_msg_u16):

        # floor setting
        for i in range(Constants.MAX_FLOORS):
            self.s_collect_type[i] = self.get_parameter(setting_msg_u16, 4*i, pow(2, 2) - 1, 0)
            self.s_numerator_code_seg1[i] = self.get_parameter(setting_msg_u16, 4*i, pow(2, 7) - 1, 2)
            self.s_numerator_code_seg2[i] = self.get_parameter(setting_msg_u16, 4*i, pow(2, 12) - 1, 7)
            self.s_door_type[i] = self.get_parameter(setting_msg_u16, 4*i, pow(2, 12), 12)
            self.s_door_park_mode[i] = self.get_parameter(setting_msg_u16, 4*i,  pow(2, 13), 13)
            self.s_level_position[i] = self.get_parameter(setting_msg_u16, (4*i) + 1, -1, 0)
            self.s_hall_call[i] = self.get_parameter(setting_msg_u16, (4*i) + 2, 1, 0)
            self.s_car_call[i] = self.get_parameter(setting_msg_u16, (4*i) + 2, 2, 1)
            self.s_motion_detector[i] = self.get_parameter(setting_msg_u16, (4*i) + 2,  pow(2, 2), 2)
            self.s_door_action[i] = self.get_parameter(setting_msg_u16, (4*i) + 2, pow(2, 6) - 1, 3)
            self.s_code_segment[i] = self.get_parameter(setting_msg_u16, (4*i) + 2,  pow(2, 13) - 1, 6)

        # main setting
        offset = 192    # offset for EPROM setting parameters
        self.s_floor_number = self.get_parameter(setting_msg_u16, offset + 41,  pow(2, 6) - 1, 0)
        print self.s_floor_number
        self.s_system_type = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 13) - 1, 9)
        self.s_bottom_floor = self.get_parameter(setting_msg_u16, offset + 52, - 1, 10)
        self.s_service_type = self.get_parameter(setting_msg_u16, offset + 34,  pow(2, 14), 14)
        self.s_do_limit_switch = self.get_parameter(setting_msg_u16, offset + 33,  pow(2, 15), 15)
        self.s_dc_limit_switch = self.get_parameter(setting_msg_u16, offset + 33,  pow(2, 14), 14)
        self.s_adv_door_opening = self.get_parameter(setting_msg_u16, offset + 40,  pow(2, 6) - 1, 0)
        self.s_park_status = self.get_parameter(setting_msg_u16, offset + 49,  pow(2, 13), 13)
        self.s_park_floor = self.get_parameter(setting_msg_u16, offset + 47,  pow(2, 12) - 1, 6)
        self.s_fire_park_floor = self.get_parameter(setting_msg_u16, offset + 47,  pow(2, 6) - 1, 0)
        self.s_car_call_mode = self.get_parameter(setting_msg_u16, offset + 44,  - 1, 14)
        self.s_hall_call_mode = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 15) - 1, 13)
        self.s_car_capacity = self.get_parameter(setting_msg_u16, offset + 43,  -1, 10)
        self.s_elv_test = self.get_parameter(setting_msg_u16, offset + 55,  pow(2, 8) - 1, 6)
        self.s_segment_blink = self.get_parameter(setting_msg_u16, offset + 35,  -1, 15)
        self.s_energy_saving = self.get_parameter(setting_msg_u16, offset + 35,  pow(2, 15) - 1, 14)
        self.s_double_door = self.get_parameter(setting_msg_u16, offset + 57, 1, 0)
        self.s_eva_direct = self.get_parameter(setting_msg_u16, offset + 57,  pow(2, 15) - 1, 14)
        self.s_flag_zone = self.get_parameter(setting_msg_u16, offset + 58,  pow(2, 15) - 1, 8)
        self.s_car_lowsdp_blink = self.get_parameter(setting_msg_u16, offset + 58,  -1, 15)
        self.s_audio_music = self.get_parameter(setting_msg_u16, offset + 24,  - 1, 15)
        self.s_audio_announce = self.get_parameter(setting_msg_u16, offset + 24,  pow(2, 15) - 1, 14)
	self.s_service_call = self.get_parameter(setting_msg_u16, offset + 22, -1, 0)
	self.s_service_call_days = self.get_parameter(setting_msg_u16, offset + 54, pow(2, 8) - 1, 0)

        # time setting
        self.s_car_light_time = self.get_parameter(setting_msg_u16, offset + 42,  pow(2, 8) - 1, 0)
        self.s_park_time = self.get_parameter(setting_msg_u16, offset + 42, - 1, 8)
        self.s_door_open_time = self.get_parameter(setting_msg_u16, offset + 48,  pow(2, 16) - 1, 9)
        self.s_door_close_time = self.get_parameter(setting_msg_u16, offset + 37,  pow(2, 7) - 1, 0)
        self.s_travel_time = self.get_parameter(setting_msg_u16, offset + 38,  - 1, 6)
        self.s_lock_debouncer = self.get_parameter(setting_msg_u16, offset + 41,  pow(2, 11) - 1, 6)
        self.s_cont_debouncer = self.get_parameter(setting_msg_u16, offset + 41,   - 1, 11)
        self.s_passenger_time = self.get_parameter(setting_msg_u16, offset + 38,  pow(2, 6) - 1, 0)
        self.s_car_acc_time = self.get_parameter(setting_msg_u16, offset + 57,  pow(2, 7) - 1, 1)
        self.s_hlf_vlt_brk_time = self.get_parameter(setting_msg_u16, offset + 49,  pow(2, 6) - 1, 1)
        self.s_up_stop_delay = self.get_parameter(setting_msg_u16, offset + 45,  pow(2, 12) - 1, 6)
        self.s_down_stop_delay = self.get_parameter(setting_msg_u16, offset + 49,  pow(2, 12) - 1, 6)
        self.s_eva_start_delay = self.get_parameter(setting_msg_u16, offset + 55,  pow(2, 6) - 1, 0)
        self.s_eva_run_delay = self.get_parameter(setting_msg_u16, offset + 53,  - 1, 11)
        self.s_pot1_on_time = self.get_parameter(setting_msg_u16, offset + 40,  pow(2, 11) - 1, 6)
        self.s_pot1_off_time = self.get_parameter(setting_msg_u16, offset + 40, - 1, 11)
        self.s_energy_saving_on = self.get_parameter(setting_msg_u16, offset + 43,  pow(2, 5) - 1, 0)
        self.s_energy_saving_off = self.get_parameter(setting_msg_u16, offset + 43,  pow(2, 10) - 1, 5)
        self.s_announce_delay = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 8) - 1, 4)
        self.s_lock_mgnt_delay = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 4) - 1, 0)
        self.s_encoder_check_start = self.get_parameter(setting_msg_u16, offset + 54,  pow(2, 12) - 1, 8)
        self.s_encoder_check_per = self.get_parameter(setting_msg_u16, offset + 54,  - 1, 12)
        self.s_lift_init_start = self.get_parameter(setting_msg_u16, offset + 57,  pow(2, 14) - 1, 8)
        self.s_lift_deep_sleep = self.get_parameter(setting_msg_u16, offset + 58,  pow(2, 8) - 1, 0)
        self.s_sunday = self.get_parameter(setting_msg_u16, offset, - 1, 0)
        self.s_sunday_on = self.get_day_parameter(self.s_sunday, pow(2, 5) - 1, 0)
        self.s_sunday_off = self.get_day_parameter(self.s_sunday, pow(2, 10) - 1, 5)
        self.s_monday = self.get_parameter(setting_msg_u16, offset + 1, - 1, 0)
        self.s_monday_on = self.get_day_parameter(self.s_monday, pow(2, 5) - 1, 0)
        self.s_monday_off = self.get_day_parameter(self.s_monday, pow(2, 10) - 1, 5)
        self.s_tuesday = self.get_parameter(setting_msg_u16, offset + 2,  - 1, 0)
        self.s_tuesday_on = self.get_day_parameter(self.s_tuesday, pow(2, 5) - 1, 0)
        self.s_tuesday_off = self.get_day_parameter(self.s_tuesday, pow(2, 10) - 1, 5)
        self.s_wednesday = self.get_parameter(setting_msg_u16, offset + 3, - 1, 0)
        self.s_wednesday_on = self.get_day_parameter(self.s_wednesday, pow(2, 5) - 1, 0)
        self.s_wednesday_off = self.get_day_parameter(self.s_wednesday, pow(2, 10) - 1, 5)
        self.s_thursday = self.get_parameter(setting_msg_u16, offset + 4, - 1, 0)
        self.s_thursday_on = self.get_day_parameter(self.s_thursday, pow(2, 5) - 1, 0)
        self.s_thursday_off = self.get_day_parameter(self.s_thursday, pow(2, 10) - 1, 5)
        self.s_friday = self.get_parameter(setting_msg_u16, offset + 5, - 1, 0)
        self.s_friday_on = self.get_day_parameter(self.s_friday, pow(2, 5) - 1, 0)
        self.s_friday_off = self.get_day_parameter(self.s_friday, pow(2, 10) - 1, 5)
        self.s_saturday = self.get_parameter(setting_msg_u16, offset + 6, - 1, 0)
        self.s_saturday_on = self.get_day_parameter(self.s_saturday, pow(2, 5) - 1, 0)
        self.s_saturday_off = self.get_day_parameter(self.s_saturday, pow(2, 10) - 1, 5)

        # speed setting
        self.s_used_speeds = self.get_parameter(setting_msg_u16, offset + 45, - 1, 12)
        self.s_lvl_bin_out = self.get_parameter(setting_msg_u16, offset + 36,  pow(2, 10) - 1, 7)
        self.s_low_bin_out = self.get_parameter(setting_msg_u16, offset + 36,  pow(2, 13) - 1, 10)
        self.s_rev_bin_out = self.get_parameter(setting_msg_u16, offset + 36, - 1, 13)
        self.s_full_bin_out = self.get_parameter(setting_msg_u16, offset + 37,  pow(2, 10) - 1, 7)
        self.s_v1_bin_out = self.get_parameter(setting_msg_u16, offset + 37,  pow(2, 13) - 1, 10)
        self.s_v2_bin_out = self.get_parameter(setting_msg_u16, offset + 37, - 1, 13)
        self.s_v3_bin_out = self.get_parameter(setting_msg_u16, offset + 48,  pow(2, 3) - 1, 0)
        self.s_v4_bin_out = self.get_parameter(setting_msg_u16, offset + 48,  pow(2, 6) - 1, 3)
        self.s_full_acc = self.get_parameter(setting_msg_u16, offset + 9, - 1, 0)
        self.s_full_decc = self.get_parameter(setting_msg_u16, offset + 10, -1, 0)
        self.s_v1_acc = self.get_parameter(setting_msg_u16, offset + 11, - 1, 0)
        self.s_v1_decc = self.get_parameter(setting_msg_u16, offset + 12, - 1, 0)
        self.s_v2_acc = self.get_parameter(setting_msg_u16, offset + 13, - 1, 0)
        self.s_v2_decc = self.get_parameter(setting_msg_u16, offset + 14, - 1, 0)
        self.s_v3_acc = self.get_parameter(setting_msg_u16, offset + 15, - 1, 0)
        self.s_v3_decc = self.get_parameter(setting_msg_u16, offset + 16, - 1, 0)
        self.s_v4_acc = self.get_parameter(setting_msg_u16, offset + 17, - 1, 0)
        self.s_v4_decc = self.get_parameter(setting_msg_u16, offset + 18, - 1, 0)

        # learn setting
        self.s_motor_type = self.get_parameter(setting_msg_u16, offset + 47, - 1, 15)
        self.s_suspension = self.get_parameter(setting_msg_u16, offset + 48,  pow(2, 8) - 1, 7)
        self.s_enc_pulse = self.get_parameter(setting_msg_u16, offset + 44,  pow(2, 14) - 1, 0)
        self.s_enc_filter = self.get_parameter(setting_msg_u16, offset + 47,  pow(2, 15) - 1, 12)
        self.s_gear_ratio = self.get_parameter(setting_msg_u16, offset + 46, - 1, 10)
        self.s_sheave_diameter = self.get_parameter(setting_msg_u16, offset + 39,  pow(2, 12) - 1, 0)
        self.s_low_speed_val = self.get_parameter(setting_msg_u16, offset + 46,  pow(2, 10) - 1, 4)
        self.s_flags_dls_to_ds = self.get_parameter(setting_msg_u16, offset + 59,  pow(2, 5) - 1, 0)
        self.s_flgs_uls_to_us = self.get_parameter(setting_msg_u16, offset + 59,  pow(2, 10) - 1, 5)
        self.s_correction_mode = self.get_parameter(setting_msg_u16, offset + 57, - 1, 15)

        # fixed input setting
        self.s_ph1i = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 2) - 1, 1)
        self.s_ph2i = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 6) - 1, 5)
        self.s_ph3i = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 7) - 1, 6)
        self.s_doi = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 11) - 1, 10)
        self.s_dci = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 1) - 1, 0)
        self.s_oli = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 3) - 1, 2)
        self.s_fli = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 4) - 1, 3)
        self.s_lfi = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 5) - 1, 4)
        self.s_cncli = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 8) - 1, 7)
        self.s_olsi = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 9) - 1, 8)
        self.s_clsi = self.get_parameter(setting_msg_u16, offset + 53,  pow(2, 10) - 1, 9)

        # programmable input
        self.s_progin1 = self.get_parameter(setting_msg_u16, offset + 23,  pow(2, 7) - 1, 0)
        self.s_progin2 = self.get_parameter(setting_msg_u16, offset + 23,  pow(2, 14) - 1, 7)
        self.s_progin3 = self.get_parameter(setting_msg_u16, offset + 24,  pow(2, 7) - 1, 0)
        self.s_progin4 = self.get_parameter(setting_msg_u16, offset + 24,  pow(2, 14) - 1, 7)
        self.s_progin5 = self.get_parameter(setting_msg_u16, offset + 25,  pow(2, 7) - 1, 0)
        self.s_progin6 = self.get_parameter(setting_msg_u16, offset + 25,  pow(2, 14) - 1, 7)
        self.s_progin7 = self.get_parameter(setting_msg_u16, offset + 26,  pow(2, 7) - 1, 0)
        self.s_progin8 = self.get_parameter(setting_msg_u16, offset + 26,  pow(2, 14) - 1, 7)
        self.s_progin9 = self.get_parameter(setting_msg_u16, offset + 27,  pow(2, 7) - 1, 0)
        self.s_progin10 = self.get_parameter(setting_msg_u16, offset + 27,  pow(2, 14) - 1, 7)

        self.s_pi1 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 1) - 1, 0)
        self.s_pi2 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 2) - 1, 1)
        self.s_pi3 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 3) - 1, 2)
        self.s_pi4 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 4) - 1, 3)
        self.s_pi5 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 5) - 1, 4)
        self.s_pi6 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 6) - 1, 5)
        self.s_pi7 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 7) - 1, 6)
        self.s_pi8 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 8) - 1, 7)
        self.s_pi9 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 9) - 1, 8)
        self.s_pi10 = self.get_parameter(setting_msg_u16, offset + 52,  pow(2, 10) - 1, 9)

        # programmable output
        self.s_progout1 = self.get_parameter(setting_msg_u16, offset + 28,  pow(2, 7) - 1, 0)
        self.s_progout2 = self.get_parameter(setting_msg_u16, offset + 28,  pow(2, 14) - 1, 7)
        self.s_progout3 = self.get_parameter(setting_msg_u16, offset + 29,  pow(2, 7) - 1, 0)
        self.s_progout4 = self.get_parameter(setting_msg_u16, offset + 29,  pow(2, 14) - 1, 7)
        self.s_progout5 = self.get_parameter(setting_msg_u16, offset + 30,  pow(2, 7) - 1, 0)
        self.s_progout6 = self.get_parameter(setting_msg_u16, offset + 30,  pow(2, 14) - 1, 7)
        self.s_progout7 = self.get_parameter(setting_msg_u16, offset + 31,  pow(2, 7) - 1, 0)
        self.s_progout8 = self.get_parameter(setting_msg_u16, offset + 31,  pow(2, 14) - 1, 7)
        self.s_progout9 = self.get_parameter(setting_msg_u16, offset + 32,  pow(2, 7) - 1, 0)
        self.s_progout11 = self.get_parameter(setting_msg_u16, offset + 32,  pow(2, 14) - 1, 7)
        self.s_progout11 = self.get_parameter(setting_msg_u16, offset + 33,  pow(2, 7) - 1, 0)
        self.s_progout12 = self.get_parameter(setting_msg_u16, offset + 33,  pow(2, 14) - 1, 7)
        self.s_progout13 = self.get_parameter(setting_msg_u16, offset + 34,  pow(2, 7) - 1, 0)
        self.s_progout14 = self.get_parameter(setting_msg_u16, offset + 34,  pow(2, 14) - 1, 7)
        self.s_progout15 = self.get_parameter(setting_msg_u16, offset + 35,  pow(2, 7) - 1, 0)
        self.s_progout16 = self.get_parameter(setting_msg_u16, offset + 35,  pow(2, 14) - 1, 7)
        self.s_progout17 = self.get_parameter(setting_msg_u16, offset + 36,  pow(2, 7) - 1, 0)

        self.s_pocontact1 = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 9) - 1, 8)
        self.s_pocontact2 = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 10) - 1, 9)
        self.s_pocontact3 = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 11) - 1, 10)
        self.s_pocontact4 = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 12) - 1, 11)
        self.s_pocontact5 = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 13) - 1, 12)
        self.s_pocontact6 = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 14) - 1, 13)
        self.s_pocontact7 = self.get_parameter(setting_msg_u16, offset + 50,  pow(2, 15) - 1, 14)
        self.s_pocontact8 = self.get_parameter(setting_msg_u16, offset + 50, - 1, 15)
        self.s_pocontact9 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 1) - 1, 0)
        self.s_pocontact10 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 2) - 1, 1)
        self.s_pocontact11 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 3) - 1, 2)
        self.s_pocontact12 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 4) - 1, 3)
        self.s_pocontact13 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 5) - 1, 4)
        self.s_pocontact14 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 6) - 1, 5)
        self.s_pocontact15 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 7) - 1, 6)
        self.s_pocontact16 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 8) - 1, 7)
        self.s_pocontact17 = self.get_parameter(setting_msg_u16, offset + 51,  pow(2, 9) - 1, 8)

        # fault setting
        self.s_e3_fault = self.get_parameter(setting_msg_u16, offset + 30,  pow(2, 15) - 1, 14)
        self.s_e4_fault = self.get_parameter(setting_msg_u16, offset + 30,  - 1, 15)
        self.s_e5_fault = self.get_parameter(setting_msg_u16, offset + 25,  pow(2, 15) - 1, 14)
        self.s_e6_fault = self.get_parameter(setting_msg_u16, offset + 25,  - 1, 15)
        self.s_e7_fault = self.get_parameter(setting_msg_u16, offset + 26,  pow(2, 15) - 1, 14)
        self.s_e8_fault = self.get_parameter(setting_msg_u16, offset + 48,  pow(2, 9) - 1, 8)
        self.s_fl_fault = self.get_parameter(setting_msg_u16, offset + 29,  pow(2, 15) - 1, 14)
        self.s_ol_fault = self.get_parameter(setting_msg_u16, offset + 29,  - 1, 15)
        self.s_oh_fault = self.get_parameter(setting_msg_u16, offset + 48,  pow(2, 7) - 1, 6)
        self.s_ph_fault = self.get_parameter(setting_msg_u16, offset + 32,  pow(2, 15) - 1, 14)
        self.s_pf_fault = self.get_parameter(setting_msg_u16, offset + 32,  - 1, 15)
        self.s_oc_fault = self.get_parameter(setting_msg_u16, offset + 31,  pow(2, 15) - 1, 14)
        self.s_fi_fault = self.get_parameter(setting_msg_u16, offset + 31,  - 1, 15)
        self.s_fe_fault = self.get_parameter(setting_msg_u16, offset + 51,  - 1, 15)

        # serviceman phone
        phone = []
        for i in range(15):  # or maybe 14
            phone.append(str(setting_msg_u16[i + 252]))

        self.s_serviceman_phone = ''.join(phone)

    def set_floor_control(self, floor_num):

        index = floor_num / 8   # determine which byte does the floor belong to?

        pow_value = floor_num % 8   # determine which bit does the floor belong to??
        and_value = pow(2, pow_value)
        and_value = Constants.ELEVATOR_NO_CALL - and_value

        self.mainMessage[Constants.SERIAL_CALL_REG0_BYTE + index] &= and_value

    def parse_parameters(self, msg_u16, exp_id):

        # ------ STATUS BITS -------
        # id
        self.elv_id = self.get_parameter(msg_u16, 3, 15, 0)
        if self.elv_id != exp_id:
            return False

        # lift status
        self.elv_lift_stat = self.get_parameter(msg_u16, 0, 31, 0)
        # correction
        self.elv_correction = self.get_parameter(msg_u16, 0, 32, 5)
        # learn
        self.elv_learn = self.get_parameter(msg_u16, 0, 64, 6)
        # auto-rev
        self.elv_auto_rev = self.get_parameter(msg_u16, 0, 128, 7)
        # fault
        self.elv_lift_fault = self.get_parameter(msg_u16, 0, 32512, 8)
        # up move
        self.elv_up_move = self.get_parameter(msg_u16, 0, 32768, 15)
        # car position
        self.elv_car_position = self.get_parameter(msg_u16, 1, -1, 0)
        # floor number
        self.elv_floor = self.get_parameter(msg_u16, 2, 63, 0)
        # down move
        self.elv_down_move = self.get_parameter(msg_u16, 2, 322768, 15)
        # lvl set
        self.elv_lvl_active = self.get_parameter(msg_u16, 3, 32, 5)
        # lifter
        self.elv_lifter_active = self.get_parameter(msg_u16, 3, 64, 6)
        # Tris
        self.elv_tris_call_enable = self.get_parameter(msg_u16, 2, 16384, 14)

        # --------------- INPUTS ------------------
        # in1
        self.elv_in1 = self.get_parameter(msg_u16, 4, 1, 0)
        # in2
        self.elv_in2 = self.get_parameter(msg_u16, 4, 2, 1)
        # in3
        self.elv_in3 = self.get_parameter(msg_u16, 4, 4, 2)
        # in4
        self.elv_in4 = self.get_parameter(msg_u16, 4, 8, 3)
        # in5
        self.elv_in5 = self.get_parameter(msg_u16, 4, 16, 4)
        # in6
        self.elv_in6 = self.get_parameter(msg_u16, 4, 32, 5)
        # in7
        self.elv_in7 = self.get_parameter(msg_u16, 4, 64, 6)
        # in8
        self.elv_in8 = self.get_parameter(msg_u16, 4, 128, 7)
        # in9
        self.elv_in9 = self.get_parameter(msg_u16, 4, 256, 8)
        # in10
        self.elv_in10 = self.get_parameter(msg_u16, 4, 512, 9)
        # in411
        self.elv_i411 = self.get_parameter(msg_u16, 4, 1024, 10)
        # in419
        self.elv_i419 = self.get_parameter(msg_u16, 4, 2048, 11)
        # in419A
        self.elv_i419a = self.get_parameter(msg_u16, 4, 4096, 12)
        # in420
        self.elv_i420 = self.get_parameter(msg_u16, 4, 8192, 13)
        # in401
        self.elv_i401 = self.get_parameter(msg_u16, 4, 16384, 14)
        # in400A
        self.elv_i400a = self.get_parameter(msg_u16, 4, 32768, 15)
        # in402
        self.elv_i402 = self.get_parameter(msg_u16, 5, 1, 0)
        # in403
        self.elv_i403 = self.get_parameter(msg_u16, 5, 2, 1)
        # in410
        self.elv_i410 = self.get_parameter(msg_u16, 5, 4, 2)
        # in405
        self.elv_i405 = self.get_parameter(msg_u16, 5, 8, 3)
        # in406
        self.elv_i406 = self.get_parameter(msg_u16, 5, 16, 4)
        # in407
        self.elv_i407 = self.get_parameter(msg_u16, 5, 32, 5)
        # IPTC
        self.elv_iptc = self.get_parameter(msg_u16, 5, 64, 6)
        # ILVL
        self.elv_ilvl = self.get_parameter(msg_u16, 5, 128, 7)
        # in404
        self.elv_i404 = self.get_parameter(msg_u16, 5, 256, 8)
        # ISTP
        self.elv_istp = self.get_parameter(msg_u16, 5, 512, 9)
        # IDC
        self.elv_idc = self.get_parameter(msg_u16, 6, 1, 0)
        # IPH1
        self.elv_idc = self.get_parameter(msg_u16, 6, 2, 1)
        # IOL
        self.elv_idc = self.get_parameter(msg_u16, 6, 4, 2)
        # IFL
        self.elv_idc = self.get_parameter(msg_u16, 6, 8, 3)
        # ILF
        self.elv_idc = self.get_parameter(msg_u16, 6, 16, 4)
        # IPH2
        self.elv_idc = self.get_parameter(msg_u16, 6, 32, 5)
        # IPH3
        self.elv_idc = self.get_parameter(msg_u16, 6, 64, 6)
        # ICL
        self.elv_idc = self.get_parameter(msg_u16, 6, 128, 7)
        # IOS
        self.elv_idc = self.get_parameter(msg_u16, 6, 256, 8)
        # ICS
        self.elv_idc = self.get_parameter(msg_u16, 6, 512, 9)
        # IDO
        self.elv_idc = self.get_parameter(msg_u16, 6, 1024, 10)
        # IC4
        self.elv_idc = self.get_parameter(msg_u16, 6, 2048, 11)
        # IC3
        self.elv_idc = self.get_parameter(msg_u16, 6, 4096, 12)
        # OK
        self.elv_idc = self.get_parameter(msg_u16, 6, 32768, 15)
        # -------------- OUTPUTS ---------------
        # UPR
        self.elv_upr = self.get_parameter(msg_u16, 7, 1, 0)
        # DNR
        self.elv_dnr = self.get_parameter(msg_u16, 7, 2, 1)
        # HIR
        self.elv_hir = self.get_parameter(msg_u16, 7, 4, 2)
        # LOR
        self.elv_lor = self.get_parameter(msg_u16, 7, 8, 3)
        # MDR
        self.elv_mdr = self.get_parameter(msg_u16, 7, 16, 4)
        # RCR
        self.elv_rcr = self.get_parameter(msg_u16, 7, 32, 5)
        # DCR
        self.elv_dcr = self.get_parameter(msg_u16, 7, 64, 6)
        # DO1R
        self.elv_do1r = self.get_parameter(msg_u16, 7, 128, 7)
        # LIGHT
        self.elv_light = self.get_parameter(msg_u16, 7, 256, 8)
        # FLT
        self.elv_flt = self.get_parameter(msg_u16, 7, 512, 9)
        # DO2R
        self.elv_do2r = self.get_parameter(msg_u16, 7, 1024, 10)
        # LVLO
        self.elv_lvlo = self.get_parameter(msg_u16, 7, 2048, 11)
        # DO3R
        self.elv_do3r = self.get_parameter(msg_u16, 7, 4096, 12)
        # ANE
        self.elv_ane = self.get_parameter(msg_u16, 7, 8192, 13)
        # MSC
        self.elv_msc = self.get_parameter(msg_u16, 7, 16384, 14)
        # PO17R
        self.elv_po17r = self.get_parameter(msg_u16, 7, 32768, 15)
        # A1
        self.elv_a1 = self.get_parameter(msg_u16, 8, 1, 0)
        # B1
        self.elv_b1 = self.get_parameter(msg_u16, 8, 2, 1)
        # C1
        self.elv_c1 = self.get_parameter(msg_u16, 8, 4, 2)
        # D1
        self.elv_d1 = self.get_parameter(msg_u16, 8, 8, 3)
        # E1
        self.elv_e1 = self.get_parameter(msg_u16, 8, 16, 4)
        # F1
        self.elv_f1 = self.get_parameter(msg_u16, 8, 32, 5)
        # G1
        self.elv_g1 = self.get_parameter(msg_u16, 8, 64, 6)
        # UAL
        self.elv_ual = self.get_parameter(msg_u16, 8, 128, 7)
        # A2
        self.elv_a2 = self.get_parameter(msg_u16, 8, 256, 8)
        # B2
        self.elv_b2 = self.get_parameter(msg_u16, 8, 512, 9)
        # C2
        self.elv_c2 = self.get_parameter(msg_u16, 8, 1024, 10)
        # D2
        self.elv_d2 = self.get_parameter(msg_u16, 8, 2048, 11)
        # E2
        self.elv_e2 = self.get_parameter(msg_u16, 8, 4096, 12)
        # F2
        self.elv_f2 = self.get_parameter(msg_u16, 8, 8192, 13)
        # G2
        self.elv_g2 = self.get_parameter(msg_u16, 8, 16384, 14)
        # DAL
        self.elv_dal = self.get_parameter(msg_u16, 8, 32768, 15)
        # PO1R
        self.elv_po1r = self.get_parameter(msg_u16, 9, 1, 0)
        # PO2R
        self.elv_po2r = self.get_parameter(msg_u16, 9, 2, 1)
        # PO3R
        self.elv_po3r = self.get_parameter(msg_u16, 9, 4, 2)
        # PO4R
        self.elv_po4r = self.get_parameter(msg_u16, 9, 8, 3)
        # PO5R
        self.elv_po5r = self.get_parameter(msg_u16, 9, 16, 4)
        # PO6R
        self.elv_po6r = self.get_parameter(msg_u16, 9, 32, 5)
        # PO7R
        self.elv_po7r = self.get_parameter(msg_u16, 9, 64, 6)
        # PO8R
        self.elv_po8r = self.get_parameter(msg_u16, 9, 128, 7)
        # PO9R
        self.elv_po9r = self.get_parameter(msg_u16, 9, 256, 8)
        # PO10R
        self.elv_po10r = self.get_parameter(msg_u16, 9, 512, 9)
        # PO11R
        self.elv_po11r = self.get_parameter(msg_u16, 9, 1024, 10)
        # PO12R
        self.elv_po12r = self.get_parameter(msg_u16, 9, 2048, 11)
        # PO13R
        self.elv_po13r = self.get_parameter(msg_u16, 9, 4096, 12)
        # PO14R
        self.elv_po14r = self.get_parameter(msg_u16, 9, 8192, 13)
        # PO15R
        self.elv_po15r = self.get_parameter(msg_u16, 9, 16384, 14)
        # PO16R
        self.elv_po16r = self.get_parameter(msg_u16, 9, 32768, 15)
        # ---------------- car calls ------------------
        # clear previous calls

        self.elv_call_car = []
        self.elv_call_hall_up = []
        self.elv_call_hall_down = []

        for i in range(Constants.MAX_FLOORS):

            if Constants.COLLECTIVE_SELECTIVE_MODE == 0:

                if self.get_calls(msg_u16, i, 10) == 0:
                    self.elv_call_hall_down.append(i)

                if self.get_calls(msg_u16, i, 13) == 0:
                    self.elv_call_hall_up.append(i)

            else:
                if self.get_calls(msg_u16, i, 10) == 0:
                    if (i % 2) == 0:
                        self.elv_call_hall_down.append(i/2)
                    else:
                        self.elv_call_hall_up.append(i/2)

            if self.get_calls(msg_u16, i, 16) == 0:  # calls are active low -> 0 means call
                self.elv_call_car.append(i)

        # ----------------- misc --------------------
        self.elv_mode = self.get_elv_mode()
        self.set_numerator_params()

        return True

    def build_setting_json(self, elv_id):

        # id
        setting = {}

        # main setting
        main_setting = {"FN": self.s_floor_number, "ST": self.s_system_type, "BOTFL": self.s_bottom_floor,
                        "CT": self.s_service_type, "LLV": self.s_load_level_value, "DCLS": self.s_dc_limit_switch,
                        "DOLS": self.s_do_limit_switch, "ADO": self.s_adv_door_opening, "PS": self.s_park_status,
                        "PF": self.s_park_floor, "FPF": self.s_fire_park_floor, "CCM": self.s_car_call_mode,
                        "HCM": self.s_hall_call_mode, "CC": self.s_car_capacity, "ET": self.s_elv_test,
                        "SB": self.s_segment_blink, "ENS": self.s_energy_saving, "DD": self.s_double_door,
                        "EVAD": self.s_eva_direct, "FZ": self.s_flag_zone, "CLB": self.s_car_lowsdp_blink,
                        "ACM": self.s_audio_music, "AA": self.s_audio_announce, "SCD": self.s_service_call,
                        "SP": self.s_serviceman_phone, "CR": self.s_counter_reset, "FACD": self.s_factory_default, "CST": self.s_service_call_days,
			"ETT": self.s_elv_test_value}

        # floor setting
        floor_setting = []
        for i in range(self.s_floor_number):
            floor_setting.append({"SF": i, "COT": self.s_collect_type[i], "SEG1": self.s_numerator_code_seg1[i],
                           "SEG2": self.s_numerator_code_seg2[i], "DT": self.s_door_type[i], "DPM": self.s_door_park_mode[i],
                           "DA": self.s_door_action[i], "HC": self.s_hall_call[i], "CACA": self.s_car_call[i],
                           "MD": self.s_motion_detector[i], "LP": self.s_level_position[i], "CS": self.s_code_segment[i]})

        # time setting
        time_setting = {"CLT": self.s_car_light_time, "PT": self.s_park_time, "DOT": self.s_door_open_time,
                        "DCT": self.s_door_close_time, "TT": self.s_travel_time, "LD": self.s_lock_debouncer,
                        "CD": self.s_cont_debouncer, "PSGT": self.s_passenger_time, "CAT": self.s_car_acc_time,
                        "HVLTBT": self.s_hlf_vlt_brk_time, "USD": self.s_up_stop_delay, "DSD": self.s_down_stop_delay,
                        "EVASD": self.s_eva_start_delay, "EVARD": self.s_eva_run_delay, "POO": self.s_pot1_on_time,
                        "POF": self.s_pot1_off_time, "ENO": self.s_energy_saving_on, "ENF": self.s_energy_saving_off,
                        "AD": self.s_announce_delay, "LMD": self.s_lock_mgnt_delay, "ECSD": self.s_encoder_check_start,
                        "ECPT": self.s_encoder_check_per, "LISD": self.s_lift_init_start, "LDS": self.s_lift_deep_sleep,
                        "SUNON": self.s_sunday_on, "SUNOF": self.s_sunday_off, "MONON": self.s_monday_on,
                        "MONOF": self.s_monday_off, "TUEON": self.s_tuesday_on, "TUEOF": self.s_tuesday_off,
                        "WENON": self.s_wednesday_on, "WENOF": self.s_wednesday_off, "THUON": self.s_thursday_on,
                        "THUOF": self.s_thursday_off, "FRION": self.s_friday_on, "FRIOF": self.s_friday_off,
                        "SATON": self.s_saturday_on, "SATOF": self.s_saturday_off}

        # speed setting
        speed_setting = {"US": self.s_used_speeds, "LESBO": self.s_lvl_bin_out, "LOSBO": self.s_low_bin_out,
                         "INSBO": self.s_rev_bin_out, "FUSBO": self.s_full_bin_out, "FUSACCD": self.s_full_acc,
                         "FUSDECCD": self.s_full_decc, "V1BO": self.s_v1_bin_out, "V1ACCD": self.s_v1_acc,
                         "V1DECCD": self.s_v1_decc, "V2BO": self.s_v2_bin_out, "V2ACCD": self.s_v2_acc,
                         "V2DECCD": self.s_v2_decc, "V3BO": self.s_v3_bin_out, "V3ACCD": self.s_v3_acc,
                         "V3DECCD": self.s_v3_decc, "V4BO": self.s_v4_bin_out, "V4ACCD": self.s_v4_acc,
                         "V4DECCD": self.s_v4_decc}
        # learn setting
        learn_setting = {"MT": self.s_motor_type, "S": self.s_suspension, "EP": self.s_enc_pulse,
                         "EF": self.s_enc_filter, "GR": self.s_gear_ratio, "SD": self.s_sheave_diameter,
                         "LSV": self.s_low_speed_val, "FDTD": self.s_flags_dls_to_ds, "FUTU": self.s_flgs_uls_to_us,
                         "CM": self.s_correction_mode, "LB": self.s_learn_button}
        # fixed inputs
        fixed_inputs = {"PH1I": self.s_ph1i, "PH2I": self.s_ph2i, "PH3I": self.s_ph3i, "DOI": self.s_doi,
                        "DCI": self.s_dci, "OLI": self.s_oli, "FLI": self.s_fli, "LFI": self.s_lfi,
                        "CNCLI": self.s_cncli, "OLSI": self.s_olsi, "CLSI": self.s_clsi}
        # programmable inputs
        prog_inputs = {"PRI1": self.s_progin1, "PRI2": self.s_progin2, "PRI3": self.s_progin3, "PRI4": self.s_progin4,
                       "PRI5": self.s_progin5, "PRI6": self.s_progin6, "PRI7": self.s_progin7, "PRI8": self.s_progin8,
                       "PRI9": self.s_progin9, "PRI10": self.s_progin10, "PRIB1": self.s_pi1, "PRIB2": self.s_pi2,
                       "PRIB3": self.s_pi3, "PRIB4": self.s_pi4, "PRIB5": self.s_pi5, "PRIB6": self.s_pi6,
                       "PRIB7": self.s_pi7, "PRIB8": self.s_pi8, "PRIB9": self.s_pi9, "PRIB10": self.s_pi10}
        # programmable outputs
        prog_outputs = {"PRO1": self.s_progout1, "PRO2": self.s_progout2, "PRO3": self.s_progout3,
                        "PRO4": self.s_progout4, "PRO5": self.s_progout5, "PRO6": self.s_progout6,
                        "PRO7": self.s_progout7, "PRO8": self.s_progout8, "PRO9": self.s_progout9,
                        "PRO10": self.s_progout10, "PRO11": self.s_progout11, "PRO12": self.s_progout12,
                        "PRO13": self.s_progout13, "PRO14": self.s_progout14, "PRO15": self.s_progout15,
                        "PRO16": self.s_progout16, "PRO17": self.s_progout17, "PROB1": self.s_pocontact1,
                        "PROB2": self.s_pocontact2, "PROB3": self.s_pocontact3, "PROB4": self.s_pocontact4,
                        "PROB5": self.s_pocontact5, "PROB6": self.s_pocontact6, "PROB7": self.s_pocontact7,
                        "PROB8": self.s_pocontact8, "PROB9": self.s_pocontact9, "PROB10": self.s_pocontact10,
                        "PROB11": self.s_pocontact11, "PROB12": self.s_pocontact12, "PROB13": self.s_pocontact13,
                        "PROB14": self.s_pocontact14, "PROB15": self.s_pocontact15, "PROB16": self.s_pocontact16,
                        "PROB17": self.s_pocontact17}
        # fault setting
        fault_setting = {"EXF": self.s_e3_fault, "CANF": self.s_e4_fault, "MB": self.s_e5_fault, "TTO": self.s_e6_fault,
                         "CFB": self.s_e7_fault, "DO": self.s_e8_fault, "FLF": self.s_fl_fault, "OLF": self.s_ol_fault,
                         "OHF": self.s_oh_fault, "DP": self.s_ph_fault, "PC": self.s_pf_fault, "OC": self.s_oc_fault,
                         "FD": self.s_fi_fault, "ENF": self.s_fe_fault, "CFH": self.s_clear_fault}

        setting['MAIN_SETTING'] = main_setting
        setting['FLOOR_SETTINGS'] = floor_setting
        setting['TIME_SETTING'] = time_setting
        setting['SPEED_SETTING'] = speed_setting
        setting['LEARN_SETTING'] = learn_setting
        setting['FIXED_INPUTS'] = fixed_inputs
        setting['PROG_INPUTS'] = prog_inputs
        setting['PROG_OUTPUTS'] = prog_outputs
        setting['FAULT_SETTING'] = fault_setting

        # setting_array = [setting]

        json_to_send = json.dumps(setting)
        return json_to_send

    def parse_setting_json(self, json_to_parse):
        json_object = json_to_parse

        elv_id = int(json_object["id"])  # id is obtained in main file not so much use here
        print "reading main setting"

        # main setting
        main_setting = json_object["MAIN_SETTING"]
        self.s_floor_number = int(main_setting["FN"])
        self.s_system_type = int(main_setting["ST"])
        self.s_bottom_floor = int(main_setting["BOTFL"])
        self.s_service_type = int(main_setting["CT"])
        self.s_load_level_value = int(main_setting["LLV"])
        self.s_dc_limit_switch = int(main_setting["DCLS"])
        self.s_do_limit_switch = int(main_setting["DOLS"])
        self.s_adv_door_opening = int(main_setting["ADO"])
        self.s_park_status = int(main_setting["PS"])
        self.s_park_floor = int(main_setting["PF"])
        self.s_fire_park_floor = int(main_setting["FPF"])
        self.s_car_call_mode = int(main_setting["CCM"])
        self.s_hall_call_mode = int(main_setting["HCM"])
        self.s_car_capacity = int(main_setting["CC"])
        self.s_elv_test = int(main_setting["ET"])
        self.s_segment_blink = int(main_setting["SB"])
        self.s_energy_saving = int(main_setting["ENS"])
        self.s_double_door = int(main_setting["DD"])
        self.s_eva_direct = int(main_setting["EVAD"])
        self.s_flag_zone = int(main_setting["FZ"])
        self.s_car_lowsdp_blink = int(main_setting["CLB"])
        self.s_audio_music = int(main_setting["ACM"])
        self.s_audio_announce = int(main_setting["AA"])
        self.s_service_call = int(main_setting["SCD"])
        self.s_serviceman_phone = (main_setting["SP"])
        self.s_counter_reset = int(main_setting["CR"])
        #self.s_factory_default = int(main_setting["FACD"])
	self.s_elv_test_value = int(main_setting["ETT"]) #TODO uncomment after khashi has added this
	self.s_service_call_days = int (main_setting["CST"])
	print "days = "
	print self.s_service_call_days
	print "service call"
	print self.s_service_call

        print "reading floor setting"
        # floor setting
        # floor_setting = []
        # for i in range(self.s_floor_number):
            # floor_setting.append(json_object["FLOOR_SETTINGS"][i])
        floor_setting = json_object["FLOOR_SETTINGS"]
        for i in range(self.s_floor_number):
            print i
            select_floor = int(floor_setting[i]["SF"])
            self.s_collect_type[select_floor] = int(floor_setting[select_floor]["COT"])
            self.s_numerator_code_seg1[select_floor] = int(floor_setting[select_floor]["SEG1"])
            self.s_numerator_code_seg2[select_floor] = int(floor_setting[select_floor]["SEG2"])
            self.s_door_type[select_floor] = int(floor_setting[select_floor]["DT"])
            self.s_door_park_mode[select_floor] = int(floor_setting[select_floor]["DPM"])
            self.s_door_action[select_floor] = int(floor_setting[select_floor]["DA"])
            self.s_hall_call[select_floor] = int(floor_setting[select_floor]["HC"])
            self.s_car_call[select_floor] = int(floor_setting[select_floor]["CACA"])
            self.s_motion_detector[select_floor] = int(floor_setting[select_floor]["MD"])
            self.s_level_position[select_floor] = int(floor_setting[select_floor]["LP"])
            self.s_code_segment[select_floor] = int(floor_setting[select_floor]["CS"])

        print "reading time setting"
        # time setting
        time_setting = json_object["TIME_SETTING"]
        self.s_car_light_time = int(time_setting["CLT"])
        self.s_park_time = int(time_setting["PT"])
        self.s_door_open_time = int(time_setting["DOT"])
        self.s_door_close_time = int(time_setting["DCT"])
        self.s_travel_time = int(time_setting["TT"])
        self.s_lock_debouncer = int(time_setting["LD"])
        self.s_cont_debouncer = int(time_setting["CD"])
        self.s_passenger_time = int(time_setting["PSGT"])
        self.s_car_acc_time = int(time_setting["CAT"])
        self.s_hlf_vlt_brk_time = int(time_setting["HVLTBT"])
        self.s_up_stop_delay = int(time_setting["USD"])
        self.s_down_stop_delay = int(time_setting["DSD"])
        self.s_eva_start_delay = int(time_setting["EVASD"])
        self.s_eva_run_delay = int(time_setting["EVARD"])
        self.s_pot1_on_time = int(time_setting["POO"])
        self.s_pot1_off_time = int(time_setting["POF"])
        self.s_energy_saving_on = int(time_setting["ENO"])
        self.s_energy_saving_off = int(time_setting["ENF"])
        self.s_announce_delay = int(time_setting["AD"])
        self.s_lock_mgnt_delay = int(time_setting["LMD"])
        self.s_encoder_check_start = int(time_setting["ECSD"])
        self.s_encoder_check_per = int(time_setting["ECPT"])
        self.s_lift_init_start = int(time_setting["LISD"])
        self.s_lift_deep_sleep = int(time_setting["LDS"])
        self.s_sunday_on = int(time_setting["SUNON"])
        self.s_sunday_off = int(time_setting["SUNOF"])

        self.s_sunday = self.s_sunday_on
        self.s_sunday |= self.s_sunday_off << 5
        if self.s_sunday_on != 0:
            self.s_sunday |= 1 << 10
        if self.s_sunday_off != 0:
            self.s_sunday |= 1 << 11

        self.s_monday_on = int(time_setting["MONON"])
        self.s_monday_off = int(time_setting["MONOF"])

        self.s_monday = self.s_sunday_on
        self.s_monday |= self.s_sunday_off << 5
        if self.s_monday_on != 0:
            self.s_monday |= 1 << 10
        if self.s_monday_off != 0:
            self.s_monday |= 1 << 11

        self.s_tuesday_on = int(time_setting["TUEON"])
        self.s_tuesday_off = int(time_setting["TUEOF"])

        self.s_tuesday = self.s_sunday_on
        self.s_tuesday |= self.s_sunday_off << 5
        if self.s_sunday_on != 0:
            self.s_tuesday |= 1 << 10
        if self.s_tuesday_off != 0:
            self.s_tuesday |= 1 << 11

        self.s_wednesday_on = int(time_setting["WENON"])
        self.s_wednesday_off = int(time_setting["WENOF"])

        self.s_wednesday = self.s_sunday_on
        self.s_wednesday |= self.s_sunday_off << 5
        if self.s_wednesday_on != 0:
            self.s_wednesday |= 1 << 10
        if self.s_wednesday_off != 0:
            self.s_wednesday |= 1 << 11

        self.s_thursday_on = int(time_setting["THUON"])
        self.s_thursday_off = int(time_setting["THUOF"])

        self.s_thursday = self.s_sunday_on
        self.s_thursday |= self.s_sunday_off << 5
        if self.s_thursday_on != 0:
            self.s_thursday |= 1 << 10
        if self.s_thursday_off != 0:
            self.s_thursday |= 1 << 11

        self.s_friday_on = int(time_setting["FRION"])
        self.s_friday_off = int(time_setting["FRIOF"])

        self.s_friday = self.s_sunday_on
        self.s_friday |= self.s_sunday_off << 5
        if self.s_friday_on != 0:
            self.s_friday |= 1 << 10
        if self.s_friday_off != 0:
            self.s_friday |= 1 << 11

        self.s_saturday_on = int(time_setting["SATON"])
        self.s_saturday_off = int(time_setting["SATOF"])

        self.s_saturday = self.s_sunday_on
        self.s_saturday |= self.s_sunday_off << 5
        if self.s_saturday_on != 0:
            self.s_saturday |= 1 << 10
        if self.s_saturday_off != 0:
            self.s_saturday |= 1 << 11

        # speed setting
        speed_setting = json_object["SPEED_SETTING"]
        self.s_used_speeds = int(speed_setting["US"])
        self.s_lvl_bin_out = int(speed_setting["LESBO"])
        self.s_low_bin_out = int(speed_setting["LOSBO"])
        self.s_rev_bin_out = int(speed_setting["INSBO"])
        self.s_full_bin_out = int(speed_setting["FUSBO"])
        self.s_full_acc = int(speed_setting["FUSACCD"])
        self.s_full_decc = int(speed_setting["FUSDECCD"])
        self.s_v1_bin_out = int(speed_setting["V1BO"])
        self.s_v1_acc = int(speed_setting["V1ACCD"])
        self.s_v1_decc = int(speed_setting["V1DECCD"])
        self.s_v2_bin_out = int(speed_setting["V2BO"])
        self.s_v2_acc = int(speed_setting["V2ACCD"])
        self.s_v2_decc = int(speed_setting["V2DECCD"])
        self.s_v3_bin_out = int(speed_setting["V3BO"])
        self.s_v3_acc = int(speed_setting["V3ACCD"])
        self.s_v3_decc = int(speed_setting["V3DECCD"])
        self.s_v4_bin_out = int(speed_setting["V4BO"])
        self.s_v4_acc = int(speed_setting["V4ACCD"])
        self.s_v4_decc = int(speed_setting["V4DECCD"])

        # learn setting
        learn_setting = json_object["LEARN_SETTING"]
        self.s_motor_type = int(learn_setting["MT"])
        self.s_suspension = int(learn_setting["S"])
        self.s_enc_pulse = int(learn_setting["EP"])
        self.s_enc_filter = int(learn_setting["EF"])
        self.s_gear_ratio = int(learn_setting["GR"])
        self.s_sheave_diameter = int(learn_setting["SD"])
        self.s_low_speed_val = int(learn_setting["LSV"])
        self.s_flags_dls_to_ds = int(learn_setting["FDTD"])
        self.s_flgs_uls_to_us = int(learn_setting["FUTU"])
        self.s_correction_mode = int(learn_setting["CM"])
        self.s_learn_button = int(learn_setting["LB"])

        # fixed inputs
        fixed_inputs = json_object["FIXED_INPUTS"]
        self.s_ph1i = int(fixed_inputs["PH1I"])
        self.s_ph2i = int(fixed_inputs["PH2I"])
        self.s_ph3i = int(fixed_inputs["PH3I"])
        self.s_doi = int(fixed_inputs["DOI"])
        self.s_dci = int(fixed_inputs["DCI"])
        self.s_oli = int(fixed_inputs["OLI"])
        self.s_fli = int(fixed_inputs["FLI"])
        self.s_lfi = int(fixed_inputs["LFI"])
        self.s_cncli = int(fixed_inputs["CNCLI"])
        self.s_olsi = int(fixed_inputs["OLSI"])
        self.s_clsi = int(fixed_inputs["CLSI"])

        # programmable inputs
        prog_inputs = json_object["PROG_INPUTS"]
        self.s_progin1 = int(prog_inputs["PRI1"])
        self.s_progin2 = int(prog_inputs["PRI2"])
        self.s_progin3 = int(prog_inputs["PRI3"])
        self.s_progin4 = int(prog_inputs["PRI4"])
        self.s_progin5 = int(prog_inputs["PRI5"])
        self.s_progin6 = int(prog_inputs["PRI6"])
        self.s_progin7 = int(prog_inputs["PRI7"])
        self.s_progin8 = int(prog_inputs["PRI8"])
        self.s_progin9 = int(prog_inputs["PRI9"])
        self.s_progin10 = int(prog_inputs["PRI10"])

        self.s_pi1 = int(prog_inputs["PRIB1"])
        self.s_pi2 = int(prog_inputs["PRIB2"])
        self.s_pi3 = int(prog_inputs["PRIB3"])
        self.s_pi4 = int(prog_inputs["PRIB4"])
        self.s_pi5 = int(prog_inputs["PRIB5"])
        self.s_pi6 = int(prog_inputs["PRIB6"])
        self.s_pi7 = int(prog_inputs["PRIB7"])
        self.s_pi8 = int(prog_inputs["PRIB8"])
        self.s_pi9 = int(prog_inputs["PRIB9"])
        self.s_pi10 = int(prog_inputs["PRIB10"])

        # programmable outputs
        prog_outputs = json_object["PROG_OUTPUTS"]
        self.s_progout1 = int(prog_outputs["PRO1"])
        self.s_progout2 = int(prog_outputs["PRO2"])
        self.s_progout3 = int(prog_outputs["PRO3"])
        self.s_progout4 = int(prog_outputs["PRO4"])
        self.s_progout5 = int(prog_outputs["PRO5"])
        self.s_progout6 = int(prog_outputs["PRO6"])
        self.s_progout7 = int(prog_outputs["PRO7"])
        self.s_progout8 = int(prog_outputs["PRO8"])
        self.s_progout9 = int(prog_outputs["PRO9"])
        self.s_progout10 = int(prog_outputs["PRO10"])
        self.s_progout11 = int(prog_outputs["PRO11"])
        self.s_progout12 = int(prog_outputs["PRO12"])
        self.s_progout13 = int(prog_outputs["PRO13"])
        self.s_progout14 = int(prog_outputs["PRO14"])
        self.s_progout15 = int(prog_outputs["PRO15"])

        self.s_pocontact1 = int(prog_outputs["PROB1"])
        self.s_pocontact2 = int(prog_outputs["PROB2"])
        self.s_pocontact3 = int(prog_outputs["PROB3"])
        self.s_pocontact4 = int(prog_outputs["PROB4"])
        self.s_pocontact5 = int(prog_outputs["PROB5"])
        self.s_pocontact6 = int(prog_outputs["PROB6"])
        self.s_pocontact7 = int(prog_outputs["PROB7"])
        self.s_pocontact8 = int(prog_outputs["PROB8"])
        self.s_pocontact9 = int(prog_outputs["PROB9"])
        self.s_pocontact10 = int(prog_outputs["PROB10"])
        self.s_pocontact11 = int(prog_outputs["PROB11"])
        self.s_pocontact12 = int(prog_outputs["PROB12"])
        self.s_pocontact13 = int(prog_outputs["PROB13"])
        self.s_pocontact14 = int(prog_outputs["PROB14"])
        self.s_pocontact15 = int(prog_outputs["PROB15"])

        # fault setting
        fault_setting = json_object["FAULT_SETTING"]
        self.s_e3_fault = int(fault_setting["EXF"])
        self.s_e4_fault = int(fault_setting["CANF"])
        self.s_e5_fault = int(fault_setting["MB"])
        self.s_e6_fault = int(fault_setting["TTO"])
        self.s_e7_fault = int(fault_setting["CFB"])
        self.s_e8_fault = int(fault_setting["DO"])
        self.s_fl_fault = int(fault_setting["FLF"])
        self.s_ol_fault = int(fault_setting["OLF"])
        self.s_oh_fault = int(fault_setting["OHF"])
        self.s_ph_fault = int(fault_setting["DP"])
        self.s_pf_fault = int(fault_setting["PC"])
        self.s_oc_fault = int(fault_setting["OC"])
        self.s_fi_fault = int(fault_setting["FD"])
        self.s_fe_fault = int(fault_setting["ENF"])
        self.s_clear_fault = int(fault_setting["CFH"])

    @staticmethod
    def get_parameter(msg_u16, index, and_value, shift_value):
        temp_val = msg_u16[index]

        if and_value != -1:
            temp_val &= and_value

        temp_val >>= shift_value
        return temp_val

    @staticmethod
    def get_day_parameter(day_value, and_value, shift_value):

        on_off_value = day_value
        if and_value != -1:
            on_off_value &= and_value

        on_off_value >>= shift_value
        return on_off_value

    def set_parameter(self, value, index, shift_value, param_len):
        # clear previous value
        for i in range(shift_value, shift_value + param_len, 1):
            self.setting_msg_u16[index] &= ~(1 << i)

        value <<= shift_value  # TODO: FIXME
        self.setting_msg_u16[index] |= value

    @staticmethod
    def get_calls(msg_u16, floor_nu, msg_offset):
        index = floor_nu / 16
        index += msg_offset

        shift_value = (floor_nu % 16)  # little Endian
        and_value = int(math.pow(2, shift_value))

        result = msg_u16[index]
        result &= and_value
        result >>= shift_value

        return result  # 0 or 1

    def get_elv_mode(self):

        mode = Constants.ELEVATOR_DEFAULT_MODE

        if self.elv_auto_rev == 1:
            if self.elv_correction == 1:
                mode = Constants.ELV_MODE_CORRECTION
            elif self.elv_learn == 1:
                mode = Constants.ELV_MODE_LEARN
            elif self.elv_lvl_active == 1:
                mode = Constants.ELV_MODE_LEVEL_SET
            elif self.elv_lifter_active == 1:
                mode = Constants.ELV_MODE_LIFTER
            else:
                mode = Constants.ELV_MODE_NORMAL

        elif self.elv_auto_rev == 0:
            mode = Constants.ELV_MODE_REVISION

        return mode

    def set_numerator_params(self):

        # up and down (direction)

        self.elv_direction = Constants.ELV_DIR_NONE

        if self.elv_ual == 1:
            self.elv_numerator_up = 1
            self.elv_direction = Constants.ELV_DIR_DOWN  # khashi says it must be reverse!
        else:
            self.elv_numerator_up = 0

        if self.elv_dal == 1:
            self.elv_numerator_down = 1
            self.elv_direction = Constants.ELV_DIR_UP
        else:
            self.elv_numerator_down = 0

        # 7segment

        if (self.elv_a1 == 0) and (self.elv_b1 == 0) and (self.elv_c1 == 0) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 0) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "-"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 0) and (self.elv_g1 == 0):
            self.elv_numerator_segment1 = "1"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 0) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 0) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "2"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 0) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "3"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "4"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 0) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "5"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 0) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "6"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 0) and (self.elv_g1 == 0):
            self.elv_numerator_segment1 = "7"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "8"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "9"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 0):
            self.elv_numerator_segment1 = "0"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 0) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 0):
            self.elv_numerator_segment1 = "G"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 0) and (self.elv_c1 == 0) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "F"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "A"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 1) and (self.elv_c1 == 0) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "P"

        elif (self.elv_a1 == 1) and (self.elv_b1 == 0) and (self.elv_c1 == 0) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "E"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 0) and (self.elv_c1 == 0) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 0):
            self.elv_numerator_segment1 = "L"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "H"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 0) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "d"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 0) and (self.elv_c1 == 1) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "h"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 0) and (self.elv_c1 == 0) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 0) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "r"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 0) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 1) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "b"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 0) and (self.elv_c1 == 1) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 0) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "o"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 0) and (self.elv_c1 == 0) and (self.elv_d1 == 1) and\
                (self.elv_e1 == 1) and (self.elv_f1 == 0) and (self.elv_g1 == 1):
            self.elv_numerator_segment1 = "c"

        elif (self.elv_a1 == 0) and (self.elv_b1 == 1) and (self.elv_c1 == 1) and (self.elv_d1 == 0) and\
                (self.elv_e1 == 0) and (self.elv_f1 == 0) and (self.elv_g1 == 0):
            self.elv_numerator_segment1 = "I"

        else:
            self.elv_numerator_segment1 = ""

        if (self.elv_a2 == 0) and (self.elv_b2 == 0) and (self.elv_c2 == 0) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 0) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "-"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 0) and (self.elv_g2 == 0):
            self.elv_numerator_segment2 = "1"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 0) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 0) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "2"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 0) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "3"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "4"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 0) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "5"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 0) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "6"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 0) and (self.elv_g2 == 0):
            self.elv_numerator_segment2 = "7"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "8"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "9"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 0):
            self.elv_numerator_segment2 = "0"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 0) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 0):
            self.elv_numerator_segment2 = "G"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 0) and (self.elv_c2 == 0) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "F"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "A"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 1) and (self.elv_c2 == 0) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "P"

        elif (self.elv_a2 == 1) and (self.elv_b2 == 0) and (self.elv_c2 == 0) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "E"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 0) and (self.elv_c2 == 0) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 0):
            self.elv_numerator_segment2 = "L"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "H"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 0) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "d"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 0) and (self.elv_c2 == 1) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "h"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 0) and (self.elv_c2 == 0) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 0) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "r"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 0) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 1) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "b"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 0) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 0) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "o"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 0) and (self.elv_c2 == 1) and (self.elv_d2 == 1) and\
                (self.elv_e2 == 1) and (self.elv_f2 == 0) and (self.elv_g2 == 1):
            self.elv_numerator_segment2 = "c"

        elif (self.elv_a2 == 0) and (self.elv_b2 == 1) and (self.elv_c2 == 1) and (self.elv_d2 == 0) and\
                (self.elv_e2 == 0) and (self.elv_f2 == 0) and (self.elv_g2 == 0):
            self.elv_numerator_segment2 = "I"

        else:
            self.elv_numerator_segment2 = ""

        self.elv_numerator_concat = self.elv_numerator_segment2 + self.elv_numerator_segment1
