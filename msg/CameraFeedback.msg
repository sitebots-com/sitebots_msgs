uint64 time_usec # [us] Image timestamp (since UNIX epoch), as passed in by CAMERA_STATUS message (or autopilot if no CCB)
int32 latitude # [degE7] Latitude
int32 longitude # [degE7] Longitude
float32 altitude_msl # [m] Altitude (MSL)
float32 altitude # [m] Altitude (Relative to HOME location)
float32 roll # [deg] Camera Roll angle (earth frame, +-180)
float32 pitch # [deg] Camera Pitch angle (earth frame, +-180)
float32 yaw # [deg] Camera Yaw (earth frame, 0-360, true)
float32 focal_length # [mm] Focal Length
uint16 image_index #  Image index
uint8 target_system #  System ID
uint8 camera_index #  Camera ID
uint8 flags #  Feedback flags
