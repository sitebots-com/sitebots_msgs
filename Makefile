js:
	protoc --proto_path=msg --js_out=import_style=commonjs,binary:/Users/pharaohlxvi/sitebots/vehicle-control-user-interface/src/proto msg/sitebots.proto

python:
	protoc -I=msg --python_out=../src/proto msg/sitebots.proto
