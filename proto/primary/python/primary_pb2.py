# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: primary.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rprimary.proto\x12\x07primary\"-\n\x11\x42MS_HV_JMP_TO_BLT\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"]\n\rSTEER_VERSION\x12\x19\n\x11\x63omponent_version\x18\x01 \x01(\r\x12\x17\n\x0f\x63\x61ncicd_version\x18\x02 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"[\n\x0b\x44\x41S_VERSION\x12\x19\n\x11\x63omponent_version\x18\x01 \x01(\r\x12\x17\n\x0f\x63\x61ncicd_version\x18\x02 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"Z\n\nHV_VERSION\x12\x19\n\x11\x63omponent_version\x18\x01 \x01(\r\x12\x17\n\x0f\x63\x61ncicd_version\x18\x02 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"Z\n\nLV_VERSION\x12\x19\n\x11\x63omponent_version\x18\x01 \x01(\r\x12\x17\n\x0f\x63\x61ncicd_version\x18\x02 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"[\n\x0bTLM_VERSION\x12\x19\n\x11\x63omponent_version\x18\x01 \x01(\r\x12\x17\n\x0f\x63\x61ncicd_version\x18\x02 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"8\n\tTIMESTAMP\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"\x96\x01\n\x0eSET_TLM_STATUS\x12\x0e\n\x06\x64river\x18\x01 \x01(\r\x12\x0f\n\x07\x63ircuit\x18\x02 \x01(\r\x12$\n\trace_type\x18\x03 \x01(\x0e\x32\x11.primary.RaceType\x12#\n\ntlm_status\x18\x04 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x05 \x01(\x04\"\x92\x01\n\nTLM_STATUS\x12\x0e\n\x06\x64river\x18\x01 \x01(\r\x12\x0f\n\x07\x63ircuit\x18\x02 \x01(\r\x12$\n\trace_type\x18\x03 \x01(\x0e\x32\x11.primary.RaceType\x12#\n\ntlm_status\x18\x04 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x05 \x01(\x04\"A\n\x13STEER_SYSTEM_STATUS\x12\x10\n\x08soc_temp\x18\x01 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"\x85\x01\n\nHV_VOLTAGE\x12\x14\n\x0cpack_voltage\x18\x01 \x01(\r\x12\x13\n\x0b\x62us_voltage\x18\x02 \x01(\r\x12\x18\n\x10max_cell_voltage\x18\x03 \x01(\r\x12\x18\n\x10min_cell_voltage\x18\x04 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x05 \x01(\x04\"F\n\nHV_CURRENT\x12\x0f\n\x07\x63urrent\x18\x01 \x01(\r\x12\r\n\x05power\x18\x02 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"]\n\x07HV_TEMP\x12\x14\n\x0c\x61verage_temp\x18\x01 \x01(\r\x12\x10\n\x08max_temp\x18\x02 \x01(\r\x12\x10\n\x08min_temp\x18\x03 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x04 \x01(\x04\"G\n\tHV_ERRORS\x12\x10\n\x08warnings\x18\x01 \x01(\r\x12\x0e\n\x06\x65rrors\x18\x02 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"T\n\x0eHV_CAN_FORWARD\x12(\n\x0f\x63\x61n_forward_set\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"^\n\x15HV_CAN_FORWARD_STATUS\x12+\n\x12\x63\x61n_forward_status\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"K\n\tTS_STATUS\x12$\n\tts_status\x18\x01 \x01(\x0e\x32\x11.primary.TsStatus\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"U\n\x11SET_TS_STATUS_DAS\x12&\n\rts_status_set\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"Z\n\x16SET_TS_STATUS_HANDCART\x12&\n\rts_status_set\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"w\n\x0cSTEER_STATUS\x12\x19\n\x03map\x18\x01 \x01(\x0e\x32\x0c.primary.Map\x12\x32\n\x10traction_control\x18\x02 \x01(\x0e\x32\x18.primary.TractionControl\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"Y\n\x0eSET_CAR_STATUS\x12-\n\x0e\x63\x61r_status_set\x18\x01 \x01(\x0e\x32\x15.primary.SetCarStatus\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"j\n\x10SET_PEDALS_RANGE\x12\x1d\n\x05\x62ound\x18\x01 \x01(\x0e\x32\x0e.primary.Bound\x12\x1d\n\x05pedal\x18\x02 \x01(\x0e\x32\x0e.primary.Pedal\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"S\n\x18SET_STEERING_ANGLE_RANGE\x12\x1d\n\x05\x62ound\x18\x01 \x01(\x0e\x32\x0e.primary.Bound\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"\xa8\x01\n\nCAR_STATUS\x12+\n\ninverter_l\x18\x01 \x01(\x0e\x32\x17.primary.InverterStatus\x12+\n\ninverter_r\x18\x02 \x01(\x0e\x32\x17.primary.InverterStatus\x12&\n\ncar_status\x18\x03 \x01(\x0e\x32\x12.primary.CarStatus\x12\x18\n\x10_inner_timestamp\x18\x04 \x01(\x04\"9\n\nDAS_ERRORS\x12\x11\n\tdas_error\x18\x01 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"7\n\nLV_CURRENT\x12\x0f\n\x07\x63urrent\x18\x01 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"r\n\nLV_VOLTAGE\x12\x11\n\tvoltage_1\x18\x01 \x01(\r\x12\x11\n\tvoltage_2\x18\x02 \x01(\r\x12\x11\n\tvoltage_3\x18\x03 \x01(\r\x12\x11\n\tvoltage_4\x18\x04 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x05 \x01(\x04\"C\n\x10LV_TOTAL_VOLTAGE\x12\x15\n\rtotal_voltage\x18\x01 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"\x96\x01\n\x0eLV_TEMPERATURE\x12\x18\n\x10\x62p_temperature_1\x18\x01 \x01(\r\x12\x18\n\x10\x62p_temperature_2\x18\x02 \x01(\r\x12\x1a\n\x12\x64\x63\x64\x63\x31\x32_temperature\x18\x03 \x01(\r\x12\x1a\n\x12\x64\x63\x64\x63\x32\x34_temperature\x18\x04 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x05 \x01(\x04\"\x7f\n\x0e\x43OOLING_STATUS\x12 \n\x18inverters_radiator_speed\x18\x01 \x01(\r\x12\x1d\n\x15motors_radiator_speed\x18\x02 \x01(\r\x12\x12\n\npump_speed\x18\x03 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x04 \x01(\x04\"X\n\x12SET_RADIATOR_SPEED\x12(\n\x0eradiator_speed\x18\x01 \x01(\x0e\x32\x10.primary.Cooling\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"R\n\x0fSET_PUMPS_SPEED\x12%\n\x0bpumps_speed\x18\x01 \x01(\x0e\x32\x10.primary.Cooling\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"[\n\x1eSET_INVERTER_CONNECTION_STATUS\x12\x1f\n\x06status\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"W\n\x1aINVERTER_CONNECTION_STATUS\x12\x1f\n\x06status\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"D\n\x0fSHUTDOWN_STATUS\x12\n\n\x02in\x18\x01 \x01(\x08\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x08\x12\x18\n\x10_inner_timestamp\x18\x03 \x01(\x04\"\"\n\x06MARKER\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"z\n\x10HV_CELLS_VOLTAGE\x12\x11\n\tvoltage_0\x18\x01 \x01(\r\x12\x11\n\tvoltage_1\x18\x02 \x01(\r\x12\x11\n\tvoltage_2\x18\x03 \x01(\r\x12\x13\n\x0bstart_index\x18\x04 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x05 \x01(\x04\"\xae\x01\n\rHV_CELLS_TEMP\x12\x13\n\x0bstart_index\x18\x01 \x01(\r\x12\x0e\n\x06temp_0\x18\x02 \x01(\r\x12\x0e\n\x06temp_1\x18\x03 \x01(\r\x12\x0e\n\x06temp_2\x18\x04 \x01(\r\x12\x0e\n\x06temp_3\x18\x05 \x01(\r\x12\x0e\n\x06temp_4\x18\x06 \x01(\r\x12\x0e\n\x06temp_5\x18\x07 \x01(\r\x12\x0e\n\x06temp_6\x18\x08 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\t \x01(\x04\"_\n\x18HV_CELL_BALANCING_STATUS\x12)\n\x10\x62\x61lancing_status\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"d\n\x19SET_CELL_BALANCING_STATUS\x12-\n\x14set_balancing_status\x18\x01 \x01(\x0e\x32\x0f.primary.Toggle\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\">\n\x0fHANDCART_STATUS\x12\x11\n\tconnected\x18\x01 \x01(\x08\x12\x18\n\x10_inner_timestamp\x18\x02 \x01(\x04\"o\n\x05SPEED\x12\x11\n\tencoder_r\x18\x01 \x01(\r\x12\x11\n\tencoder_l\x18\x02 \x01(\r\x12\x12\n\ninverter_r\x18\x03 \x01(\r\x12\x12\n\ninverter_l\x18\x04 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\x05 \x01(\x04\"\xa9\x01\n\rINV_L_REQUEST\x12\x0e\n\x06\x64\x61ta_0\x18\x01 \x01(\r\x12\x0e\n\x06\x64\x61ta_1\x18\x02 \x01(\r\x12\x0e\n\x06\x64\x61ta_2\x18\x03 \x01(\r\x12\x0e\n\x06\x64\x61ta_3\x18\x04 \x01(\r\x12\x0e\n\x06\x64\x61ta_4\x18\x05 \x01(\r\x12\x0e\n\x06\x64\x61ta_5\x18\x06 \x01(\r\x12\x0e\n\x06\x64\x61ta_6\x18\x07 \x01(\r\x12\x0e\n\x06\x64\x61ta_7\x18\x08 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\t \x01(\x04\"\xa9\x01\n\rINV_R_REQUEST\x12\x0e\n\x06\x64\x61ta_0\x18\x01 \x01(\r\x12\x0e\n\x06\x64\x61ta_1\x18\x02 \x01(\r\x12\x0e\n\x06\x64\x61ta_2\x18\x03 \x01(\r\x12\x0e\n\x06\x64\x61ta_3\x18\x04 \x01(\r\x12\x0e\n\x06\x64\x61ta_4\x18\x05 \x01(\r\x12\x0e\n\x06\x64\x61ta_5\x18\x06 \x01(\r\x12\x0e\n\x06\x64\x61ta_6\x18\x07 \x01(\r\x12\x0e\n\x06\x64\x61ta_7\x18\x08 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\t \x01(\x04\"\xaa\x01\n\x0eINV_L_RESPONSE\x12\x0e\n\x06reg_id\x18\x01 \x01(\r\x12\x0e\n\x06\x64\x61ta_0\x18\x02 \x01(\r\x12\x0e\n\x06\x64\x61ta_1\x18\x03 \x01(\r\x12\x0e\n\x06\x64\x61ta_2\x18\x04 \x01(\r\x12\x0e\n\x06\x64\x61ta_3\x18\x05 \x01(\r\x12\x0e\n\x06\x64\x61ta_4\x18\x06 \x01(\r\x12\x0e\n\x06\x64\x61ta_5\x18\x07 \x01(\r\x12\x0e\n\x06\x64\x61ta_6\x18\x08 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\t \x01(\x04\"\xaa\x01\n\x0eINV_R_RESPONSE\x12\x0e\n\x06reg_id\x18\x01 \x01(\r\x12\x0e\n\x06\x64\x61ta_0\x18\x02 \x01(\r\x12\x0e\n\x06\x64\x61ta_1\x18\x03 \x01(\r\x12\x0e\n\x06\x64\x61ta_2\x18\x04 \x01(\r\x12\x0e\n\x06\x64\x61ta_3\x18\x05 \x01(\r\x12\x0e\n\x06\x64\x61ta_4\x18\x06 \x01(\r\x12\x0e\n\x06\x64\x61ta_5\x18\x07 \x01(\r\x12\x0e\n\x06\x64\x61ta_6\x18\x08 \x01(\r\x12\x18\n\x10_inner_timestamp\x18\t \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_0_TX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_0_RX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_1_TX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_1_RX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_2_TX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_2_RX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_3_TX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_3_RX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_4_TX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_4_RX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_5_TX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"0\n\x14\x46LASH_CELLBOARD_5_RX\x12\x18\n\x10_inner_timestamp\x18\x01 \x01(\x04\"\xc6\x17\n\x04Pack\x12\x35\n\x11\x42MS_HV_JMP_TO_BLT\x18\x01 \x03(\x0b\x32\x1a.primary.BMS_HV_JMP_TO_BLT\x12-\n\rSTEER_VERSION\x18\x02 \x03(\x0b\x32\x16.primary.STEER_VERSION\x12)\n\x0b\x44\x41S_VERSION\x18\x03 \x03(\x0b\x32\x14.primary.DAS_VERSION\x12\'\n\nHV_VERSION\x18\x04 \x03(\x0b\x32\x13.primary.HV_VERSION\x12\'\n\nLV_VERSION\x18\x05 \x03(\x0b\x32\x13.primary.LV_VERSION\x12)\n\x0bTLM_VERSION\x18\x06 \x03(\x0b\x32\x14.primary.TLM_VERSION\x12%\n\tTIMESTAMP\x18\x07 \x03(\x0b\x32\x12.primary.TIMESTAMP\x12/\n\x0eSET_TLM_STATUS\x18\x08 \x03(\x0b\x32\x17.primary.SET_TLM_STATUS\x12\'\n\nTLM_STATUS\x18\t \x03(\x0b\x32\x13.primary.TLM_STATUS\x12\x39\n\x13STEER_SYSTEM_STATUS\x18\n \x03(\x0b\x32\x1c.primary.STEER_SYSTEM_STATUS\x12\'\n\nHV_VOLTAGE\x18\x0b \x03(\x0b\x32\x13.primary.HV_VOLTAGE\x12\'\n\nHV_CURRENT\x18\x0c \x03(\x0b\x32\x13.primary.HV_CURRENT\x12!\n\x07HV_TEMP\x18\r \x03(\x0b\x32\x10.primary.HV_TEMP\x12%\n\tHV_ERRORS\x18\x0e \x03(\x0b\x32\x12.primary.HV_ERRORS\x12/\n\x0eHV_CAN_FORWARD\x18\x0f \x03(\x0b\x32\x17.primary.HV_CAN_FORWARD\x12=\n\x15HV_CAN_FORWARD_STATUS\x18\x10 \x03(\x0b\x32\x1e.primary.HV_CAN_FORWARD_STATUS\x12%\n\tTS_STATUS\x18\x11 \x03(\x0b\x32\x12.primary.TS_STATUS\x12\x35\n\x11SET_TS_STATUS_DAS\x18\x12 \x03(\x0b\x32\x1a.primary.SET_TS_STATUS_DAS\x12?\n\x16SET_TS_STATUS_HANDCART\x18\x13 \x03(\x0b\x32\x1f.primary.SET_TS_STATUS_HANDCART\x12+\n\x0cSTEER_STATUS\x18\x14 \x03(\x0b\x32\x15.primary.STEER_STATUS\x12/\n\x0eSET_CAR_STATUS\x18\x15 \x03(\x0b\x32\x17.primary.SET_CAR_STATUS\x12\x33\n\x10SET_PEDALS_RANGE\x18\x16 \x03(\x0b\x32\x19.primary.SET_PEDALS_RANGE\x12\x43\n\x18SET_STEERING_ANGLE_RANGE\x18\x17 \x03(\x0b\x32!.primary.SET_STEERING_ANGLE_RANGE\x12\'\n\nCAR_STATUS\x18\x18 \x03(\x0b\x32\x13.primary.CAR_STATUS\x12\'\n\nDAS_ERRORS\x18\x19 \x03(\x0b\x32\x13.primary.DAS_ERRORS\x12\'\n\nLV_CURRENT\x18\x1a \x03(\x0b\x32\x13.primary.LV_CURRENT\x12\'\n\nLV_VOLTAGE\x18\x1b \x03(\x0b\x32\x13.primary.LV_VOLTAGE\x12\x33\n\x10LV_TOTAL_VOLTAGE\x18\x1c \x03(\x0b\x32\x19.primary.LV_TOTAL_VOLTAGE\x12/\n\x0eLV_TEMPERATURE\x18\x1d \x03(\x0b\x32\x17.primary.LV_TEMPERATURE\x12/\n\x0e\x43OOLING_STATUS\x18\x1e \x03(\x0b\x32\x17.primary.COOLING_STATUS\x12\x37\n\x12SET_RADIATOR_SPEED\x18\x1f \x03(\x0b\x32\x1b.primary.SET_RADIATOR_SPEED\x12\x31\n\x0fSET_PUMPS_SPEED\x18  \x03(\x0b\x32\x18.primary.SET_PUMPS_SPEED\x12O\n\x1eSET_INVERTER_CONNECTION_STATUS\x18! \x03(\x0b\x32\'.primary.SET_INVERTER_CONNECTION_STATUS\x12G\n\x1aINVERTER_CONNECTION_STATUS\x18\" \x03(\x0b\x32#.primary.INVERTER_CONNECTION_STATUS\x12\x31\n\x0fSHUTDOWN_STATUS\x18# \x03(\x0b\x32\x18.primary.SHUTDOWN_STATUS\x12\x1f\n\x06MARKER\x18$ \x03(\x0b\x32\x0f.primary.MARKER\x12\x33\n\x10HV_CELLS_VOLTAGE\x18% \x03(\x0b\x32\x19.primary.HV_CELLS_VOLTAGE\x12-\n\rHV_CELLS_TEMP\x18& \x03(\x0b\x32\x16.primary.HV_CELLS_TEMP\x12\x43\n\x18HV_CELL_BALANCING_STATUS\x18\' \x03(\x0b\x32!.primary.HV_CELL_BALANCING_STATUS\x12\x45\n\x19SET_CELL_BALANCING_STATUS\x18( \x03(\x0b\x32\".primary.SET_CELL_BALANCING_STATUS\x12\x31\n\x0fHANDCART_STATUS\x18) \x03(\x0b\x32\x18.primary.HANDCART_STATUS\x12\x1d\n\x05SPEED\x18* \x03(\x0b\x32\x0e.primary.SPEED\x12-\n\rINV_L_REQUEST\x18+ \x03(\x0b\x32\x16.primary.INV_L_REQUEST\x12-\n\rINV_R_REQUEST\x18, \x03(\x0b\x32\x16.primary.INV_R_REQUEST\x12/\n\x0eINV_L_RESPONSE\x18- \x03(\x0b\x32\x17.primary.INV_L_RESPONSE\x12/\n\x0eINV_R_RESPONSE\x18. \x03(\x0b\x32\x17.primary.INV_R_RESPONSE\x12;\n\x14\x46LASH_CELLBOARD_0_TX\x18/ \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_0_TX\x12;\n\x14\x46LASH_CELLBOARD_0_RX\x18\x30 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_0_RX\x12;\n\x14\x46LASH_CELLBOARD_1_TX\x18\x31 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_1_TX\x12;\n\x14\x46LASH_CELLBOARD_1_RX\x18\x32 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_1_RX\x12;\n\x14\x46LASH_CELLBOARD_2_TX\x18\x33 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_2_TX\x12;\n\x14\x46LASH_CELLBOARD_2_RX\x18\x34 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_2_RX\x12;\n\x14\x46LASH_CELLBOARD_3_TX\x18\x35 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_3_TX\x12;\n\x14\x46LASH_CELLBOARD_3_RX\x18\x36 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_3_RX\x12;\n\x14\x46LASH_CELLBOARD_4_TX\x18\x37 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_4_TX\x12;\n\x14\x46LASH_CELLBOARD_4_RX\x18\x38 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_4_RX\x12;\n\x14\x46LASH_CELLBOARD_5_TX\x18\x39 \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_5_TX\x12;\n\x14\x46LASH_CELLBOARD_5_RX\x18: \x03(\x0b\x32\x1d.primary.FLASH_CELLBOARD_5_RX*k\n\x08RaceType\x12\x19\n\x15RaceType_ACCELERATION\x10\x00\x12\x14\n\x10RaceType_SKIDPAD\x10\x01\x12\x16\n\x12RaceType_AUTOCROSS\x10\x02\x12\x16\n\x12RaceType_ENDURANCE\x10\x03*X\n\x0eInverterStatus\x12\x16\n\x12InverterStatus_OFF\x10\x00\x12\x17\n\x13InverterStatus_IDLE\x10\x01\x12\x15\n\x11InverterStatus_ON\x10\x02*G\n\tCarStatus\x12\x12\n\x0e\x43\x61rStatus_IDLE\x10\x00\x12\x13\n\x0f\x43\x61rStatus_SETUP\x10\x01\x12\x11\n\rCarStatus_RUN\x10\x02*\'\n\x06Toggle\x12\r\n\tToggle_ON\x10\x00\x12\x0e\n\nToggle_OFF\x10\x01*\x90\x01\n\x0fTractionControl\x12\x17\n\x13TractionControl_OFF\x10\x00\x12 \n\x1cTractionControl_SLIP_CONTROL\x10\x01\x12$\n TractionControl_TORQUE_VECTORING\x10\x02\x12\x1c\n\x18TractionControl_COMPLETE\x10\x03*Y\n\x08TsStatus\x12\x10\n\x0cTsStatus_OFF\x10\x00\x12\x16\n\x12TsStatus_PRECHARGE\x10\x01\x12\x0f\n\x0bTsStatus_ON\x10\x02\x12\x12\n\x0eTsStatus_FATAL\x10\x03*R\n\x03Map\x12\t\n\x05Map_R\x10\x00\x12\x0b\n\x07Map_D20\x10\x01\x12\x0b\n\x07Map_D40\x10\x02\x12\x0b\n\x07Map_D60\x10\x03\x12\x0b\n\x07Map_D80\x10\x04\x12\x0c\n\x08Map_D100\x10\x05*;\n\x0cSetCarStatus\x12\x15\n\x11SetCarStatus_IDLE\x10\x00\x12\x14\n\x10SetCarStatus_RUN\x10\x01*-\n\x05\x42ound\x12\x11\n\rBound_SET_MAX\x10\x00\x12\x11\n\rBound_SET_MIN\x10\x01*/\n\x05Pedal\x12\x15\n\x11Pedal_ACCELERATOR\x10\x00\x12\x0f\n\x0bPedal_BRAKE\x10\x01*+\n\x07\x43ooling\x12\x0f\n\x0b\x43ooling_MAX\x10\x00\x12\x0f\n\x0b\x43ooling_OFF\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'primary_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RACETYPE._serialized_start=8384
  _RACETYPE._serialized_end=8491
  _INVERTERSTATUS._serialized_start=8493
  _INVERTERSTATUS._serialized_end=8581
  _CARSTATUS._serialized_start=8583
  _CARSTATUS._serialized_end=8654
  _TOGGLE._serialized_start=8656
  _TOGGLE._serialized_end=8695
  _TRACTIONCONTROL._serialized_start=8698
  _TRACTIONCONTROL._serialized_end=8842
  _TSSTATUS._serialized_start=8844
  _TSSTATUS._serialized_end=8933
  _MAP._serialized_start=8935
  _MAP._serialized_end=9017
  _SETCARSTATUS._serialized_start=9019
  _SETCARSTATUS._serialized_end=9078
  _BOUND._serialized_start=9080
  _BOUND._serialized_end=9125
  _PEDAL._serialized_start=9127
  _PEDAL._serialized_end=9174
  _COOLING._serialized_start=9176
  _COOLING._serialized_end=9219
  _BMS_HV_JMP_TO_BLT._serialized_start=26
  _BMS_HV_JMP_TO_BLT._serialized_end=71
  _STEER_VERSION._serialized_start=73
  _STEER_VERSION._serialized_end=166
  _DAS_VERSION._serialized_start=168
  _DAS_VERSION._serialized_end=259
  _HV_VERSION._serialized_start=261
  _HV_VERSION._serialized_end=351
  _LV_VERSION._serialized_start=353
  _LV_VERSION._serialized_end=443
  _TLM_VERSION._serialized_start=445
  _TLM_VERSION._serialized_end=536
  _TIMESTAMP._serialized_start=538
  _TIMESTAMP._serialized_end=594
  _SET_TLM_STATUS._serialized_start=597
  _SET_TLM_STATUS._serialized_end=747
  _TLM_STATUS._serialized_start=750
  _TLM_STATUS._serialized_end=896
  _STEER_SYSTEM_STATUS._serialized_start=898
  _STEER_SYSTEM_STATUS._serialized_end=963
  _HV_VOLTAGE._serialized_start=966
  _HV_VOLTAGE._serialized_end=1099
  _HV_CURRENT._serialized_start=1101
  _HV_CURRENT._serialized_end=1171
  _HV_TEMP._serialized_start=1173
  _HV_TEMP._serialized_end=1266
  _HV_ERRORS._serialized_start=1268
  _HV_ERRORS._serialized_end=1339
  _HV_CAN_FORWARD._serialized_start=1341
  _HV_CAN_FORWARD._serialized_end=1425
  _HV_CAN_FORWARD_STATUS._serialized_start=1427
  _HV_CAN_FORWARD_STATUS._serialized_end=1521
  _TS_STATUS._serialized_start=1523
  _TS_STATUS._serialized_end=1598
  _SET_TS_STATUS_DAS._serialized_start=1600
  _SET_TS_STATUS_DAS._serialized_end=1685
  _SET_TS_STATUS_HANDCART._serialized_start=1687
  _SET_TS_STATUS_HANDCART._serialized_end=1777
  _STEER_STATUS._serialized_start=1779
  _STEER_STATUS._serialized_end=1898
  _SET_CAR_STATUS._serialized_start=1900
  _SET_CAR_STATUS._serialized_end=1989
  _SET_PEDALS_RANGE._serialized_start=1991
  _SET_PEDALS_RANGE._serialized_end=2097
  _SET_STEERING_ANGLE_RANGE._serialized_start=2099
  _SET_STEERING_ANGLE_RANGE._serialized_end=2182
  _CAR_STATUS._serialized_start=2185
  _CAR_STATUS._serialized_end=2353
  _DAS_ERRORS._serialized_start=2355
  _DAS_ERRORS._serialized_end=2412
  _LV_CURRENT._serialized_start=2414
  _LV_CURRENT._serialized_end=2469
  _LV_VOLTAGE._serialized_start=2471
  _LV_VOLTAGE._serialized_end=2585
  _LV_TOTAL_VOLTAGE._serialized_start=2587
  _LV_TOTAL_VOLTAGE._serialized_end=2654
  _LV_TEMPERATURE._serialized_start=2657
  _LV_TEMPERATURE._serialized_end=2807
  _COOLING_STATUS._serialized_start=2809
  _COOLING_STATUS._serialized_end=2936
  _SET_RADIATOR_SPEED._serialized_start=2938
  _SET_RADIATOR_SPEED._serialized_end=3026
  _SET_PUMPS_SPEED._serialized_start=3028
  _SET_PUMPS_SPEED._serialized_end=3110
  _SET_INVERTER_CONNECTION_STATUS._serialized_start=3112
  _SET_INVERTER_CONNECTION_STATUS._serialized_end=3203
  _INVERTER_CONNECTION_STATUS._serialized_start=3205
  _INVERTER_CONNECTION_STATUS._serialized_end=3292
  _SHUTDOWN_STATUS._serialized_start=3294
  _SHUTDOWN_STATUS._serialized_end=3362
  _MARKER._serialized_start=3364
  _MARKER._serialized_end=3398
  _HV_CELLS_VOLTAGE._serialized_start=3400
  _HV_CELLS_VOLTAGE._serialized_end=3522
  _HV_CELLS_TEMP._serialized_start=3525
  _HV_CELLS_TEMP._serialized_end=3699
  _HV_CELL_BALANCING_STATUS._serialized_start=3701
  _HV_CELL_BALANCING_STATUS._serialized_end=3796
  _SET_CELL_BALANCING_STATUS._serialized_start=3798
  _SET_CELL_BALANCING_STATUS._serialized_end=3898
  _HANDCART_STATUS._serialized_start=3900
  _HANDCART_STATUS._serialized_end=3962
  _SPEED._serialized_start=3964
  _SPEED._serialized_end=4075
  _INV_L_REQUEST._serialized_start=4078
  _INV_L_REQUEST._serialized_end=4247
  _INV_R_REQUEST._serialized_start=4250
  _INV_R_REQUEST._serialized_end=4419
  _INV_L_RESPONSE._serialized_start=4422
  _INV_L_RESPONSE._serialized_end=4592
  _INV_R_RESPONSE._serialized_start=4595
  _INV_R_RESPONSE._serialized_end=4765
  _FLASH_CELLBOARD_0_TX._serialized_start=4767
  _FLASH_CELLBOARD_0_TX._serialized_end=4815
  _FLASH_CELLBOARD_0_RX._serialized_start=4817
  _FLASH_CELLBOARD_0_RX._serialized_end=4865
  _FLASH_CELLBOARD_1_TX._serialized_start=4867
  _FLASH_CELLBOARD_1_TX._serialized_end=4915
  _FLASH_CELLBOARD_1_RX._serialized_start=4917
  _FLASH_CELLBOARD_1_RX._serialized_end=4965
  _FLASH_CELLBOARD_2_TX._serialized_start=4967
  _FLASH_CELLBOARD_2_TX._serialized_end=5015
  _FLASH_CELLBOARD_2_RX._serialized_start=5017
  _FLASH_CELLBOARD_2_RX._serialized_end=5065
  _FLASH_CELLBOARD_3_TX._serialized_start=5067
  _FLASH_CELLBOARD_3_TX._serialized_end=5115
  _FLASH_CELLBOARD_3_RX._serialized_start=5117
  _FLASH_CELLBOARD_3_RX._serialized_end=5165
  _FLASH_CELLBOARD_4_TX._serialized_start=5167
  _FLASH_CELLBOARD_4_TX._serialized_end=5215
  _FLASH_CELLBOARD_4_RX._serialized_start=5217
  _FLASH_CELLBOARD_4_RX._serialized_end=5265
  _FLASH_CELLBOARD_5_TX._serialized_start=5267
  _FLASH_CELLBOARD_5_TX._serialized_end=5315
  _FLASH_CELLBOARD_5_RX._serialized_start=5317
  _FLASH_CELLBOARD_5_RX._serialized_end=5365
  _PACK._serialized_start=5368
  _PACK._serialized_end=8382
# @@protoc_insertion_point(module_scope)
