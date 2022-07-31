# flake8: noqa
# type: ignore
# pylint: skip-file
click_context  # unused variable (autonomy/analyse/__init__.py:30)
cmd1  # unused function (autonomy/analyse/cli.py:25)
build_deployment  # unused function (autonomy/cli/deploy.py:38)
dev_mode  # unused variable (autonomy/cli/deploy.py:67)
schema_dir  # unused variable (autonomy/configurations/base.py:32)
_validator  # unused attribute (autonomy/deploy/base.py:111)
_validator  # unused attribute (autonomy/deploy/base.py:115)
agent_spec  # unused attribute (autonomy/deploy/base.py:330)
old_wd  # unused variable (autonomy/deploy/base.py:402)
build_docker_compose_yml  # unused function (autonomy/deploy/generators/docker_compose/base.py:52)
HARDHAT_NODE_TEMPLATE  # unused variable (autonomy/deploy/generators/docker_compose/templates.py:51)
HARDHAT_TEMPLATE  # unused variable (autonomy/deploy/generators/kubernetes/templates.py:25)
run_agent  # unused function (autonomy/cli/replay.py:44)
run_tendermint  # unused function (autonomy/cli/replay.py:78)
run_until_interruption  # unused method (autonomy/replay/tendermint.py:178)
hard_reset  # unused function (autonomy/replay/tendermint.py:195)
status  # unused function (autonomy/replay/tendermint.py:215)
broadcast_tx_sync  # unused function (autonomy/replay/tendermint.py:238)
tx  # unused function (autonomy/replay/tendermint.py:244)
LOCAL  # unused variable (autonomy/analyse/benchmark/aggregate.py:35)
CONSENSUS  # unused variable (autonomy/analyse/benchmark/aggregate.py:36)
TOTAL  # unused variable (autonomy/analyse/benchmark/aggregate.py:37)
benchmark  # unused function (autonomy/cli/analyse.py:35)
docstrings  # unused function (autonomy/cli/analyse.py:49)
parse_logs  # unused function (autonomy/cli/analyse.py:74)
HARDHAT_IMAGE_NAME  # unused variable (autonomy/constants.py:25)
is_transition_func_total  # unused method (autonomy/analyse/abci/app_spec.py:119)
get_transitions  # unused method (autonomy/analyse/abci/app_spec.py:134)
generat_abci_app_pecs  # unused function (autonomy/cli/analyse.py:52)
check_abci_app_specs  # unused function (autonomy/cli/analyse.py:79)
run_handler_check  # unused function (autonomy/cli/analyse.py:159)
dump_json  # unused method (autonomy/analyse/abci/app_spec.py:159)
dump_yaml  # unused method (autonomy/analyse/abci/app_spec.py:163)
dump_mermaid  # unused method (autonomy/analyse/abci/app_spec.py:167)
from_json  # unused method  (autonomy/configurations/base.py:100)
SERVICES  # unused variable  (autonomy/configurations/constants.py:30)
_directory  # unused attribute (autonomy/cli/hash.py:63)
generate_all  # unused function (autonomy/cli/hash.py:72)
hash_file  # unused function (autonomy/cli/hash.py:94)
_create_or_update_from_json  # unused method (autonomy/configurations/base.py:175)
help  # unused attribute (autonomy/cli/core.py:41)
DEFAULT_ABCI_BUILD_DIR  # unused variable (autonomy/deploy/constants.py:105)
build_images  # unused function (autonomy/cli/deploy.py:187)
execinfo  # unused variable (autonomy/data/Dockerfiles/tendermint/app.py:100)
get_params  # unused function (autonomy/data/Dockerfiles/tendermint/app.py:142)
update_params  # unused function (autonomy/data/Dockerfiles/tendermint/app.py:155)
gentle_reset  # unused function (autonomy/data/Dockerfiles/tendermint/app.py:187)
app_hash  # unused function (autonomy/data/Dockerfiles/tendermint/app.py:197)
handle_notfound  # unused function (autonomy/data/Dockerfiles/tendermint/app.py:236)
handle_server_error  # unused function (autonomy/data/Dockerfiles/tendermint/app.py:242)
create_server  # unused function (autonomy/data/Dockerfiles/tendermint/app.py:251)
call_vote  # unused function (autonomy/data/Dockerfiles/dev/watcher.py:54)
wait_for_votes  # unused function (autonomy/data/Dockerfiles/dev/watcher.py:67)
on_any_event  # unused method (autonomy/data/Dockerfiles/dev/watcher.py:166)
tendermint_health_check  # unused function (autonomy/test_tools/utils.py:30)
DEFAULT_ACN_CONFIG  # unused variable (autonomy/test_tools/docker/acn_node.py:35)
ACNNodeDockerImage  # unused class (autonomy/test_tools/docker/acn_node.py:45)
SAFE_CONTRACT  # unused variable (autonomy/test_tools/docker/amm_net.py:41)
ROUTER_CONTRACT  # unused variable (autonomy/test_tools/docker/amm_net.py:42)
DEFAULT_CALLBACK_HANDLER  # unused variable (autonomy/test_tools/docker/amm_net.py:43)
PROXY_FACTORY_CONTRACT  # unused variable (autonomy/test_tools/docker/amm_net.py:44)
MULTISEND_CONTRACT  # unused variable (autonomy/test_tools/docker/amm_net.py:45)
MULTISEND_CALL_ONLY_CONTRACT  # unused variable (autonomy/test_tools/docker/amm_net.py:46)
AMMNetDockerImage  # unused class (autonomy/test_tools/docker/amm_net.py:49)
launch_image  # unused function (autonomy/test_tools/docker/base.py:173)
launch_many_containers  # unused function (autonomy/test_tools/docker/base.py:191)
_.setup_class  # unused method (autonomy/test_tools/docker/base.py:224)
_.teardown_class  # unused method (autonomy/test_tools/docker/base.py:246)
DEFAULT_GANACHE_ADDR  # unused variable (autonomy/test_tools/docker/ganache.py:33)
DEFAULT_GANACHE_PORT  # unused variable (autonomy/test_tools/docker/ganache.py:34)
DEFAULT_GANACHE_CHAIN_ID  # unused variable (autonomy/test_tools/docker/ganache.py:35)
GanacheDockerImage  # unused class (autonomy/test_tools/docker/ganache.py:38)
SAFE_CONTRACT  # unused variable (autonomy/test_tools/docker/gnosis_safe_net.py:44)
DEFAULT_CALLBACK_HANDLER  # unused variable (autonomy/test_tools/docker/gnosis_safe_net.py:45)
PROXY_FACTORY_CONTRACT  # unused variable (autonomy/test_tools/docker/gnosis_safe_net.py:46)
MULTISEND_CONTRACT  # unused variable (autonomy/test_tools/docker/gnosis_safe_net.py:47)
MULTISEND_CALL_ONLY_CONTRACT  # unused variable (autonomy/test_tools/docker/gnosis_safe_net.py:48)
GnosisSafeNetDockerImage  # unused class (autonomy/test_tools/docker/gnosis_safe_net.py:51)
FlaskTendermintDockerImage  # unused class (autonomy/test_tools/docker/tendermint.py:119)
_.health_check  # unused method (autonomy/test_tools/docker/tendermint.py:371)
ETHEREUM_ENCRYPTED_KEYS  # unused variable (autonomy/test_tools/configurations.py:46)
ETHEREUM_ENCRYPTION_PASSWORD  # unused variable (autonomy/test_tools/configurations.py:47)
GANACHE_CONFIGURATION  # unused variable (autonomy/test_tools/configurations.py:48)
HTTP_LOCALHOST  # unused variable (autonomy/test_tools/configurations.py:39)
KEY_PAIRS  # unused variable (autonomy/test_tools/configurations.py:62)
UseTendermint  # unused class (autonomy/test_tools/fixture_helpers.py:55)
_._start_tendermint  # unused method (autonomy/test_tools/fixture_helpers.py:62)
_.node_address  # unused property (autonomy/test_tools/fixture_helpers.py:81)
UseFlaskTendermintNode  # unused class (autonomy/test_tools/fixture_helpers.py:87)
_._start_tendermint  # unused method (autonomy/test_tools/fixture_helpers.py:91)
_.get_laddr  # unused method (autonomy/test_tools/fixture_helpers.py:120)
UseGnosisSafeHardHatNet  # unused class (autonomy/test_tools/fixture_helpers.py:129)
_._start_hardhat  # unused method (autonomy/test_tools/fixture_helpers.py:135)
gnosis_safe_hardhat_scope_function  # unused variable (autonomy/test_tools/fixture_helpers.py:138)
hardhat_port  # unused variable (autonomy/test_tools/fixture_helpers.py:138)
UseGanache  # unused class (autonomy/test_tools/fixture_helpers.py:144)
_._start_ganache  # unused method (autonomy/test_tools/fixture_helpers.py:150)
ganache  # unused variable (autonomy/test_tools/fixture_helpers.py:152)
UseACNNode  # unused class (autonomy/test_tools/fixture_helpers.py:163)
_._start_acn  # unused method (autonomy/test_tools/fixture_helpers.py:170)
_._acn_node_image  # unused attribute (autonomy/test_tools/fixture_helpers.py:174)
get_register_contract  # unused function (autonomy/test_tools/helpers/contracts.py:30)
GanacheForkDockerImage  # unused function (autonomy/test_tools/docker/ganache.py:111)
try_send  # unused function (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/base.py:68)
make_round_class  # unused function (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/base.py:79)
ANY_ADDRESS  # unused variable (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/configurations.py:144)
wait_for_condition  # unused function (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/async_utils.py:29)
BaseThreadedAsyncLoop  # unused class (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/async_utils.py:146)
thread  # unused variable (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/async_utils.py:151)
_.setup  # unused method (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/async_utils.py:153)
_.execute  # unused method (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/async_utils.py:158)
_.teardown  # unused method (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/async_utils.py:163)
_.get_command  # unused method (/home/marcofavorito/workfolder/open-autonomy/autonomy/test_tools/helpers/tendermint_utils.py:125)
