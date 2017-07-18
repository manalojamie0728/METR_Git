#ifndef SERVER_H_
#define SERVER_H_

#include "OTTI/ott_integrator/src/mhd_http_server.h"

using namespace std;

class Server: public mhd::HttpServer
{
public:
	virtual ~Server();
	int api_handler(mhd::HttpRequest* request, mhd::HttpResponse* response);
	int call_operation(string action, string args[]);
};

#endif