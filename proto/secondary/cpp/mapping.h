#ifndef secondary_MAPPING_H
#define secondary_MAPPING_H

#include <string>
#include <vector>

#include "secondary.pb.h"

#ifdef secondary_IMPLEMENTATION
#undef secondary_IMPLEMENTATION
#define __secondary_IMPLEMENTATION
#endif

#include "../../../lib/secondary/c/network.h"

#ifdef __secondary_IMPLEMENTATION
#undef __secondary_IMPLEMENTATION
#define secondary_IMPLEMENTATION
#endif

#ifndef CANLIB_MESSAGE_ID_TYPE
#define CANLIB_MESSAGE_ID_TYPE
typedef uint16_t canlib_message_id;
#endif // CANLIB_MESSAGE_ID_TYPE

typedef struct {
    std::vector<secondary_message_IMU_ANGULAR_RATE> IMU_ANGULAR_RATE;
    std::vector<secondary_message_IMU_ACCELERATION> IMU_ACCELERATION;
    std::vector<secondary_message_IRTS_FL_0> IRTS_FL_0;
    std::vector<secondary_message_IRTS_FL_1> IRTS_FL_1;
    std::vector<secondary_message_IRTS_FL_2> IRTS_FL_2;
    std::vector<secondary_message_IRTS_FL_3> IRTS_FL_3;
    std::vector<secondary_message_IRTS_FR_0> IRTS_FR_0;
    std::vector<secondary_message_IRTS_FR_1> IRTS_FR_1;
    std::vector<secondary_message_IRTS_FR_2> IRTS_FR_2;
    std::vector<secondary_message_IRTS_FR_3> IRTS_FR_3;
    std::vector<secondary_message_IRTS_RL_0> IRTS_RL_0;
    std::vector<secondary_message_IRTS_RL_1> IRTS_RL_1;
    std::vector<secondary_message_IRTS_RL_2> IRTS_RL_2;
    std::vector<secondary_message_IRTS_RL_3> IRTS_RL_3;
    std::vector<secondary_message_IRTS_RR_0> IRTS_RR_0;
    std::vector<secondary_message_IRTS_RR_1> IRTS_RR_1;
    std::vector<secondary_message_IRTS_RR_2> IRTS_RR_2;
    std::vector<secondary_message_IRTS_RR_3> IRTS_RR_3;
    std::vector<secondary_message_GPS_COORDS> GPS_COORDS;
    std::vector<secondary_message_GPS_SPEED> GPS_SPEED;
    std::vector<secondary_message_LAP_COUNT> LAP_COUNT;
    std::vector<secondary_message_PEDALS_OUTPUT_conversion> PEDALS_OUTPUT;
    std::vector<secondary_message_CONTROL_OUTPUT> CONTROL_OUTPUT;
    std::vector<secondary_message_STEERING_ANGLE> STEERING_ANGLE;
} secondary_proto_pack;

void secondary_proto_serialize_from_id(canlib_message_id id, secondary::Pack* pack, secondary_devices* map);
void secondary_proto_deserialize(secondary::Pack* pack, secondary_proto_pack* map);

#ifdef secondary_MAPPING_IMPLEMENTATION

