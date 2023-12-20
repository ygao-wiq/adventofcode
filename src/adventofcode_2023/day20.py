import collections
import copy
import enum
import math

import utils

event = collections.namedtuple("event", ["source", "pulse", "destination"])

class Pulse(enum.Enum):
    LOW = 0
    HIGH = 1

class Broadcaster(object):
    def __init__(self, name: str, adjacent: list[str]):
        self.name = name
        self.adjacent: list[str] = adjacent
    def output(self, e: event) -> list[event]:
        return [event(self.name, e.pulse, r) for r in self.adjacent]

class Inverter(object):
    def __init__(self, name: str, adjacent: list[str]):
        self.name = name
        self.adjacent: list[str] = adjacent
    def output(self, e: event) -> list[event]:
        output_pulse = Pulse.HIGH if e.pulse is Pulse.LOW else Pulse.LOW
        return [event(self.name, output_pulse, r) for r in self.adjacent]

class FlipFlop(object):
    def __init__(self, name: str, adjacent: list[str]):
        self.name = name
        self.adjacent: list[str] = adjacent
        self.status = False  # initial switch status
    def output(self, e: event) -> list[event]:
        output_pulse = Pulse.LOW if self.status else Pulse.HIGH
        if e.pulse is Pulse.LOW:
            self.status = not self.status
            return [event(self.name, output_pulse, r) for r in self.adjacent]
        return []

class Conjunction(object):
    def __init__(self, name: str, adjacent: list[str]):
        self.name = name
        self.adjacent: list[str] = adjacent
        self.inputs: list[str] = list()
        self.memory = dict()
        self.status = False  # initial switch status
    def output(self, e: event) -> list[event]:
        self.memory[e.source] = e.pulse
        if all([v is Pulse.HIGH for v in self.memory.values()]):
            output_pulse = Pulse.LOW
        else:
            output_pulse = Pulse.HIGH
        return [event(self.name, output_pulse, r) for r in self.adjacent]

def sort_out_conjunction_inputs(modules: dict[str, any]) -> dict[str, any]:
    for m in modules.values():
        if type(m) is Conjunction:
            m.inputs = [m1.name for m1 in modules.values() if m.name in m1.adjacent]
            m.memory = {n: Pulse.LOW for n in m.inputs}
    return modules
def solution_1(data_lines: list[str]):
    modules = dict()
    for l in data_lines:
        raw_module, targets = l.split(" -> ")
        if raw_module == "broadcaster":
            modules["broadcaster"] = Broadcaster("broadcaster", targets.split(", "))
        elif raw_module[0] == "%":
            modules[raw_module[1:]] = FlipFlop(raw_module[1:], targets.split(", "))
        elif "inv" in raw_module:
            modules["inv"] = Inverter(raw_module[1:], targets.split(", "))
        elif raw_module[0] == "&":
            modules[raw_module[1:]] = Conjunction(raw_module[1:], targets.split(", "))
    modules = sort_out_conjunction_inputs(modules)
    low_pulses_cnt = 0
    high_pulses_cnt = 0
    for _ in range(1000):
        queue: list[event] = [event("button", Pulse.LOW, "broadcaster")]
        print("======", low_pulses_cnt, high_pulses_cnt)
        while queue:
            e: event = queue.pop(0)
            if e.pulse is Pulse.HIGH:
                high_pulses_cnt += 1
            elif e.pulse is Pulse.LOW:
                low_pulses_cnt += 1
            if e.destination == "output":
                continue
            if e.destination in modules:
                for e1 in modules[e.destination].output(e):
                    queue.append(e1)
    print(low_pulses_cnt * high_pulses_cnt)

def solution_2(data_lines: list[str]):
    modules = dict()
    for l in data_lines:
        raw_module, targets = l.split(" -> ")
        if raw_module == "broadcaster":
            modules["broadcaster"] = Broadcaster("broadcaster", targets.split(", "))
        elif raw_module[0] == "%":
            modules[raw_module[1:]] = FlipFlop(raw_module[1:], targets.split(", "))
        elif "inv" in raw_module:
            modules["inv"] = Inverter(raw_module[1:], targets.split(", "))
        elif raw_module[0] == "&":
            modules[raw_module[1:]] = Conjunction(raw_module[1:], targets.split(", "))
    original_modules = sort_out_conjunction_inputs(modules)
    low_pulses_cnt = 0
    high_pulses_cnt = 0
    sub_m_condition = []
    for m_name in ["hn", "mp", "xf", "fz"]:
        modules = copy.deepcopy(original_modules)
        cont = True
        cnt = 0
        while cont:
            queue: list[event] = [event("button", Pulse.LOW, "broadcaster")]
            cnt += 1
            while queue:
                e: event = queue.pop(0)
                if e.pulse is Pulse.HIGH:
                    high_pulses_cnt += 1
                elif e.pulse is Pulse.LOW:
                    low_pulses_cnt += 1
                if e.destination == "output":
                    continue
                if e.pulse is Pulse.HIGH and e.source == m_name:
                    sub_m_condition.append(cnt)
                    cont = False
                    break
                if e.destination in modules:
                    todo_events = modules[e.destination].output(e)
                    for e1 in todo_events:
                        queue.append(e1)
    print(math.lcm(*sub_m_condition))

if __name__ == "__main__":
    data_lines = utils.get_file_content("day20.dat")
    data_lines = [l.strip() for l in data_lines]
    #solution_1(data_lines)
    solution_2(data_lines)