#include <iostream>
#include <cc++/cmdoptns.h>

// Default Stuff for Config
#include "log_macro.h"
#include "constants.h"
#include "autofree.h"
#include "app_setting.h"
#include "init_check.h"
#include "string_util.h"

// Original API Handler Files
#include "ott_operations.h"
#include "rest_router.h"
#include "rest_basic_auth.h"

#include "product_rest_handler.h"
#include "all_products_rest_handler.h"
#include "confirmation_code_rest_handler.h"

#include "confirmation_code_generator.h"

#include "queue_accessor_manager.h"
#include "queue_accessor_queued.h"

#include "mysql_conn_pool.h"
#include "query_orders.h"

#include "generic_service.h"

#include "id_generator.h"
#include "signalling.h"

#include "generic_conn_impl.h"
#include "generic_conn.h"
#include "sms_sender.h"
#include "rt_conn.h"

// Mini-Project Classes
#include "operation.h"
#include "db_connect.h"
#include "server.h"

using namespace std;

int main(int argc, char** argv)
{
	// Parse command options
	//
	ost::CommandOptionArg config_file_opt("config", "c", "Config file", true);
	AutoFree<ost::CommandOptionParse> cmd(ost::makeCommandOptionParse(argc, argv, NULL));

	if (cmd->argsHaveError())
	{
		fprintf(stderr, "%s\n%s\n", cmd->printErrors(), cmd->printUsage());
		return -1;
	}


	// Parse config file
	//
	AppSetting app_setting;
	if (app_setting.initialize(config_file_opt.values[0]) <= 0)
	{
		fprintf(stderr, "ERROR: Failed to open config file '%s'\n", config_file_opt.values[0]);
		return -1;
	}

	#define SETTINGOBJ app_setting
	const char* pvalue;

	const char* root_path;
	GET_CFG_STRING_S(root_path, "API_HANDLER_ROOT_PATH",
					 pvalue, "/otti/api/v1.0/", true);

	const char* log_file;
	GET_CFG_STRING_S(log_file, "API_HANDLER_LOG_FILE",
					 pvalue, NULL, false);

	int log_level;
	GET_CFG_INT_S(log_level, "API_HANDLER_LOG_LEVEL",
				  pvalue, "0", true);

	int threads;
	GET_CFG_INT_S(threads, "API_HANDLER_THREADS",
				  pvalue, NULL, false);

	int port;
	GET_CFG_INT_S(port, "API_HANDLER_PORT",
				  pvalue, NULL, false);

	int queued_conns;
	GET_CFG_INT_S(queued_conns, "API_HANDLER_QUEUED_CONNS",
				  pvalue, NULL, false);


	int status_queue_id;
	GET_CFG_INT_S(status_queue_id, "STATUS_UPDATER_INPUT_QUEUED_ID",
				  pvalue, NULL, false);

	const char* confirm_code_msg_tpl;
	GET_CFG_STRING_S(confirm_code_msg_tpl, "CONFIRM_CODE_MSG_TEMPLATE",
					 pvalue, NULL, false);

	const char* confirm_code_msg_sender;
	GET_CFG_STRING_S(confirm_code_msg_sender, "CONFIRM_CODE_MSG_SENDER",
					 pvalue, NULL, false);

	int confirm_code_length;
	GET_CFG_INT_S(confirm_code_length, "CONFIRM_CODE_LENGTH",
				  pvalue, NULL, false);

	// HTTPS Keys
	//
	const char* https_key_file;
	GET_CFG_STRING_S(https_key_file, "API_HANDLER_HTTPS_KEY_FILE",
					 pvalue, "", true);

	const char* https_cert_file;
	GET_CFG_STRING_S(https_cert_file, "API_HANDLER_HTTPS_CERT_FILE",
					 pvalue, "", true);

	const char* https_key_pass;
	GET_CFG_STRING_S(https_key_pass, "API_HANDLER_HTTPS_KEY_PASS",
					 pvalue, "", true);

	const char* https_priorities;
	GET_CFG_STRING_S(https_priorities, "API_HANDLER_HTTPS_PRIORITIES",
					 pvalue, "NORMAL", true);

	// Generic Conn Config
	int generic_conn_count;
	GET_CFG_INT_S(generic_conn_count, "GENERIC_CONN_COUNT",
				  pvalue, "1", true);

	const char* generic_conn_auth_user;
	GET_CFG_STRING_S(generic_conn_auth_user, "GENERIC_CONN_AUTH_USER",
					 pvalue, "", true);

	const char* generic_conn_auth_pass;
	GET_CFG_STRING_S(generic_conn_auth_pass, "GENERIC_CONN_AUTH_PASS",
					 pvalue, "", true);

	// Database config (MYSQL)
	//
	const char* db_host;
	GET_CFG_STRING_S(db_host, "DB_HOST",
					 pvalue, NULL, false);

	const char* db_name;
	GET_CFG_STRING_S(db_name, "DB_NAME",
					 pvalue, NULL, false);

	const char* db_user;
	GET_CFG_STRING_S(db_user, "DB_USER",
					 pvalue, NULL, false);

	const char* db_pass;
	GET_CFG_STRING_S(db_pass, "DB_PASS",
					 pvalue, NULL, false);

	int db_port;
	GET_CFG_INT_S(db_port, "DB_PORT",
				  pvalue, "0", true);

	int db_connections;
	GET_CFG_INT_S(db_connections, "DB_CONNS",
				  pvalue, "1", true);

	int db_partitions;
	GET_CFG_INT_S(db_partitions, "DB_PARTITION",
				  pvalue, "1", true);

	// Queued
	//
    const char* queued_host;
    GET_CFG_STRING_S(queued_host, "QUEUED_HOST",
					 pvalue, "localhost", true);

    int queued_port;
    GET_CFG_INT_S(queued_port, "QUEUED_PORT",
				  pvalue, "5252", true);

	// RT
	//
	int rt_conn_count;
	GET_CFG_INT_S(rt_conn_count, "RT_CONN_COUNT",
				  pvalue, NULL, false);

	int rt_timeout_ms;
	GET_CFG_INT_S(rt_timeout_ms, "RT_TIMEOUT_MS",
				  pvalue, NULL, false);

	const char* rt_endpoint;
	GET_CFG_STRING_S(rt_endpoint, "RT_ENDPOINT",
					 pvalue, NULL, false);

	const char* rt_cp_tx_id_pref;
	GET_CFG_STRING_S(rt_cp_tx_id_pref, "RT_CP_TX_ID_PREF",
					 pvalue, NULL, false);

	const char* rt_cp_id;
	GET_CFG_STRING_S(rt_cp_id, "RT_CP_ID",
					 pvalue, NULL, false);

	const char* rt_cp_user_id;
	GET_CFG_STRING_S(rt_cp_user_id, "RT_CP_USER_ID",
					 pvalue, NULL, false);

	const char* rt_cp_pass;
	GET_CFG_STRING_S(rt_cp_pass, "RT_PASS",
					 pvalue, NULL, false);

	const char* rt_a_keyword;
	GET_CFG_STRING_S(rt_a_keyword, "RT_A_KEYWORD",
					 pvalue, NULL, false);

	const char* rt_s_keyword;
	GET_CFG_STRING_S(rt_s_keyword, "RT_S_KEYWORD",
					 pvalue, NULL, false);

	// Log File Initialize
	//
	if ((g_process_log = init_log_file_trc(log_file, log_level)) == NULL)
	{
		fprintf(stderr, "ERROR: Failed to open log file '%s'\n", log_file);
		return -1;
	}
	log_setprefix("MAIN");

	#ifndef WIN32
		int child_pid = fork();
		if (child_pid < 0)
		{
			fprintf(stderr, "ERROR: Failed to spawn child process.\n");
			return -1;
		}
		else if (child_pid == 0)
		{
			setsid();
		}
		else
		{
			return 0;
		}

		disable_signalling();
		start_signal_handler();
	#endif /* WIN32 */

	// Libcurl Global Init call
	//
    CURLcode curl_rc = curl_global_init(CURL_GLOBAL_ALL);
    if (curl_rc)
    {
        fprintf(stderr, "ERROR: Failed to initialize libcurl with curl_global_init()\n");
        return -1;
    }
	
	// ID Generator
	//
	INIT_CHECK(OrderIDGenerator::initialize(1), "OrderIDGenerator");
	
	// Confirmation Code Generator
	//
	INIT_CHECK(ConfirmationCodeGenerator::instance.initialize(), "ConfirmationCodeGenerator");
	
	// MYSQL Connections
	//

	INIT_CHECK(MySQLConnPool::instance.initialize(db_connections, db_host, db_name, db_user, db_pass, db_port), "MYSQLConnections");

	db::orders::partitions = db_partitions;

	INIT_CHECK(OTTOperations::instance.initialize(), "OTTOperations");
	INIT_CHECK(rest::BasicAuth::instance.initialize(), "BasicAuth");

	QueueAccessorQueuedFactory queued_fact(queued_host, queued_port);
	QueueAccessorManager::Initialize(&queued_fact, queued_conns);

	// OTT Services
	//
	GenericService generic_service;
	OTTOperations::instance.setProductServer(ORDER_TYPE_GENERIC, &generic_service);

	// OTT Connections
	//
	GenericConnImpl generic_conn;
	generic_conn.auth_user = generic_conn_auth_user;
	generic_conn.auth_pass = generic_conn_auth_pass;
	ConnFactory<GenericConnInterface, GenericConnImpl> generic_fact(&generic_conn);
	INIT_CHECK(GenericConn::instance.initialize(&generic_fact, generic_conn_count), "GenericConn");

	// SMS Sender
	//
	RTConn rt_conn;
	rt_conn._endpoint = rt_endpoint;
	rt_conn._timeout_ms = rt_timeout_ms;
	rt_conn._cp_tx_id_pref = rt_cp_tx_id_pref;
	rt_conn._cp_id = rt_cp_id;
	rt_conn._cp_user_id = rt_cp_user_id;
	rt_conn._cp_pass = rt_cp_pass;
	rt_conn._a_keyword = rt_a_keyword;
	rt_conn._s_keyword = rt_s_keyword;

	ConnFactory<SMSSenderInterface, RTConn> rt_factory(&rt_conn);
	INIT_CHECK(SMSSender::instance.initialize(&rt_factory, rt_conn_count), "SMSSender");

	// REST Handlers
	//
	ProductRESTHandler product_handler;
	AllProductsRESTHandler all_products_handler;
	ConfirmationCodeRESTHandler confirm_code_handler;
	confirm_code_handler._code_length = confirm_code_length;
	confirm_code_handler._msg_template = confirm_code_msg_tpl;
	confirm_code_handler._msg_sender = confirm_code_msg_sender;
	confirm_code_handler._queue_id = status_queue_id;

	// Routes
	//
	string root(root_path);

	rest::Router router;
	router.handle(root + "product", &product_handler);
	router.handle(root + "confirmationcode", &confirm_code_handler);
	router.handle(root + "allproducts", &all_products_handler);

	// Start server
	//
	if (router.start(port,
					 threads,
					 https_key_file,
					 https_cert_file,
					 https_key_pass,
					 https_priorities))
	{
		fprintf(stderr, "Failed to start server.\n");
		return -1;
	}

	while (!SHUTDOWN)
	{
		mt_sleep(1000);
	}

	router.stop();


	#ifndef WIN32
		join_signal_handler();
	#endif

	return 0;
}