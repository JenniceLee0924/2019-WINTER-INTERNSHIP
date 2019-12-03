#include <stdio.h>
#include <gtest/gtest.h>

#include "CanDataModel.h"

TEST(test_case_name, test_name) {
  EXPECT_EQ(0, CanDataModel( "Left_TurnStatus", "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( "Left_TurnStatus", "0x105", "0x1000000000000000"));
  
  EXPECT_EQ(0, CanDataModel( "Right_TurnStatus", "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( "Right_TurnStatus", "0x105", "0x2000000000000000"));

  EXPECT_EQ(0, CanDataModel( 'ParkingLight_Reminder', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'ParkingLight_Reminder', "0x105", "0x0800000000000000"));

  EXPECT_EQ(0, CanDataModel( 'HazardStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'HazardStatus', "0x105", "0x4000000000000000"));

  EXPECT_EQ(0, CanDataModel( 'PositionLampStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'PositionLampStatus', "0x105", "0x8000000000000000"));

  EXPECT_EQ(0, CanDataModel( 'HighBeamStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'HighBeamStatus', "0x105", "0x0001000000000000"));

  EXPECT_EQ(0, CanDataModel( 'LowBeamStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'LowBeamStatus', "0x105", "0x0002000000000000"));

  EXPECT_EQ(0, CanDataModel( 'Front_Fog_Status', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'Front_Fog_Status', "0x105", "0x0004000000000000"));

  EXPECT_EQ(0, CanDataModel( 'Rear_Fog_Status', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'Rear_Fog_Status', "0x105", "0x0008000000000000"));

  EXPECT_EQ(0, CanDataModel( 'DRLStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'DRLStatus', "0x105", "0x0000000400000000"));

  EXPECT_EQ(0, CanDataModel( 'LFDoorStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'LFDoorStatus', "0x105", "0x0000001000000000"));

  EXPECT_EQ(0, CanDataModel( 'RFDoorStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'RFDoorStatus', "0x105", "0x0000002000000000"));

  EXPECT_EQ(0, CanDataModel( 'LRDoorStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'LRDoorStatus', "0x105", "0x0000004000000000"));

  EXPECT_EQ(0, CanDataModel( 'RRDoorStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'RRDoorStatus', "0x105", "0x0000008000000000"));

  EXPECT_EQ(0, CanDataModel( 'HoodStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'HoodStatus', "0x105", "0x0000000001000000"));


  EXPECT_EQ(0, CanDataModel( 'TrunkStatus', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'TrunkStatus', "0x105", "0x0000000003000000"));


  EXPECT_EQ(0, CanDataModel( 'Alarm_Mode', "0x105", "0x0000000000000000"));
  EXPECT_EQ(1, CanDataModel( 'Alarm_Mode', "0x105", "0x0100000000000000"));
  EXPECT_EQ(2, CanDataModel( 'Alarm_Mode', "0x105", "0x0200000000000000"));
  EXPECT_EQ(3, CanDataModel( 'Alarm_Mode', "0x105", "0x0300000000000000"));
  EXPECT_EQ(4, CanDataModel( 'Alarm_Mode', "0x105", "0x0400000000000000"));
  EXPECT_EQ(5, CanDataModel( 'Alarm_Mode', "0x105", "0x0500000000000000"));


}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
