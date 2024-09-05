class CPU:
  def __init__(self, cpu_type):
    self.cpu_type = cpu_type

class Computer:
  def __init__(self, cpu_type):
    self.CPU = CPU(cpu_type)


# Create a Computer instance with a specific CPU type
computer = Computer(cpu_type="Intel Core i7")

# Output the CPU type of the Computer
print(f"Computer CPU Type:")
print(f" - CPU Type: {computer.CPU.cpu_type}")