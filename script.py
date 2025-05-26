import sys
import os


def	create_file(file:str) -> None:
	header = f"{file}.h"
	content = f"""#pragma once
	
class {file}{{
	public:
		{file}(void);
		{file}(const {file}& other);
		{file}& operator=(const {file}& other);
		~{file}(void);
}};
"""
	
	with open(header, "w") as f:
		f.write(content)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Wrong usage!! use the following ./script.py ClassName")
	else:
		create_file(sys.argv[1])