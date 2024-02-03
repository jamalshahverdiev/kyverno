from json import JSONDecodeError, dumps
from subprocess import run, CalledProcessError, PIPE
from os import path, getcwd, makedirs
from kubernetes import client, config

def get_audit_cluster_policies():
    config.load_kube_config()  
    v1 = client.CustomObjectsApi()
    policies = v1.list_cluster_custom_object("kyverno.io", "v1", "clusterpolicies")
    # print("All policy names:", [p['metadata']['name'] for p in policies['items']])

    audit_policies = [p['metadata']['name'] for p in policies['items'] 
                  if p['spec'].get('validationFailureAction') == 'Audit' 
                  and not p['metadata']['name'].startswith('restart')]
    
    return audit_policies

def get_rules_from_policy(policy_name):
    config.load_kube_config()
    v1 = client.CustomObjectsApi()
    policy_data = v1.get_cluster_custom_object("kyverno.io", "v1", "clusterpolicies", policy_name)
    
    if policy_data:
        rules = [rule.get('name', '') for rule in policy_data.get('spec', {}).get('rules', [])]
        return rules
    return []

def get_policy_reports():
    config.load_kube_config()
    v1 = client.CustomObjectsApi()
    reports = v1.list_cluster_custom_object("wgpolicyk8s.io", "v1alpha2", "policyreports")
    return reports

def run_command(cmd):
    try:
        completed_process = run(cmd, shell=True, check=True, stdout=PIPE, stderr=PIPE, text=True)
        return completed_process.stdout.strip()
    except CalledProcessError as e:
        print(f"An error occurred while running command: {e}")
        return None

def filter_policy_reports(reports, policy_name, rule_name):
    filtered_reports = []
    for report in reports.get('items', []):
        filtered_results = [result for result in report.get('results', [])
                            if result.get('policy') == policy_name
                            and result.get('rule') == rule_name
                            and result.get('result') == 'fail']
        if filtered_results:
            modified_report = report.copy()
            modified_report['results'] = filtered_results
            modified_report['summary']['fail'] = len(filtered_results)
            modified_report['summary']['pass'] = 0  
            filtered_reports.append(modified_report)
    return filtered_reports


def generate_table(filtered_reports, policy_name, rule_name):
    namespaces = [report.get('scope', {}).get('namespace', '') for report in filtered_reports]
    kinds = [report.get('scope', {}).get('kind', '') for report in filtered_reports]
    names = [report.get('scope', {}).get('name', '') for report in filtered_reports]

    if not namespaces or not kinds or not names:
        print(f"No data available to generate table for policy '{policy_name}', rule '{rule_name}'.")
        return None

    max_namespace_len = max(len(namespace) for namespace in namespaces)
    max_kind_len = max(len(kind) for kind in kinds)
    max_name_len = max(len(name) for name in names)

    table = f"{'Namespace'.ljust(max_namespace_len)}\t{'Kind'.ljust(max_kind_len)}\t{'Name'.ljust(max_name_len)}\n"
    for namespace, kind, name in zip(namespaces, kinds, names):
        table += f"{namespace.ljust(max_namespace_len)}\t{kind.ljust(max_kind_len)}\t{name.ljust(max_name_len)}\n"

    return table

def ensure_directory(directory_name):
    makedirs(directory_name, exist_ok=True)

output_directory = path.join(getcwd(), 'policyreports')
ensure_directory(output_directory)

audit_policies = get_audit_cluster_policies()

for policy_name in audit_policies:
    rules = get_rules_from_policy(policy_name)
    for rule_name in rules:
        try:
            policy_reports_json_data = get_policy_reports()
            if policy_reports_json_data:
                policy_reports_data = get_policy_reports()
                filtered_reports = filter_policy_reports(policy_reports_data, policy_name, rule_name)
                # filtered_reports_json = dumps(filtered_reports, indent=4)

                # generated_json_file = f'{policy_name}-{rule_name}-filtered-policy-reports.json'
                # output_file_path = path.join(output_directory, generated_json_file)
                # with open(output_file_path, 'w') as file:
                #     file.write(filtered_reports_json)

                # Generate and write the table to a file
                generated_table_file = f'{policy_name}-{rule_name}-filtered-policy-reports.txt'
                table_output_path = path.join(output_directory, generated_table_file)
                table_content = generate_table(filtered_reports, policy_name, rule_name)
                if table_content:
                    with open(table_output_path, 'w') as table_file:
                        table_file.write(table_content)
                        # print(f"Table for policy '{policy_name}', rule '{rule_name}' written to file: {table_output_path}")
                else:
                    print(f"Skipped generating table for policy '{policy_name}', rule '{rule_name}' due to no data.")

            else:
                print("Failed to get policy reports data.")
        except JSONDecodeError:
            print("Error decoding JSON from the data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
