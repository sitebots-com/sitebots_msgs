js:
	protoc --proto_path=msg --js_out=import_style=commonjs,binary:/Users/pharaohlxvi/sitebots/vehicle-control-user-interface/src/proto proto/sitebots.proto

python:
	protoc -I=proto --python_out=src/sitebots_proto proto/sitebots.proto