void secondary_proto_serialize_from_id(canlib_message_id id, secondary::Pack* pack, secondary_devices* map) {
    int index = secondary_index_from_id(id);

    if (index == -1) return;

    switch(id) {
        case 1260: {
            secondary_message_IMU_ANGULAR_RATE* msg = (secondary_message_IMU_ANGULAR_RATE*) (*map)[index].message_raw;
            secondary::IMU_ANGULAR_RATE* proto_msg = pack->add_imu_angular_rate();
            proto_msg->set_ang_rate_x(msg->ang_rate_x);
            proto_msg->set_ang_rate_y(msg->ang_rate_y);
            proto_msg->set_ang_rate_z(msg->ang_rate_z);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1261: {
            secondary_message_IMU_ACCELERATION* msg = (secondary_message_IMU_ACCELERATION*) (*map)[index].message_raw;
            secondary::IMU_ACCELERATION* proto_msg = pack->add_imu_acceleration();
            proto_msg->set_accel_x(msg->accel_x);
            proto_msg->set_accel_y(msg->accel_y);
            proto_msg->set_accel_z(msg->accel_z);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1460: {
            secondary_message_IRTS_FL_0* msg = (secondary_message_IRTS_FL_0*) (*map)[index].message_raw;
            secondary::IRTS_FL_0* proto_msg = pack->add_irts_fl_0();
            proto_msg->set_channel1(msg->channel1);
            proto_msg->set_channel2(msg->channel2);
            proto_msg->set_channel3(msg->channel3);
            proto_msg->set_channel4(msg->channel4);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1461: {
            secondary_message_IRTS_FL_1* msg = (secondary_message_IRTS_FL_1*) (*map)[index].message_raw;
            secondary::IRTS_FL_1* proto_msg = pack->add_irts_fl_1();
            proto_msg->set_channel5(msg->channel5);
            proto_msg->set_channel6(msg->channel6);
            proto_msg->set_channel7(msg->channel7);
            proto_msg->set_channel8(msg->channel8);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1462: {
            secondary_message_IRTS_FL_2* msg = (secondary_message_IRTS_FL_2*) (*map)[index].message_raw;
            secondary::IRTS_FL_2* proto_msg = pack->add_irts_fl_2();
            proto_msg->set_channel9(msg->channel9);
            proto_msg->set_channel10(msg->channel10);
            proto_msg->set_channel11(msg->channel11);
            proto_msg->set_channel12(msg->channel12);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1463: {
            secondary_message_IRTS_FL_3* msg = (secondary_message_IRTS_FL_3*) (*map)[index].message_raw;
            secondary::IRTS_FL_3* proto_msg = pack->add_irts_fl_3();
            proto_msg->set_channel13(msg->channel13);
            proto_msg->set_channel14(msg->channel14);
            proto_msg->set_channel15(msg->channel15);
            proto_msg->set_channel16(msg->channel16);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1464: {
            secondary_message_IRTS_FR_0* msg = (secondary_message_IRTS_FR_0*) (*map)[index].message_raw;
            secondary::IRTS_FR_0* proto_msg = pack->add_irts_fr_0();
            proto_msg->set_channel1(msg->channel1);
            proto_msg->set_channel2(msg->channel2);
            proto_msg->set_channel3(msg->channel3);
            proto_msg->set_channel4(msg->channel4);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1465: {
            secondary_message_IRTS_FR_1* msg = (secondary_message_IRTS_FR_1*) (*map)[index].message_raw;
            secondary::IRTS_FR_1* proto_msg = pack->add_irts_fr_1();
            proto_msg->set_channel5(msg->channel5);
            proto_msg->set_channel6(msg->channel6);
            proto_msg->set_channel7(msg->channel7);
            proto_msg->set_channel8(msg->channel8);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1466: {
            secondary_message_IRTS_FR_2* msg = (secondary_message_IRTS_FR_2*) (*map)[index].message_raw;
            secondary::IRTS_FR_2* proto_msg = pack->add_irts_fr_2();
            proto_msg->set_channel9(msg->channel9);
            proto_msg->set_channel10(msg->channel10);
            proto_msg->set_channel11(msg->channel11);
            proto_msg->set_channel12(msg->channel12);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1467: {
            secondary_message_IRTS_FR_3* msg = (secondary_message_IRTS_FR_3*) (*map)[index].message_raw;
            secondary::IRTS_FR_3* proto_msg = pack->add_irts_fr_3();
            proto_msg->set_channel13(msg->channel13);
            proto_msg->set_channel14(msg->channel14);
            proto_msg->set_channel15(msg->channel15);
            proto_msg->set_channel16(msg->channel16);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1468: {
            secondary_message_IRTS_RL_0* msg = (secondary_message_IRTS_RL_0*) (*map)[index].message_raw;
            secondary::IRTS_RL_0* proto_msg = pack->add_irts_rl_0();
            proto_msg->set_channel1(msg->channel1);
            proto_msg->set_channel2(msg->channel2);
            proto_msg->set_channel3(msg->channel3);
            proto_msg->set_channel4(msg->channel4);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1469: {
            secondary_message_IRTS_RL_1* msg = (secondary_message_IRTS_RL_1*) (*map)[index].message_raw;
            secondary::IRTS_RL_1* proto_msg = pack->add_irts_rl_1();
            proto_msg->set_channel5(msg->channel5);
            proto_msg->set_channel6(msg->channel6);
            proto_msg->set_channel7(msg->channel7);
            proto_msg->set_channel8(msg->channel8);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1470: {
            secondary_message_IRTS_RL_2* msg = (secondary_message_IRTS_RL_2*) (*map)[index].message_raw;
            secondary::IRTS_RL_2* proto_msg = pack->add_irts_rl_2();
            proto_msg->set_channel9(msg->channel9);
            proto_msg->set_channel10(msg->channel10);
            proto_msg->set_channel11(msg->channel11);
            proto_msg->set_channel12(msg->channel12);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1471: {
            secondary_message_IRTS_RL_3* msg = (secondary_message_IRTS_RL_3*) (*map)[index].message_raw;
            secondary::IRTS_RL_3* proto_msg = pack->add_irts_rl_3();
            proto_msg->set_channel13(msg->channel13);
            proto_msg->set_channel14(msg->channel14);
            proto_msg->set_channel15(msg->channel15);
            proto_msg->set_channel16(msg->channel16);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1472: {
            secondary_message_IRTS_RR_0* msg = (secondary_message_IRTS_RR_0*) (*map)[index].message_raw;
            secondary::IRTS_RR_0* proto_msg = pack->add_irts_rr_0();
            proto_msg->set_channel1(msg->channel1);
            proto_msg->set_channel2(msg->channel2);
            proto_msg->set_channel3(msg->channel3);
            proto_msg->set_channel4(msg->channel4);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1473: {
            secondary_message_IRTS_RR_1* msg = (secondary_message_IRTS_RR_1*) (*map)[index].message_raw;
            secondary::IRTS_RR_1* proto_msg = pack->add_irts_rr_1();
            proto_msg->set_channel5(msg->channel5);
            proto_msg->set_channel6(msg->channel6);
            proto_msg->set_channel7(msg->channel7);
            proto_msg->set_channel8(msg->channel8);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1474: {
            secondary_message_IRTS_RR_2* msg = (secondary_message_IRTS_RR_2*) (*map)[index].message_raw;
            secondary::IRTS_RR_2* proto_msg = pack->add_irts_rr_2();
            proto_msg->set_channel9(msg->channel9);
            proto_msg->set_channel10(msg->channel10);
            proto_msg->set_channel11(msg->channel11);
            proto_msg->set_channel12(msg->channel12);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1475: {
            secondary_message_IRTS_RR_3* msg = (secondary_message_IRTS_RR_3*) (*map)[index].message_raw;
            secondary::IRTS_RR_3* proto_msg = pack->add_irts_rr_3();
            proto_msg->set_channel13(msg->channel13);
            proto_msg->set_channel14(msg->channel14);
            proto_msg->set_channel15(msg->channel15);
            proto_msg->set_channel16(msg->channel16);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1025: {
            secondary_message_GPS_COORDS* msg = (secondary_message_GPS_COORDS*) (*map)[index].message_raw;
            secondary::GPS_COORDS* proto_msg = pack->add_gps_coords();
            proto_msg->set_latitude(msg->latitude);
            proto_msg->set_longitude(msg->longitude);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1057: {
            secondary_message_GPS_SPEED* msg = (secondary_message_GPS_SPEED*) (*map)[index].message_raw;
            secondary::GPS_SPEED* proto_msg = pack->add_gps_speed();
            proto_msg->set_speed(msg->speed);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 1089: {
            secondary_message_LAP_COUNT* msg = (secondary_message_LAP_COUNT*) (*map)[index].message_raw;
            secondary::LAP_COUNT* proto_msg = pack->add_lap_count();
            proto_msg->set_timestamp(msg->timestamp);
            proto_msg->set_lap_count(msg->lap_count);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 769: {
            secondary_message_PEDALS_OUTPUT_conversion* msg = (secondary_message_PEDALS_OUTPUT_conversion*) (*map)[index].message_conversion;
            secondary::PEDALS_OUTPUT* proto_msg = pack->add_pedals_output();
            proto_msg->set_bse_front(msg->bse_front);
            proto_msg->set_bse_rear(msg->bse_rear);
            proto_msg->set_apps(msg->apps);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 801: {
            secondary_message_CONTROL_OUTPUT* msg = (secondary_message_CONTROL_OUTPUT*) (*map)[index].message_raw;
            secondary::CONTROL_OUTPUT* proto_msg = pack->add_control_output();
            proto_msg->set_right(msg->right);
            proto_msg->set_left(msg->left);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

        case 258: {
            secondary_message_STEERING_ANGLE* msg = (secondary_message_STEERING_ANGLE*) (*map)[index].message_raw;
            secondary::STEERING_ANGLE* proto_msg = pack->add_steering_angle();
            proto_msg->set_angle(msg->angle);
#ifdef CANLIB_TIMESTAMP
            proto_msg->set__inner_timestamp(msg->_timestamp);
#endif // CANLIB_TIMESTAMP
            break;
        }

    }
}

void secondary_proto_deserialize(secondary::Pack* pack, secondary_proto_pack* map) {
    map->IMU_ANGULAR_RATE.resize(pack->imu_angular_rate_size());
    for(int i = 0; i < pack->imu_angular_rate_size(); i++){
        map->IMU_ANGULAR_RATE[i].ang_rate_x =pack->imu_angular_rate(i).ang_rate_x();
        map->IMU_ANGULAR_RATE[i].ang_rate_y =pack->imu_angular_rate(i).ang_rate_y();
        map->IMU_ANGULAR_RATE[i].ang_rate_z =pack->imu_angular_rate(i).ang_rate_z();
#ifdef CANLIB_TIMESTAMP
        map->IMU_ANGULAR_RATE[i]._timestamp = pack->imu_angular_rate(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IMU_ACCELERATION.resize(pack->imu_acceleration_size());
    for(int i = 0; i < pack->imu_acceleration_size(); i++){
        map->IMU_ACCELERATION[i].accel_x =pack->imu_acceleration(i).accel_x();
        map->IMU_ACCELERATION[i].accel_y =pack->imu_acceleration(i).accel_y();
        map->IMU_ACCELERATION[i].accel_z =pack->imu_acceleration(i).accel_z();
#ifdef CANLIB_TIMESTAMP
        map->IMU_ACCELERATION[i]._timestamp = pack->imu_acceleration(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FL_0.resize(pack->irts_fl_0_size());
    for(int i = 0; i < pack->irts_fl_0_size(); i++){
        map->IRTS_FL_0[i].channel1 =pack->irts_fl_0(i).channel1();
        map->IRTS_FL_0[i].channel2 =pack->irts_fl_0(i).channel2();
        map->IRTS_FL_0[i].channel3 =pack->irts_fl_0(i).channel3();
        map->IRTS_FL_0[i].channel4 =pack->irts_fl_0(i).channel4();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FL_0[i]._timestamp = pack->irts_fl_0(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FL_1.resize(pack->irts_fl_1_size());
    for(int i = 0; i < pack->irts_fl_1_size(); i++){
        map->IRTS_FL_1[i].channel5 =pack->irts_fl_1(i).channel5();
        map->IRTS_FL_1[i].channel6 =pack->irts_fl_1(i).channel6();
        map->IRTS_FL_1[i].channel7 =pack->irts_fl_1(i).channel7();
        map->IRTS_FL_1[i].channel8 =pack->irts_fl_1(i).channel8();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FL_1[i]._timestamp = pack->irts_fl_1(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FL_2.resize(pack->irts_fl_2_size());
    for(int i = 0; i < pack->irts_fl_2_size(); i++){
        map->IRTS_FL_2[i].channel9 =pack->irts_fl_2(i).channel9();
        map->IRTS_FL_2[i].channel10 =pack->irts_fl_2(i).channel10();
        map->IRTS_FL_2[i].channel11 =pack->irts_fl_2(i).channel11();
        map->IRTS_FL_2[i].channel12 =pack->irts_fl_2(i).channel12();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FL_2[i]._timestamp = pack->irts_fl_2(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FL_3.resize(pack->irts_fl_3_size());
    for(int i = 0; i < pack->irts_fl_3_size(); i++){
        map->IRTS_FL_3[i].channel13 =pack->irts_fl_3(i).channel13();
        map->IRTS_FL_3[i].channel14 =pack->irts_fl_3(i).channel14();
        map->IRTS_FL_3[i].channel15 =pack->irts_fl_3(i).channel15();
        map->IRTS_FL_3[i].channel16 =pack->irts_fl_3(i).channel16();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FL_3[i]._timestamp = pack->irts_fl_3(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FR_0.resize(pack->irts_fr_0_size());
    for(int i = 0; i < pack->irts_fr_0_size(); i++){
        map->IRTS_FR_0[i].channel1 =pack->irts_fr_0(i).channel1();
        map->IRTS_FR_0[i].channel2 =pack->irts_fr_0(i).channel2();
        map->IRTS_FR_0[i].channel3 =pack->irts_fr_0(i).channel3();
        map->IRTS_FR_0[i].channel4 =pack->irts_fr_0(i).channel4();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FR_0[i]._timestamp = pack->irts_fr_0(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FR_1.resize(pack->irts_fr_1_size());
    for(int i = 0; i < pack->irts_fr_1_size(); i++){
        map->IRTS_FR_1[i].channel5 =pack->irts_fr_1(i).channel5();
        map->IRTS_FR_1[i].channel6 =pack->irts_fr_1(i).channel6();
        map->IRTS_FR_1[i].channel7 =pack->irts_fr_1(i).channel7();
        map->IRTS_FR_1[i].channel8 =pack->irts_fr_1(i).channel8();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FR_1[i]._timestamp = pack->irts_fr_1(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FR_2.resize(pack->irts_fr_2_size());
    for(int i = 0; i < pack->irts_fr_2_size(); i++){
        map->IRTS_FR_2[i].channel9 =pack->irts_fr_2(i).channel9();
        map->IRTS_FR_2[i].channel10 =pack->irts_fr_2(i).channel10();
        map->IRTS_FR_2[i].channel11 =pack->irts_fr_2(i).channel11();
        map->IRTS_FR_2[i].channel12 =pack->irts_fr_2(i).channel12();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FR_2[i]._timestamp = pack->irts_fr_2(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_FR_3.resize(pack->irts_fr_3_size());
    for(int i = 0; i < pack->irts_fr_3_size(); i++){
        map->IRTS_FR_3[i].channel13 =pack->irts_fr_3(i).channel13();
        map->IRTS_FR_3[i].channel14 =pack->irts_fr_3(i).channel14();
        map->IRTS_FR_3[i].channel15 =pack->irts_fr_3(i).channel15();
        map->IRTS_FR_3[i].channel16 =pack->irts_fr_3(i).channel16();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_FR_3[i]._timestamp = pack->irts_fr_3(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RL_0.resize(pack->irts_rl_0_size());
    for(int i = 0; i < pack->irts_rl_0_size(); i++){
        map->IRTS_RL_0[i].channel1 =pack->irts_rl_0(i).channel1();
        map->IRTS_RL_0[i].channel2 =pack->irts_rl_0(i).channel2();
        map->IRTS_RL_0[i].channel3 =pack->irts_rl_0(i).channel3();
        map->IRTS_RL_0[i].channel4 =pack->irts_rl_0(i).channel4();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RL_0[i]._timestamp = pack->irts_rl_0(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RL_1.resize(pack->irts_rl_1_size());
    for(int i = 0; i < pack->irts_rl_1_size(); i++){
        map->IRTS_RL_1[i].channel5 =pack->irts_rl_1(i).channel5();
        map->IRTS_RL_1[i].channel6 =pack->irts_rl_1(i).channel6();
        map->IRTS_RL_1[i].channel7 =pack->irts_rl_1(i).channel7();
        map->IRTS_RL_1[i].channel8 =pack->irts_rl_1(i).channel8();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RL_1[i]._timestamp = pack->irts_rl_1(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RL_2.resize(pack->irts_rl_2_size());
    for(int i = 0; i < pack->irts_rl_2_size(); i++){
        map->IRTS_RL_2[i].channel9 =pack->irts_rl_2(i).channel9();
        map->IRTS_RL_2[i].channel10 =pack->irts_rl_2(i).channel10();
        map->IRTS_RL_2[i].channel11 =pack->irts_rl_2(i).channel11();
        map->IRTS_RL_2[i].channel12 =pack->irts_rl_2(i).channel12();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RL_2[i]._timestamp = pack->irts_rl_2(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RL_3.resize(pack->irts_rl_3_size());
    for(int i = 0; i < pack->irts_rl_3_size(); i++){
        map->IRTS_RL_3[i].channel13 =pack->irts_rl_3(i).channel13();
        map->IRTS_RL_3[i].channel14 =pack->irts_rl_3(i).channel14();
        map->IRTS_RL_3[i].channel15 =pack->irts_rl_3(i).channel15();
        map->IRTS_RL_3[i].channel16 =pack->irts_rl_3(i).channel16();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RL_3[i]._timestamp = pack->irts_rl_3(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RR_0.resize(pack->irts_rr_0_size());
    for(int i = 0; i < pack->irts_rr_0_size(); i++){
        map->IRTS_RR_0[i].channel1 =pack->irts_rr_0(i).channel1();
        map->IRTS_RR_0[i].channel2 =pack->irts_rr_0(i).channel2();
        map->IRTS_RR_0[i].channel3 =pack->irts_rr_0(i).channel3();
        map->IRTS_RR_0[i].channel4 =pack->irts_rr_0(i).channel4();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RR_0[i]._timestamp = pack->irts_rr_0(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RR_1.resize(pack->irts_rr_1_size());
    for(int i = 0; i < pack->irts_rr_1_size(); i++){
        map->IRTS_RR_1[i].channel5 =pack->irts_rr_1(i).channel5();
        map->IRTS_RR_1[i].channel6 =pack->irts_rr_1(i).channel6();
        map->IRTS_RR_1[i].channel7 =pack->irts_rr_1(i).channel7();
        map->IRTS_RR_1[i].channel8 =pack->irts_rr_1(i).channel8();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RR_1[i]._timestamp = pack->irts_rr_1(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RR_2.resize(pack->irts_rr_2_size());
    for(int i = 0; i < pack->irts_rr_2_size(); i++){
        map->IRTS_RR_2[i].channel9 =pack->irts_rr_2(i).channel9();
        map->IRTS_RR_2[i].channel10 =pack->irts_rr_2(i).channel10();
        map->IRTS_RR_2[i].channel11 =pack->irts_rr_2(i).channel11();
        map->IRTS_RR_2[i].channel12 =pack->irts_rr_2(i).channel12();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RR_2[i]._timestamp = pack->irts_rr_2(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->IRTS_RR_3.resize(pack->irts_rr_3_size());
    for(int i = 0; i < pack->irts_rr_3_size(); i++){
        map->IRTS_RR_3[i].channel13 =pack->irts_rr_3(i).channel13();
        map->IRTS_RR_3[i].channel14 =pack->irts_rr_3(i).channel14();
        map->IRTS_RR_3[i].channel15 =pack->irts_rr_3(i).channel15();
        map->IRTS_RR_3[i].channel16 =pack->irts_rr_3(i).channel16();
#ifdef CANLIB_TIMESTAMP
        map->IRTS_RR_3[i]._timestamp = pack->irts_rr_3(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->GPS_COORDS.resize(pack->gps_coords_size());
    for(int i = 0; i < pack->gps_coords_size(); i++){
        map->GPS_COORDS[i].latitude =pack->gps_coords(i).latitude();
        map->GPS_COORDS[i].longitude =pack->gps_coords(i).longitude();
#ifdef CANLIB_TIMESTAMP
        map->GPS_COORDS[i]._timestamp = pack->gps_coords(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->GPS_SPEED.resize(pack->gps_speed_size());
    for(int i = 0; i < pack->gps_speed_size(); i++){
        map->GPS_SPEED[i].speed =pack->gps_speed(i).speed();
#ifdef CANLIB_TIMESTAMP
        map->GPS_SPEED[i]._timestamp = pack->gps_speed(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->LAP_COUNT.resize(pack->lap_count_size());
    for(int i = 0; i < pack->lap_count_size(); i++){
        map->LAP_COUNT[i].timestamp =pack->lap_count(i).timestamp();
        map->LAP_COUNT[i].lap_count =pack->lap_count(i).lap_count();
#ifdef CANLIB_TIMESTAMP
        map->LAP_COUNT[i]._timestamp = pack->lap_count(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->PEDALS_OUTPUT.resize(pack->pedals_output_size());
    for(int i = 0; i < pack->pedals_output_size(); i++){
        map->PEDALS_OUTPUT[i].bse_front =pack->pedals_output(i).bse_front();
        map->PEDALS_OUTPUT[i].bse_rear =pack->pedals_output(i).bse_rear();
        map->PEDALS_OUTPUT[i].apps =pack->pedals_output(i).apps();
#ifdef CANLIB_TIMESTAMP
        map->PEDALS_OUTPUT[i]._timestamp = pack->pedals_output(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->CONTROL_OUTPUT.resize(pack->control_output_size());
    for(int i = 0; i < pack->control_output_size(); i++){
        map->CONTROL_OUTPUT[i].right =pack->control_output(i).right();
        map->CONTROL_OUTPUT[i].left =pack->control_output(i).left();
#ifdef CANLIB_TIMESTAMP
        map->CONTROL_OUTPUT[i]._timestamp = pack->control_output(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
    map->STEERING_ANGLE.resize(pack->steering_angle_size());
    for(int i = 0; i < pack->steering_angle_size(); i++){
        map->STEERING_ANGLE[i].angle =pack->steering_angle(i).angle();
#ifdef CANLIB_TIMESTAMP
        map->STEERING_ANGLE[i]._timestamp = pack->steering_angle(i)._inner_timestamp();
#endif // CANLIB_TIMESTAMP
    }
}

#endif // secondary_MAPPING_IMPLEMENTATION

#endif // secondary_MAPPING_H