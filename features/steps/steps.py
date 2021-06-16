from behave import *

# This should be added to environment.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords()

use_step_matcher('re')


@when(r'the main page is visited and searched for user identity')
def impl(context):
    context.actionwords.the_main_page_is_visited_and_searched_for_user_identity()


@then(r'the searched text appears in results header')
def impl(context):
    context.actionwords.the_searched_text_appears_in_results_header()


@then(r'all allocations must be superior to "(.*)"')
def impl(context, p1):
    context.actionwords.all_allocations_must_be_superior_to_p1(p1)


@then(r'the output is equal to the total budget')
def impl(context):
    context.actionwords.the_output_is_equal_to_the_total_budget()


@when(r'the cost allocation matrix is generated')
def impl(context):
    context.actionwords.the_cost_allocation_matrix_is_generated()


@given(r'a launched browser on main ATIH page')
def impl(context):
    context.actionwords.a_launched_browser_on_main_atih_page()


@given(r'a total budget of "(.*)"')
def impl(context, p1):
    context.actionwords.a_total_budget_of_p1(p1)


@given(r'a "(.*)" and a "(.*)"')
def impl(context, p1, p2):
    context.actionwords.a_p1_and_a_p2(p1, p2)


@given(r'an hospital list')
def impl(context):
    context.actionwords.an_hospital_list()




