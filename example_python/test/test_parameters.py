import generate_parameter_module_example
print("OK 1")
import generate_parameter_module_example.minimal_publisher
print("OK 2")
from generate_parameter_module_example.minimal_publisher import MinimalParam

print(MinimalParam)