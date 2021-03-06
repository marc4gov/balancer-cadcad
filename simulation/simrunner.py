# #!/usr/bin/env python
# # coding: utf-8
#
# import argparse
# import json
#
# import pandas as pd
# from cadCAD.configuration import Experiment
# from cadCAD.configuration.utils import config_sim
# from cadCAD.engine import ExecutionContext, ExecutionMode, Executor
# from cadCAD import configs
#
# from simulation import (CommonsSimulationConfiguration, bootstrap_simulation,
#                         partial_state_update_blocks)
#
#
# def run_simulation(c: CommonsSimulationConfiguration):
#     initial_conditions, simulation_parameters = bootstrap_simulation(c)
#
#     exp = Experiment()
#     exp.append_configs(
#         initial_state=initial_conditions,
#         partial_state_update_blocks=partial_state_update_blocks,
#         sim_configs=simulation_parameters
#     )
#
#     # Do not use multi_proc, breaks ipdb.set_trace()
#     exec_mode = ExecutionMode()
#     single_proc_context = ExecutionContext(exec_mode.local_mode)
#     executor = Executor(single_proc_context, configs)
#
#     raw_system_events, tensor_field, sessions = executor.execute()
#
#     df = pd.DataFrame(raw_system_events)
#     df_final = df[df.substep.eq(2)]
#
#     result = {
#         "timestep": list(df_final["timestep"]),
#         "funding_pool": list(df_final["funding_pool"]),
#         "token_price": list(df_final["token_price"]),
#         "sentiment": list(df_final["sentiment"])
#     }
#     return result, df_final
#
#
# parser = argparse.ArgumentParser()
# c_default = CommonsSimulationConfiguration()
# parser.add_argument("--hatchers", type=int, default=c_default.hatchers)
# parser.add_argument("--proposals", type=int, default=c_default.proposals)
# parser.add_argument("--hatch_tribute", type=float,
#                     default=c_default.hatch_tribute)
# parser.add_argument("--vesting_80p_unlocked", type=float,
#                     default=c_default.vesting_80p_unlocked)
# parser.add_argument("--exit_tribute", type=float,
#                     default=c_default.exit_tribute)
# parser.add_argument("--kappa", type=int, default=c_default.kappa)
# parser.add_argument("--days_to_80p_of_max_voting_weight",
#                     type=int, default=c_default.days_to_80p_of_max_voting_weight)
# parser.add_argument("--max_proposal_request", type=float,
#                     default=c_default.max_proposal_request)
# parser.add_argument("-T", "--timesteps_days", type=int,
#                     default=c_default.timesteps_days)
# args = parser.parse_args()
#
# c = CommonsSimulationConfiguration(**vars(args))
# print("Running sim config", c)
# o, _ = run_simulation(c)
# print(json.dumps(o))
