import tcms_api
from datetime import datetime

rpc_client = tcms_api.TCMS().exec

user = rpc_client.User.filter()[0]
print(f"user: {user}")

classification = rpc_client.Classification.filter({})[0]
print(f"classification: {classification}")

list_products = rpc_client.Product.filter()
print(f"product={list_products}")

product = rpc_client.Product.filter({'name': 'Product created'})[0]
print(product)

# product = rpc_client.Product.create({
#     'name': 'Product created',
#     'classification': classification['id'],
# })

version = rpc_client.Version.create({
    'product': product['id'],
    'value': f'version-auto-{datetime.now().isoformat()}',
})

# create TestPlan
test_plan = rpc_client.TestPlan.create({
    'name': f'TP: created at {datetime.now().isoformat()}',
    'text': 'A script is creating this TP and adds TCs and TRs to it to establish a performance baseline',
    'type': 4, # 4: Interation, 7: Performance
    'product': product['id'],
    'product_version': version['id'],
    'is_active': True,
})

test_cases = [] # for run
# test case setting
priority = rpc_client.Priority.filter({})[0]
category = rpc_client.Category.filter({'product': product['id'],})[0]
confirmed_status = rpc_client.TestCaseStatus.filter({'is_confirmed': True})[0]

for i in range(3):
    test_case = rpc_client.TestCase.create({
        'summary': f'Case {i+1} created',
        'product': product['id'],
        'category': category['id'],
        'priority': priority['id'],
        'case_status': confirmed_status['id'],
        'text': f"text for case {i+1}"
    })
    # id, create_date, is_automated, script, arguments, extra_link, summary,
    # requirement, notes, text, setup_duration, testing_duration, case_status,
    # category, priority, author, default_tester, reviewer
    # ref: https://kiwitcms.readthedocs.io/en/latest/modules/tcms.testcases.models.html#tcms.testcases.models.TestCase
    print(test_case)
    rpc_client.TestCase.add_comment(test_case['id'], f"comment for case {i+1}")

    test_cases.append(test_case)
    rpc_client.TestPlan.add_case(test_plan['id'], test_case['id'])
    

    
# # create build, test run & test executions
# pass_status = rpc_client.TestExecutionStatus.filter({'weight__gt': 0})[0]
# build = rpc_client.Build.create({
#     'name': 'b.%s' % datetime.now().isoformat(),
#     'description': 'the product build at %s' % datetime.now().isoformat(),
#     'version': version['id'],
# })


# # create a separate TestPlan
# for i in range(RANGE_SIZE):
#     test_run = rpc_client.TestRun.create({
#         'summary': 'TR %d %s' % (i, datetime.now().isoformat()),
#         'manager': user['id'],
#         'plan': test_plan['id'],
#         'build': build['id'],
#     })
#     print("TR-%d created" % test_run['id'])

#     # add cases to TR
#     for case in test_cases:
#         result = rpc_client.TestRun.add_case(test_run['id'], case['id'])
#         if not isinstance(result, list):
#             result = [result]

#         # record the results
#         for execution in result:
#             rpc_client.TestExecution.update(execution['id'], {
#                 'status': pass_status['id'],
#             })
