cmake_minimum_required(VERSION 2.8.3)
project(sitebots_msgs)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
  mavros_msgs
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  MobileStatus.msg
  ChannelList.msg
  Channel.msg
  CameraFeedback.msg
  Edge.msg
	Node.msg
  GeometryGraph.msg
)

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

catkin_python_setup()

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
  mavros_msgs
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES vehicle-controller
   CATKIN_DEPENDS std_msgs mavros_msgs
#  DEPENDS system_lib
)
