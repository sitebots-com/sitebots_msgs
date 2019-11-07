js:
<<<<<<< HEAD
	protoc --proto_path=msg --js_out=import_style=commonjs,binary:/Users/pharaohlxvi/sitebots/vehicle-control-user-interface/src/proto msg/sitebots.proto

python:
	protoc -I=msg --python_out=../src/proto msg/sitebots.proto
=======
	protoc --proto_path=msg --js_out=import_style=commonjs,binary:/Users/pharaohlxvi/sitebots/vehicle-control-user-interface/src/proto proto/sitebots.proto

python:
	protoc -I=proto --python_out=src/sitebots_proto proto/sitebots.proto
>>>>>>> 48384d2... merged with previous sitebots_msgs
