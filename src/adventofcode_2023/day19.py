import collections
import utils

part = collections.namedtuple("part", ["x", "a", "m", "s"])
rule = collections.namedtuple("rule", ["field", "comparator", "gauge", "target"])

def rule_evaluator(p: dict, rs: list[rule]) -> str | None:
    for r in rs:
        if r.field is not None:
            if r.comparator == "<" and p[r.field] < r.gauge:
                return r.target
            elif r.comparator == ">" and p[r.field] > r.gauge:
                return r.target
        else:
            return r.target
    return None


def solution_1():
    data_lines = utils.get_file_content("day19.dat")
    data_lines = [r.strip() for r in data_lines]

    workflows_mapping = dict()
    workflows = list()
    parts = list()
    part_data_lineno = 0
    for idx, line in enumerate(data_lines):
        if line:
            name, raw_rules = line.split("{")
            raw_rules = raw_rules[:-1].split(",")
            rules = list()
            for raw_rule in raw_rules:
                if ":" in raw_rule:
                    condition, target_wf = raw_rule.split(":")
                    field, comparator, gauge = condition[0], condition[1], int(condition[2:])
                    rules.append(rule(field, comparator, gauge, target_wf))
                else:
                    target_wf = raw_rule
                    rules.append(rule(None, None, None, target_wf))
            workflows_mapping[name] = rules
            workflows.append((name, rules))
        else:
            part_data_lineno = idx
            break
    for line in data_lines[part_data_lineno+1:]:
        features = line[1:-1].split(",")
        parts.append({"x": int(features[0][2:]), "m": int(features[1][2:]), "a": int(features[2][2:]), "s": int(features[3][2:])})
    accepted = list()
    rejected = list()
    for p in parts:
        i = 0
        curr_wf_name = "in"
        curr_wf_rules = workflows_mapping[curr_wf_name]
        i = workflows.index((curr_wf_name, curr_wf_rules))
        while True:
            if curr_wf_name == "A":
                accepted.append(p)
                break
            elif curr_wf_name == "R":
                rejected.append(p)
                break
            next_wf_name = rule_evaluator(p, curr_wf_rules)
            if next_wf_name and next_wf_name not in ["A", "R"]:
                curr_wf_name = next_wf_name
                curr_wf_rules = workflows_mapping[curr_wf_name]
                continue
            elif next_wf_name in ["A", "R"]:
                curr_wf_name = next_wf_name
                continue
            else:
                # i = workflows.index((curr_wf_name, curr_wf_rules)) + 1
                i = (i+1) % len(workflows)
                curr_wf_name, curr_wf_rules = workflows[i]
    ret = 0
    for p in accepted:
        ret += p["x"] + p["m"] + p["a"] + p["s"]

    print(ret)

def visit_count(wf_mapping, target_wf, x_range, m_range, a_range, s_range):
    if target_wf == "A":
        return len(x_range) * len(m_range) * len(a_range) * len(s_range)
    if target_wf == "R":
        return 0
    if len(x_range) == 0 or len(m_range) == 0 or len(a_range) == 0 or len(s_range) == 0:
        return 0
    count = 0
    for r in wf_mapping[target_wf]:
        if r.field is not None:
            if r.comparator == "<":
                test = lambda n: n<r.gauge
            elif r.comparator == ">":
                test = lambda n: n>r.gauge
            else:
                assert False
            if r.field == "x":
                count += visit_count(wf_mapping, r.target, list(filter(test, x_range)), m_range, a_range, s_range)
                x_range = [i for i in x_range if not test(i)]
            elif r.field == "m":
                count += visit_count(wf_mapping, r.target, x_range, list(filter(test, m_range)), a_range, s_range)
                m_range = [i for i in m_range if not test(i)]
            elif r.field == "a":
                count += visit_count(wf_mapping, r.target, x_range, m_range, list(filter(test, a_range)), s_range)
                a_range = [i for i in a_range if not test(i)]
            elif r.field == "s":
                count += visit_count(wf_mapping, r.target, x_range, m_range, a_range, list(filter(test, s_range)))
                s_range = [i for i in s_range if not test(i)]
        else:
            count += visit_count(wf_mapping, r.target, x_range, m_range, a_range, s_range)
    return count
def solution_2():
    data_lines = utils.get_file_content("day19.dat")
    data_lines = [r.strip() for r in data_lines]

    workflows_mapping = dict()
    reversed_workflows_mapping = dict()
    workflows = list()
    parts = list()
    part_data_lineno = 0
    for idx, line in enumerate(data_lines):
        if line:
            name, raw_rules = line.split("{")
            raw_rules = raw_rules[:-1].split(",")
            rules = list()
            for raw_rule in raw_rules:
                if ":" in raw_rule:
                    condition, target_wf = raw_rule.split(":")
                    field, comparator, gauge = condition[0], condition[1], int(condition[2:])
                    rules.append(rule(field, comparator, gauge, target_wf))
                else:
                    target_wf = raw_rule
                    rules.append(rule(None, None, None, target_wf))
                if rules[-1].target  not in ["A", "R"]:
                    reversed_workflows_mapping[rules[-1].target] = reversed_workflows_mapping.get(rules[-1].target, set())
                    reversed_workflows_mapping[rules[-1].target].add((name, rules[-1]))
            workflows_mapping[name] = rules
            workflows.append((name, rules))
        else:
            part_data_lineno = idx
            break
    for line in data_lines[part_data_lineno+1:]:
        features = line[1:-1].split(",")
        parts.append({"x": int(features[0][2:]), "m": int(features[1][2:]), "a": int(features[2][2:]), "s": int(features[3][2:])})
    print(visit_count(workflows_mapping, "in", list(range(1, 4001)), list(range(1, 4001)), list(range(1, 4001)), list(range(1, 4001))))

if __name__ == "__main__":
    solution_1()
    solution_2()