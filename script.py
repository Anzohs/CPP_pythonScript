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

def	create_cpp(file:str) -> None:
	cxx = f"{file}.cpp"
	content =f'''#include "{file}.h"

{file}::{file}(void){{}}

{file}::{file}(const {file}& other){{}}

{file}& {file}::operator=(const {file}& other){{
	if (this == &other)
		return (*this);
	return (*this);
}}

{file}::~{file}(void){{}}
'''
	with open(cxx, "w") as f:
		f.write(content)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Wrong usage!! use the following ./script.py ClassName")
	else:
		create_file(sys.argv[1])
		create_cpp(sys.argv[1])